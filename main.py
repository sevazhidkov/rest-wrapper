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


def send_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.RequestException as error:
        print('Error while sending request: ', error)
        exit()


def get_by_id(id):
    response = send_request(API_URL + str(id))
    return json.loads(response.text)


def get_all():
    response = send_request(API_URL)
    return json.loads(response.text)


def validate_id(post_id):
    if not post_id.isdigit():
        print('Post id should be digit')
        return False
    elif int(post_id) not in range(1, 100):
        print('Post id should be bigger than 0 and smaller than 100')
        return False
    return True


def print_post(post):
    for (key, value) in post.items():
        print key + ':', value

print('Loading data')
# If user didn't provided id, print all posts.
# Else - validate id and get post by id.
if len(sys.argv) == 1:
    posts = get_all()
    for post in posts:
        print_post(post)
        print
else:
    post_id = sys.argv[1]
    if validate_id(post_id):
        post = get_by_id(int(post_id))
        print_post(post)
    else:
        print('Quitting')
