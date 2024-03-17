from chainlit import ChatProfile

witt_0p5k_chat_profile = ChatProfile(
    name='WITT-0.5K',
    markdown_description='Wittgenbot with a context length of 512.',
    icon='/public/WITT-0.5K_icon.png',
)

witt_1p5k_chat_profile = ChatProfile(
    name='WITT-1.5K',
    markdown_description='Wittgenbot with a context length of 1500.',
    icon='/public/WITT-1.5K_icon.png',
)

cohere_command_chat_profile = ChatProfile(
    name='Command',
    markdown_description='Cohere\'s flagship text generation model.',
    icon='/public/cohere_icon.png',
)

foo_bar_chat_profile = ChatProfile(
    name='FooBar',
    markdown_description='FooBar model',
    icon='/public/foo_bar_icon.png',
)
