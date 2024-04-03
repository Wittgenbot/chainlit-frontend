import chainlit as cl
from src.cohere_api import cohere_rerank_excerpts
from src.mistral_7b_intruct_v0p2 import query_mistral
from src.semantic_search import semantic_search
import textwrap
from utils.chat_profiles_enum import ChatProfile

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
        source_parts = source.split('/')[-1].rstrip('.txt').split(' by ')
        book_name = source_parts[0]
        author_name = source_parts[1] if len(source_parts) > 1 else 'Unknown'
        step_output += f"- **{frequency} {'excerpt' if frequency == 1 else 'excerpts'}** from `{book_name}` by {author_name}\n\n"

    return step_output


@cl.step(name='Semantic Search')
async def find_semantically_similar_documents(question, wittgenbot_profile, num_matched_excerpts):

    match wittgenbot_profile:
        case ChatProfile.wittgenbot_512_50:
            index_type = { 'chunk_size': 512, 'chunk_overlap': 50 }
        case ChatProfile.wittgenbot_1500_300:
            index_type = { 'chunk_size': 1500, 'chunk_overlap': 300 }

    documents = await semantic_search(question, index_type, num_matched_excerpts)

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


@cl.step(name='Querying the Model')
async def query_model(prompt):
    response = await query_mistral(prompt)
    current_step_output = f'Based on the context, the **Mistral-7B-Instruct-v0.2 Model** answered the question as follows:\n\n'
    current_step_output +=  response
    cl.context.current_step.output = current_step_output
    return response


async def query_wittgenbot_rag(question, chat_profile):
    semantically_similar_documents = await find_semantically_similar_documents(question, chat_profile, num_matched_excerpts=25)
    reranked_documents = await rerank_excerpts(question, semantically_similar_documents, num_reranked_excerpts=3)
    prompt = await create_prompt(question, reranked_documents)
    response = await query_model(prompt)
    return response