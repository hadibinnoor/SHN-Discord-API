from requests import get
from decouple import config

API_KEY = config('HUMOR_API_KEY')


def get_random_joke():
    response = get(
        f'https://api.humorapi.com/jokes/random?api-key={API_KEY}').json()
    return response['joke']
