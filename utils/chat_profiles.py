from chainlit import ChatProfile

cohere_command_chat_profile = ChatProfile(
    name='Command',
    markdown_description='Command is Cohere\'s flagship text generation model.',
    icon='/public/Cohere_logo.svg',
)

foo_bar_chat_profile = ChatProfile(
    name='FooBar',
    markdown_description='FooBar model',
    icon='https://picsum.photos/100',
)
