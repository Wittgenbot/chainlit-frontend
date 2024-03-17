from chainlit import Avatar

async def collect_avatars():
    await Avatar(name='Wittgenbot-0.5K', path='./public/WITT-0.5K_icon.png').send()
    await Avatar(name='Wittgenbot-1.5K', path='./public/WITT-1.5K_icon.png').send()
    await Avatar(name='Command', path='./public/cohere_icon.png').send()
    await Avatar(name='FooBar', path='./public/foo_bar_icon.png').send()
