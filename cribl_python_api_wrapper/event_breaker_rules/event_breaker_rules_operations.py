from cribl_python_api_wrapper.lib.http_operations import *


def get_event_breaker_rules(base_url, cribl_auth_token, worker_group=None, fleet=None, group=None, verify=True):
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
            return get(base_url + "/m/" + group + "/lib/breakers",
                       headers=headers, payload=payload, verify=verify)
        else:
            return get(base_url + "/lib/breakers",
                       headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of pipelines: %s " % str(e))


def create_event_breaker_ruleset(base_url, cribl_auth_token, config, worker_group=None, fleet=None, group=None,
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
            return post(base_url + "/m/" + group + "/lib/breakers",
                        headers=headers, payload=payload, verify=verify)
        else:
            return post(base_url + "/lib/breakers", headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create event breaker rule: %s" % str(e))


def update_event_breaker_ruleset(base_url, cribl_auth_token, config, worker_group=None, fleet=None, group=None,
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
            return patch(base_url + "/m/" + group + "/lib/breakers" + "/" + config["id"],
                         headers=headers, payload=payload, verify=verify)
        else:
            return patch(base_url + "/lib/breakers" + "/" + config["id"], headers=headers, payload=payload,
                         verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to update event breaker rule: %s" % str(e))


def delete_event_breaker_ruleset(base_url, cribl_auth_token, config, worker_group=None, fleet=None, group=None,
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
            return patch(base_url + "/m/" + group + "/lib/breakers" + "/" + config["id"],
                         headers=headers, payload=payload, verify=verify)
        else:
            return patch(base_url + "/lib/breakers" + "/" + config["id"], headers=headers, payload=payload,
                         verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to delete event breaker rule: %s" % str(e))
