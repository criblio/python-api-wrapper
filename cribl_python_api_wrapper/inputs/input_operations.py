from cribl_python_api_wrapper.lib.http_operations import *


def get_inputs(base_url, cribl_auth_token, worker_group=None, fleet=None, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return get(base_url + "/m/" + group + "/system/inputs",
                       headers=headers, payload=payload, verify=verify)
        else:
            return get(base_url + "/system/inputs",
                       headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of inputs: %s" % str(e))


def get_input_by_id(base_url, cribl_auth_token, input_id, worker_group=None, fleet=None, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return get(base_url + "/m/" + group + "/system/inputs/" + input_id,
                       headers=headers, payload=payload, verify=verify)
        else:
            # single instance
            return get(base_url + "/system/inputs/" + input_id,
                       headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to get input %s from Cribl: %s" % (
            input_id, str(e)))


def create_input(base_url, cribl_auth_token, create_config, worker_group=None, fleet=None, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = create_config

    if "status" in payload:
        del payload["status"]

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return post(base_url + "/m/" + group + "/system/inputs",
                        headers=headers, payload=payload, verify=verify)
        else:
            # single instance
            return post(base_url + "/system/inputs", headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create input: %s" % str(e))


def update_input(base_url, cribl_auth_token, input_id, update_config, worker_group=None, fleet=None, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = update_config

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return patch(base_url + "/m/" + group + "/system/inputs/" + input_id,
                         headers=headers, payload=payload, verify=verify)
        else:
            # single instance
            return patch(base_url + "/system/inputs/" + input_id,
                         headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to update input %s: %s" % (input_id, str(e)))


def delete_input(base_url, cribl_auth_token, input_id, worker_group=None, fleet=None, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return delete(base_url + "/m/" + group + "/system/inputs/" + input_id,
                          headers=headers, verify=verify)
        else:
            # single instance
            return delete(base_url + "/system/inputs/" + input_id,
                          headers=headers, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete input %s: %s" % (input_id, str(e)))


def get_input_statuses(base_url, cribl_auth_token, worker_group=None, fleet=None, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return get(base_url + "/m/" + group + "/system/status/inputs",
                       headers=headers, payload=payload, verify=verify)
        else:
            # single instance
            return get(base_url + "/system/status/inputs",
                       headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to get input statuses: %s" % str(e))


def get_input_status_by_id(base_url, cribl_auth_token, input_name, worker_group=None, fleet=None, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return get(base_url + "/m/" + group + "/system/status/inputs/" + input_name,
                       headers=headers, payload=payload, verify=verify)
        else:
            # single instance
            return get(base_url + "/system/status/inputs/" + input_name,
                       headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get input status for %s: %s" % (input_name, str(e)))
