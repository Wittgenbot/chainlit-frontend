import asyncio
import chainlit as cl
import modal
import nest_asyncio

try:
    asyncio.get_event_loop()
    nest_asyncio.apply()
except RuntimeError:
    pass

async def query_wittgenbot_ft(question):
    modal_lookup_async = cl.make_async(modal.Function.lookup)
    query_wittgenbot_ft = await modal_lookup_async(app_name='wittgenbot',
                                                              tag='query_wittgenbot_ft')

    modal_query_async = cl.make_async(query_wittgenbot_ft.remote)
    response = await modal_query_async(question)

    return response