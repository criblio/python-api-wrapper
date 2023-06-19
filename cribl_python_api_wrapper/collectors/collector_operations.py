from cribl_python_api_wrapper.lib.http_operations import *


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


def get_collection_jobs(base_url, cribl_auth_token, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/lib/jobs", headers=headers, payload=payload)
        else:
            return get(base_url + "/lib/jobs", headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get collection job information from Cribl: %s" % str(e))


def get_collector_by_id(base_url, cribl_auth_token, collector_id, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = None

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


def create_collector(base_url, cribl_auth_token, create_config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = create_config

    try:
        if worker_group is not None:
            return post(base_url + "/m/" + worker_group + "/lib/jobs",
                        headers=headers, payload=payload)
        else:
            return post(base_url + "/lib/jobs",
                        headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get collector information from Cribl: %s" % str(e))
