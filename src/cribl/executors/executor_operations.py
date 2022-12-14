from cribl.lib.http_operations import *


def get_executors(base_url, cribl_auth_token, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/executors",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/executors",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get executor information from Cribl: %s" % str(e))


def get_executor_by_id(base_url, cribl_auth_token, executor_id, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/executors" + "/" + executor_id,
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/executors" + "/" + executor_id,
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get executor information from Cribl: %s" % str(e))
