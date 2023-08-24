from cribl_python_api_wrapper.lib.http_operations import *


def get_regexes(base_url, cribl_auth_token, worker_group=None, fleet=None, group=None, verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")

        if group is not None:
            return get(base_url + "/m/" + group + "/lib/regex",
                       headers=headers, payload=payload, verify=verify)
        else:
            return get(base_url + "/lib/regex",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get parser information from Cribl: %s" % str(e))


def get_regex(base_url, cribl_auth_token, regex_id, worker_group=None, fleet=None, group=None, verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return get(base_url + "/m/" + group + "/lib/regex" + "/" + regex_id,
                       headers=headers, payload=payload, verify=verify)
        else:
            return get(base_url + "/lib/regex" + "/" + regex_id,
                       headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create pipeline: %s " % str(e))


def create_regex(base_url, cribl_auth_token, config, worker_group=None, fleet=None, group=None, verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return post(base_url + "/m/" + group + "/lib/regex/",
                        headers=headers, payload=payload, verify=verify)
        else:
            return post(base_url + "/lib/regex",
                        headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create pipeline: %s " % str(e))


def update_regex(base_url, cribl_auth_token, regex_id, config, worker_group=None, fleet=None, group=None,
                 verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return patch(base_url + "/m/" + group + "/lib/regex/" + regex_id,
                         headers=headers, payload=payload, verify=verify)
        else:
            return patch(base_url + "/lib/regex/" + regex_id,
                         headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to update parser: %s " % str(e))


def delete_regex(base_url, cribl_auth_token, regex_id, worker_group=None, fleet=None, group=None, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return delete(base_url + "/m/" + group + "/lib/regex/" + regex_id,
                          headers=headers, verify=verify)
        else:
            return delete(base_url + "/lib/regex/" + regex_id,
                          headers=headers, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete input %s: %s" % (regex_id, str(e)))
