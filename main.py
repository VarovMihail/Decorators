from datetime import datetime
import requests
from log_tools import logger



@logger
def product(a, b):
    return a * b

HOST = 'https://swapi.dev/api/'

@logger
def get_people(char_id):
    return requests.get(f'{HOST}people/{char_id}').json()


if __name__ == '__main__':
    product(10,6)
    get_people(1)


















