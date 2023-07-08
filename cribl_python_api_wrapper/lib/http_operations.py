import requests
import json


# wrapper functions around requests methods
# returns Response object

def get(url, headers, payload, stream=False, verify=True):
    if payload is not None:
        return requests.get(url, data=json.dumps(payload), headers=headers, stream=stream, verify=verify)
    else:
        return requests.get(url, headers=headers, stream=stream, verify=verify)


def post(url, headers, payload, verify=True):
    return requests.post(url, data=json.dumps(payload), headers=headers, verify=verify)


# should be used for file uploads (e.g. lookup files, packs)
def put(url, headers, data, verify=True):
    return requests.put(url, headers=headers, data=data, verify=verify)


def patch(url, headers, payload, verify=True):
    return requests.patch(url, data=json.dumps(payload), headers=headers, verify=verify)


def delete(url, headers, payload=None, verify=True):
    if payload is not None:
        return requests.delete(url, headers=headers, verify=verify, data=json.dumps(payload))
    else:
        return requests.delete(url, headers=headers, verify=verify)
