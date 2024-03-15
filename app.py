import chainlit as cl
from utils.chat_profiles import ded_512, ded_1500, cohere_command_chat_profile, foo_bar_chat_profile
from src.query_model import ChatProfile, query_chat_profile

@cl.oauth_callback
def oauth_callback(provider_id, token, raw_user_data, default_user):
    return default_user


@cl.set_chat_profiles
async def list_chat_profiles():
    return [ded_512, ded_1500, cohere_command_chat_profile, foo_bar_chat_profile]


@cl.on_chat_start
async def on_chat_start():
    chat_profile = cl.user_session.get('chat_profile')
    chat_profile_enum = ChatProfile.FOO_BAR
    match chat_profile:
        case ded_512.name:
            chat_profile_enum = ChatProfile.DED_512_50
        case ded_1500.name:
            chat_profile_enum = ChatProfile.DED_1500_300
        case cohere_command_chat_profile.name:
            chat_profile_enum = ChatProfile.COHERE
    cl.user_session.set('chat_profile_enum', chat_profile_enum)


@cl.on_message
async def main(message: cl.Message):
    chat_profile_enum = cl.user_session.get('chat_profile_enum')

    msg = cl.Message(content='')
    await msg.send()

    async for token in query_chat_profile(question=message.content, chat_profile=chat_profile_enum):
        await msg.stream_token(token)

    await msg.update()