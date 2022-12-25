import requests
import json


# wrapper functions around requests methods
# returns Response object


def get(url, headers, payload):
    if payload is not None:
        r = requests.get(url, data=json.dumps(payload), headers=headers)
    else:
        r = requests.get(url, headers=headers)
    return r


def post(url, headers, payload):
    return requests.post(url, data=json.dumps(payload), headers=headers)


# should be used for file uploads (e.g. lookup files, packs)
def put(url, headers, data):
    return requests.put(url, headers=headers, data=data)


def patch(url, headers, payload):
    return requests.patch(url, data=json.dumps(payload), headers=headers)


def delete(url, headers):
    return requests.delete(url, headers=headers)
