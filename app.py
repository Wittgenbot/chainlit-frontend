import chainlit as cl
from utils.avatars import collect_avatars
from utils.chat_profiles import witt_0p5k_chat_profile, witt_1p5k_chat_profile, cohere_command_chat_profile, foo_bar_chat_profile
from src.query_model import ChatProfile, query_chat_profile

@cl.oauth_callback
def oauth_callback(provider_id, token, raw_user_data, default_user):
    return default_user


@cl.set_chat_profiles
async def list_chat_profiles():
    return [witt_0p5k_chat_profile, witt_1p5k_chat_profile, cohere_command_chat_profile, foo_bar_chat_profile]


@cl.on_chat_start
async def on_chat_start():
    chat_profile = cl.user_session.get('chat_profile')
    chat_profile_enum = ChatProfile.FOO_BAR
    author = 'FooBar'

    await collect_avatars()

    match chat_profile:
        case witt_0p5k_chat_profile.name:
            chat_profile_enum = ChatProfile.WITT_512_50
            author = 'Wittgenbot-0.5K'
        case witt_1p5k_chat_profile.name:
            chat_profile_enum = ChatProfile.WITT_1500_300
            author = 'Wittgenbot-1.5K'
        case cohere_command_chat_profile.name:
            chat_profile_enum = ChatProfile.COHERE
            author = 'Command'

    cl.user_session.set('chat_profile_enum', chat_profile_enum)
    cl.user_session.set('author', author)


@cl.on_message
async def main(message: cl.Message):
    chat_profile_enum = cl.user_session.get('chat_profile_enum')
    author = cl.user_session.get('author')

    msg = cl.Message(content='', author=author)
    await msg.send()

    async for token in query_chat_profile(question=message.content, chat_profile=chat_profile_enum):
        await msg.stream_token(token)

    await msg.update()