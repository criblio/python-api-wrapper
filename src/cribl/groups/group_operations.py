from cribl.lib.http_operations import *


def get_groups(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/master/groups",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to commit configuration to Cribl: %s" % str(e))


def deploy_commit(base_url, cribl_auth_token, version, worker_group):
    headers = {"Content-type": "application/json",
               "Accept": "application/json", "Authorization": "Bearer " + cribl_auth_token}
    payload = {
        "version": version
    }

    try:
        return patch(base_url + "/master/groups/" + worker_group + "/deploy",
                     headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to commit configuration to Cribl: %s" % str(e))
