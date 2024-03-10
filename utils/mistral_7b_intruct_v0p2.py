import modal

async def query_mistral(prompt):
    print('fetching the function')
    query_mistral_7b_instruct_v0p2 = modal.Function.lookup(app_name='philosophy-question-answerer', tag='query_mistral_7b_instruct_v0p2')
    print('querying Mistral')
    response = query_mistral_7b_instruct_v0p2.remote(prompt)
    return response