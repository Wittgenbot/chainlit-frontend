import chainlit as cl
import cohere
import os

async def query_cohere(prompt):

    prompt = f'In the context of Ludwig Wittgenstein\'s Philosophical Investigations, answer the following question: {prompt}'

    co = cohere.Client(os.getenv('COHERE_API_KEY'))

    try:
        cohere_chat_async = cl.make_async(co.chat)
        response = await cohere_chat_async(message=prompt, model='command', temperature=0.9)
        words = response.text
    except Exception as e:
        print(f'An error has occurred: {e}')
        words = 'Oops, something went wrong!'

    return words


async def cohere_rerank_excerpts(question, documents, num_reranked_excerpts):

    text_to_source = { doc['text'] : doc['source'] for doc in documents }

    co = cohere.Client(os.getenv('COHERE_API_KEY'))
    cohere_rerank_async = cl.make_async(co.rerank)
    reranked_docs = await cohere_rerank_async(query=question,
                                              documents=[ doc['text'] for doc in documents ],
                                              top_n=num_reranked_excerpts,
                                              model='rerank-english-v2.0')

    reranked_texts = [ doc.document['text'] for doc in reranked_docs ]
    docs = [
        {
          'text': text,
          'source': text_to_source[text]
        } for text in reranked_texts
    ]

    return docs