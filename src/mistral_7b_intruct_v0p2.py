import asyncio
import chainlit as cl
import modal
import nest_asyncio

try:
    asyncio.get_event_loop()
    nest_asyncio.apply()
except RuntimeError:
    pass

async def query_mistral(prompt):
    modal_lookup_async = cl.make_async(modal.Function.lookup)
    query_mistral_7b_instruct_v0p2 = await modal_lookup_async(app_name='wittgenbot',
                                                              tag='query_mistral_7b_instruct_v0p2')

    modal_query_async = cl.make_async(query_mistral_7b_instruct_v0p2.remote)
    response = await modal_query_async(prompt)

    return response