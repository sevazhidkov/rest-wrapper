#!/usr/bin/env python
import sys
import json
from pprint import pprint
try:
    import requests
except ImportError:
    print(
        'Script requires requests package. \n'
        'You can install it by running "pip install requests"'
    )
    exit()

API_URL = 'http://jsonplaceholder.typicode.com/posts/'


def get_by_id(id):
    response = requests.get(API_URL + str(id))
    return json.loads(response.text)


def get_all():
    response = requests.get(API_URL)
    return json.loads(response.text)


def validate_id(post_id):
    if not post_id.isdigit():
        print('Post id should be digit')
        return False
    elif int(post_id) not in range(1, 100):
        print('Post id should be bigger than 0 and smaller than 100')
        return False
    return True

print('Loading data')
# If user didn't provided id, print all posts.
# Else - validate id and get post by id.
if len(sys.argv) == 1:
    pprint(get_all())
else:
    post_id = sys.argv[1]
    if validate_id(post_id):
        pprint(get_by_id(int(post_id)))
    else:
        print('Quitting')
