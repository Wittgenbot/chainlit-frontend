import asyncio
import cohere
import os

async def query_cohere(prompt):
    co = cohere.Client(os.getenv('COHERE_API_KEY'))

    try:
        response = co.chat(message=prompt, model='command', temperature=0.9)
        words = response.text.split(' ')
    except Exception as e:
        print(f'An error has occurred: {e}', flush=True)
        words = 'Oops, something went wrong!'.split(' ')

    for word in words:
        await asyncio.sleep(0.1)
        yield word + ' '