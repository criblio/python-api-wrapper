import requests
import json


# wrapper functions around requests methods
# returns Response object


def get(url, headers, payload, stream=False):
    if payload is not None:
        return requests.get(url, data=json.dumps(payload), headers=headers, stream=stream)
    else:
        return requests.get(url, headers=headers, stream=stream)


def post(url, headers, payload):
    return requests.post(url, data=json.dumps(payload), headers=headers)


# should be used for file uploads (e.g. lookup files, packs)
def put(url, headers, data):
    return requests.put(url, headers=headers, data=data)


def patch(url, headers, payload):
    return requests.patch(url, data=json.dumps(payload), headers=headers)


def delete(url, headers, payload=None):
    if payload is not None:
        return requests.delete(url, headers=headers, data=json.dumps(payload))
    else:
        return requests.delete(url, headers=headers)
