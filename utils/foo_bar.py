import asyncio

async def query_foo_bar(prompt):
    response = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
At auctor urna nunc id cursus metus. Risus sed vulputate odio ut enim blandit volutpat maecenas volutpat. \
Elementum integer enim neque volutpat ac tincidunt vitae. Sit amet mattis vulputate enim.m \
Est lorem ipsum dolor sit amet consectetur adipiscing. \
Lectus urna duis convallis convallis tellus id interdum velit. \
Porta non pulvinar neque laoreet suspendisse interdum. \
Viverra tellus in hac habitasse platea dictumst vestibulum rhoncus.'

    words = response.split(' ')
    for word in words:
        await asyncio.sleep(0.1)
        yield word + ' '