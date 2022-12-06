from ..lib.http_operations import *


def get_parsers(base_url, cribl_auth_token, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = parsers = None

    try:
        if worker_group is not None:
            response = get(base_url + "/m/" + worker_group + "/lib/parsers",
                           headers=headers, payload=payload)
        else:
            response = get(base_url + "/lib/parsers",
                           headers=headers, payload=payload)

        if response.status_code == 200:
            if response.json() and response.json()["items"]:
                parsers = response.json()

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get parser information from Cribl: %s" % str(e))

    return parsers


def get_parser(base_url, cribl_auth_token, parser_id, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            response = get(base_url + "/m/" + worker_group + "/lib/parsers" + "/" + parser_id,
                           headers=headers, payload=payload)
        else:
            response = get(base_url + "/lib/parsers" + "/" + parser_id,
                           headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create pipeline: %s " % str(e))

    return response


def create_parser(base_url, cribl_auth_token, config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config

    try:
        if worker_group is not None:
            response = post(base_url + "/m/" + worker_group + "/lib/parsers/",
                            headers=headers, payload=payload)
        else:
            response = post(base_url + "/lib/parsers",
                            headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create pipeline: %s " % str(e))

    return response


def update_parser(base_url, cribl_auth_token, parser_id, config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config

    try:
        if worker_group is not None:
            response = patch(base_url + "/m/" + worker_group + "/lib/parsers/" + parser_id,
                             headers=headers, payload=payload)
        else:
            response = patch(base_url + "/lib/parsers/" + parser_id,
                             headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to update parser: %s " % str(e))

    return response


def delete_parser(base_url, cribl_auth_token, parser_id, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        if worker_group is not None:
            response = delete(base_url + "/m/" + worker_group + "/lib/parsers/" + parser_id,
                              headers=headers)
        else:
            response = delete(base_url + "/system/inputs/" + parser_id,
                              headers=headers)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete input %s: %s" % (parser_id, str(e)))

    return response
