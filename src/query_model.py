import asyncio
import random
from src.wittgenbot_ft import query_wittgenbot_ft
from src.wittgenbot_rag import query_wittgenbot_rag
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
        case ChatProfile.WITTGENBOT_FT:
            response = await query_wittgenbot_ft(question)
        case ChatProfile.WITTGENBOT_512_50:
            response = await query_wittgenbot_rag(question, ChatProfile.wittgenbot_512_50)
        case ChatProfile.WITTGENBOT_1500_300:
            response = await query_wittgenbot_rag(question, ChatProfile.wittgenbot_1500_300)

    async for word in stream_output(response):
        yield word