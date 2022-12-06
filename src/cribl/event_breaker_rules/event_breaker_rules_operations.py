from cribl.lib.http_operations import *


def get_event_breaker_rules(base_url, cribl_auth_token, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = event_breaker_rules = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/lib/breakers",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/lib/breakers",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of pipelines: %s " % str(e))


def create_event_breaker_ruleset(base_url, cribl_auth_token, config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = config

    try:
        if worker_group is not None:
            return post(base_url + "/m/" + worker_group + "/lib/breakers",
                        headers=headers, payload=payload)
        else:
            return post(base_url + "/lib/breakers", headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create event breaker rule: %s" % str(e))


def update_event_breaker_ruleset(base_url, cribl_auth_token, config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = config

    try:
        if worker_group is not None:
            return patch(base_url + "/m/" + worker_group + "/lib/breakers" + "/" + config["id"],
                         headers=headers, payload=payload)
        else:
            return patch(base_url + "/lib/breakers" + "/" + config["id"], headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create event breaker rule: %s" % str(e))


def delete_event_breaker_ruleset(base_url, cribl_auth_token, config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = config

    try:
        if worker_group is not None:
            return patch(base_url + "/m/" + worker_group + "/lib/breakers" + "/" + config["id"],
                         headers=headers, payload=payload)
        else:
            return patch(base_url + "/lib/breakers" + "/" + config["id"], headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create event breaker rule: %s" % str(e))
