from datetime import datetime
import requests
from log_tools_2 import logger

#path_to_file = r'Logs/log.log'

@logger('Logs/log.log')
def product(a, b):
    return a * b

HOST = 'https://swapi.dev/api/'

@logger('Logs/log.log')
def get_people(char_id):
    return requests.get(f'{HOST}people/{char_id}').json()


if __name__ == '__main__':
    product(10,6)
    get_people(1)


















