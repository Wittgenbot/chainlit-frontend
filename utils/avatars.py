from chainlit import Avatar

async def collect_avatars():
    await Avatar(name='Wittgenbot-Fine-Tuned', path='./public/WITT-FT_icon.png').send()
    await Avatar(name='Wittgenbot-512', path='./public/WITT-0.5K_icon.png').send()
    await Avatar(name='Wittgenbot-1500', path='./public/WITT-1.5K_icon.png').send()