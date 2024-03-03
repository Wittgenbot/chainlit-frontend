import chainlit as cl
from utils.chat_profiles import cohere_command_chat_profile, foo_bar_chat_profile
from utils.cohere import query_cohere
from utils.foo_bar import query_foo_bar

@cl.set_chat_profiles
async def list_chat_profiles():
    return [cohere_command_chat_profile, foo_bar_chat_profile]


@cl.on_chat_start
async def on_chat_start():
    chat_profile = cl.user_session.get('chat_profile')

    query_function = query_foo_bar
    if chat_profile == cohere_command_chat_profile.name:
        query_function = query_cohere

    cl.user_session.set('query_function', query_function)


@cl.on_message
async def main(message: cl.Message):
    query_function = cl.user_session.get('query_function')

    msg = cl.Message(content='')
    await msg.send()

    async for token in query_function(prompt=message.content):
        await msg.stream_token(token)

    await msg.update()