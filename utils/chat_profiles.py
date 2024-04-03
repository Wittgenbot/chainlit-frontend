from chainlit import ChatProfile

wittgenbot_ft_chat_profile = ChatProfile(
    name='WITT-FT',
    markdown_description='Wittgenbot fine-tuned on a QA dataset.',
    icon='/public/WITT-FT_icon.png',
)

wittgenbot_0p5k_chat_profile = ChatProfile(
    name='WITT-0.5K',
    markdown_description='Wittgenbot with a context length of 512.',
    icon='/public/WITT-0.5K_icon.png',
)

wittgenbot_1p5k_chat_profile = ChatProfile(
    name='WITT-1.5K',
    markdown_description='Wittgenbot with a context length of 1500.',
    icon='/public/WITT-1.5K_icon.png',
)