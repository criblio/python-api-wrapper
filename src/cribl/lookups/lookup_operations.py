from cribl.lib.http_operations import *


def get_lookups(base_url, cribl_auth_token, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/system/lookups",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/system/lookups",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get lookups from Cribl: %s" % str(e))
