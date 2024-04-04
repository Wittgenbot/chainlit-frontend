from chainlit import ChatProfile

wittgenbot_ft_chat_profile = ChatProfile(
    name='WITT-FT',
    markdown_description='<center>Wittgenbot fine-tuned on a QA dataset.</center>',
    icon='/public/WITT-FT_icon.png',
)

wittgenbot_0p5k_chat_profile = ChatProfile(
    name='WITT-0.5K',
    markdown_description='<center>Wittgenbot using RAG with a context length of 512.</center>',
    icon='/public/WITT-0.5K_icon.png',
)

wittgenbot_1p5k_chat_profile = ChatProfile(
    name='WITT-1.5K',
    markdown_description = '<center>Wittgenbot using RAG with a context length of 1500.</center>',
    icon='/public/WITT-1.5K_icon.png',
)