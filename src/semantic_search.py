import modal
import asyncio, nest_asyncio
import chainlit as cl

try:
    asyncio.get_event_loop()
    nest_asyncio.apply()
except RuntimeError:
    pass

async def semantic_search(question, index_type, num_matched_excerpts):
    modal_lookup_async = cl.make_async(modal.Function.lookup)
    semantic_search = await modal_lookup_async(app_name='philosophy-question-answerer',
                                               tag='semantic_search')

    modal_semantic_search_async = cl.make_async(semantic_search.remote)
    documents = await modal_semantic_search_async(question,
                                                  index_type,
                                                  num_matched_excerpts)

    return documents