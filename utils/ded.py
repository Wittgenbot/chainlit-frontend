import chainlit as cl
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import textwrap
from utils.cohere import cohere_rerank_excerpts
from utils.chat_profiles_enum import ChatProfile
from utils.mistral_7b_intruct_v0p2 import query_mistral

def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2',
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'device': 'cpu', 'batch_size': 10}
    )

embedding_model = load_embedding_model()


def load_faiss_index(chunk_size, chunk_overlap):
    return FAISS.load_local(f'faiss_indices/chunk_size_{chunk_size}_chunk_overlap_{chunk_overlap}',
                            embedding_model,
                            allow_dangerous_deserialization=True)

faiss_index_512_50 = load_faiss_index(512, 50)
faiss_index_1500_300 = load_faiss_index(1500, 300)


async def generate_step_output(documents):

    source_frequency = {}
    for doc in documents:
        source = doc['source']
        if source in source_frequency:
            source_frequency[source] += 1
        else:
            source_frequency[source] = 1

    step_output = ''
    for source, frequency in source_frequency.items():
        source_parts = source.split('/')[-1].rstrip('.txt')
        step_output += f'- **{frequency} excerpts** from `{source_parts}`\n\n'

    return step_output


@cl.step(name='Semantic Search')
async def find_semantically_similar_documents(question, ded_profile, num_matched_excerpts):

    match ded_profile:
        case ChatProfile.DED_512_50:
            faiss_index = faiss_index_512_50
        case ChatProfile.DED_1500_300:
            faiss_index = faiss_index_1500_300

    results = faiss_index.similarity_search(query=question, k=num_matched_excerpts)
    documents = [
        {
            'text': result.page_content,
            'source': result.metadata['source']
        } for result in results
    ]

    current_step_output = f'From the following sources, {num_matched_excerpts} excerpts were semantically matched to the question:\n'
    current_step_output += await generate_step_output(documents)
    cl.context.current_step.output = current_step_output

    return documents


@cl.step(name='Reranking')
async def rerank_excerpts(question, documents, num_reranked_excerpts):
   reranked_documents = await cohere_rerank_excerpts(question, documents, num_reranked_excerpts)

   current_step_output = f'The matched excerpts were reranked in terms of relevance. The {num_reranked_excerpts} most relevant excerpts were selected from the following sources:\n'
   current_step_output += await generate_step_output(reranked_documents)
   cl.context.current_step.output = current_step_output
   return reranked_documents


async def create_prompt(question, documents):
    context = ''
    for doc in documents:
        context = context + textwrap.fill(doc['text'], 150) + '\n' + textwrap.fill(doc['source'], 150) + '\n\n'
    prompt = f'''
Answer the following QUESTION with the given CONTEXT. \n\n
QUESTION: {question} \n
CONTEXT: \n {context} \n
ANSWER:
'''
    return prompt


async def query_ded(question, chat_profile):
    semantically_similar_documents = await find_semantically_similar_documents(question, chat_profile, num_matched_excerpts=25)
    reranked_documents = await rerank_excerpts(question, semantically_similar_documents, num_reranked_excerpts=3)
    prompt = await create_prompt(question, reranked_documents)
    response = await query_mistral(prompt)
    return response