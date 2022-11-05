from random import randint


def generate_random_url():
    MEME_COUNT = 1478
    meme_id = randint(1, MEME_COUNT)
    return f'https://raw.githubusercontent.com/TinkerHub-Farook-College/discord-server-hooks/main/memes/{meme_id}.png'
