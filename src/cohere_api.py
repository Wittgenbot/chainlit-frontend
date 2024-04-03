import chainlit as cl
import cohere
import os

async def cohere_rerank_excerpts(question, documents, num_reranked_excerpts):

    co = cohere.Client(os.getenv('COHERE_API_KEY'))
    cohere_rerank_async = cl.make_async(co.rerank)
    reranked_response = await cohere_rerank_async(query=question,
                                                  documents=[ doc['text'] for doc in documents ],
                                                  top_n=num_reranked_excerpts,
                                                  model='rerank-english-v2.0')

    reranked_documents = [ documents[result.index] for result in reranked_response.results ]

    return reranked_documents