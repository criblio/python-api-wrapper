from cribl.lib.http_operations import *


def get_outputs(base_url, cribl_auth_token, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/system/outputs",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/system/outputs",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of outputs: %s" % str(e))


def get_output_by_id(base_url, cribl_auth_token, output_id, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/system/outputs/" + output_id,
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/m/" + worker_group + "/system/outputs/" + output_id,
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get output %s from Cribl: %s" % (
            output_id, str(e)))


def create_output(base_url, cribl_auth_token, create_config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = create_config

    if "status" in payload:
        del payload["status"]

    try:
        if worker_group is not None:
            return post(base_url + "/m/" + worker_group + "/system/outputs",
                        headers=headers, payload=payload)
        else:
            return post(base_url + "/system/outputs", headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create output: %s" % str(e))


def update_output(base_url, cribl_auth_token, output_id, update_config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = update_config

    try:
        if worker_group is not None:
            return patch(base_url + "/m/" + worker_group + "/system/outputs/" + output_id,
                         headers=headers, payload=payload)
        else:
            return patch(base_url + "/system/outputs/" + output_id, headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to update output %s: %s" % (output_id, str(e)))


def delete_output(base_url, cribl_auth_token, output_id, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        if worker_group is not None:
            return delete(base_url + "/m/" + worker_group + "/system/outputs/" + output_id,
                          headers=headers)
        else:
            return delete(base_url + "/system/outputs/" + output_id, headers=headers)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete output %s: %s" % (output_id, str(e)))


def get_output_statuses(base_url, cribl_auth_token, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/system/status/outputs",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/system/status/outputs",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get output statuses: %s" % str(e))


def get_output_status_by_id(base_url, cribl_auth_token, output_name, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/system/status/outputs/" + output_name,
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/system/status/outputs/" + output_name,
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get output status for %s: %s" % (output_name, str(e)))
