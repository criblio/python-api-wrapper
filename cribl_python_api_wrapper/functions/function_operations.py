from cribl_python_api_wrapper.lib.http_operations import *


def get_functions(base_url, cribl_auth_token, worker_group):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/functions",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/functions",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list functions %s" % str(e))


def get_function_by_id(base_url, cribl_auth_token, function_id, worker_group):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/functions/" + function_id,
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/functions" + function_id,
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list branches: %s" % str(e))