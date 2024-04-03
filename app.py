import chainlit as cl
from src.query_model import ChatProfile, query_chat_profile
from utils.avatars import collect_avatars
from utils.chat_profiles import wittgenbot_ft_chat_profile, wittgenbot_0p5k_chat_profile, wittgenbot_1p5k_chat_profile

@cl.oauth_callback
def oauth_callback(provider_id, token, raw_user_data, default_user):
    return default_user


@cl.set_chat_profiles
async def list_chat_profiles():
    return [wittgenbot_ft_chat_profile, wittgenbot_0p5k_chat_profile, wittgenbot_1p5k_chat_profile, ]


@cl.on_chat_start
async def on_chat_start():
    chat_profile = cl.user_session.get('chat_profile')

    await collect_avatars()

    match chat_profile:
        case wittgenbot_ft_chat_profile.name:
            chat_profile_enum = ChatProfile.WITTGENBOT_FT
            author = 'Wittgenbot-Fine-Tuned'
        case wittgenbot_0p5k_chat_profile.name:
            chat_profile_enum = ChatProfile.WITTGENBOT_512_50
            author = 'Wittgenbot-512'
        case wittgenbot_1p5k_chat_profile.name:
            chat_profile_enum = ChatProfile.WITTGENBOT_1500_300
            author = 'Wittgenbot-1500'

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