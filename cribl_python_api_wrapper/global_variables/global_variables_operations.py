from cribl_python_api_wrapper.lib.http_operations import *


def get_global_variables(base_url, cribl_auth_token, worker_group=None, fleet=None):
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
            return get(base_url + "/m/" + group + "/lib/vars",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/lib/vars",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of global variables: %s" % str(e))


def get_global_variable_by_id(base_url, cribl_auth_token, global_variable_id, worker_group=None, fleet=None):
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
            return get(base_url + "/m/" + group + "/lib/vars/" + global_variable_id,
                       headers=headers, payload=payload)
        else:
            # single instance
            return get(base_url + "/lib/vars/" + global_variable_id,
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get global variable %s from Cribl: %s" % (
            global_variable_id, str(e)))


def create_global_variable(base_url, cribl_auth_token, create_config, worker_group=None, fleet=None):
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
            return post(base_url + "/m/" + group + "/lib/vars",
                        headers=headers, payload=payload)
        else:
            # single instance
            return post(base_url + "/lib/vars", headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create global variable: %s" % str(e))


def update_global_variable(base_url, cribl_auth_token, global_variable_id, update_config, worker_group=None,
                           fleet=None):
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
            return patch(base_url + "/m/" + group + "/lib/vars/" + global_variable_id,
                         headers=headers, payload=payload)
        else:
            # single instance
            return patch(base_url + "/lib/vars/" + global_variable_id,
                         headers=headers, payload=payload)
    except Exception as e:
        raise Exception(
            "General exception raised while attempting to update global_variable %s: %s" % (global_variable_id, str(e)))


def delete_global_variable(base_url, cribl_auth_token, global_variable_id, worker_group=None, fleet=None):
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
            return delete(base_url + "/m/" + group + "/lib/vars/" + global_variable_id,
                          headers=headers)
        else:
            # single instance
            return delete(base_url + "/lib/vars/" + global_variable_id,
                          headers=headers)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to delete global_variable %s: %s" % (global_variable_id, str(e)))
