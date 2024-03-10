from chainlit import ChatProfile

ded_512 = ChatProfile(
    name='DED-0.5K',
    markdown_description='ChatDED 512',
    icon='https://picsum.photos/110',
)

ded_1500 = ChatProfile(
    name='DED-1.5K',
    markdown_description='ChatDED 1500',
    icon='https://picsum.photos/110',
)

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
