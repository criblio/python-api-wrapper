from cribl_python_api_wrapper.lib.http_operations import *


def get_profiler_objects(base_url, cribl_auth_token, worker_id):
    # get worker process profile
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/w/" + worker_id + "/system/profiler",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of profiler objects: %s" % str(e))
