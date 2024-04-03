import asyncio
import random
from src.cohere_api import query_cohere
from src.foo_bar import query_foo_bar
from src.witt import query_witt
from utils.chat_profiles_enum import ChatProfile

async def stream_output(response):
    words = response.split(' ')
    for word in words:
        weights = [3, 1]
        sleep_range = [random.uniform(0.05, 0.25), random.uniform(0.3, 0.45)]
        sleep_time = random.choices(sleep_range, weights=weights)[0]
        await asyncio.sleep(sleep_time)
        yield word + ' '


async def query_chat_profile(question, chat_profile):

    response = ''

    match chat_profile:
        case ChatProfile.WITT_512_50:
            response = await query_witt(question, ChatProfile.WITT_512_50)
        case ChatProfile.WITT_1500_300:
            response = await query_witt(question, ChatProfile.WITT_1500_300)
        case ChatProfile.COHERE:
            response = await query_cohere(question)
        case ChatProfile.FOO_BAR:
            response = await query_foo_bar(question)

    async for word in stream_output(response):
        yield word