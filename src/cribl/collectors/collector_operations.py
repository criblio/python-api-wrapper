from ..lib.http_operations import *


def get_collectors(base_url, cribl_auth_token, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/collectors",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/collectors",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get collector information from Cribl: %s" % str(e))


def get_collector_by_id(base_url, cribl_auth_token, collector_id, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = collector = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/collectors/" + collector_id,
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/collectors/" + collector_id,
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get collector information from Cribl: %s" % str(e))
