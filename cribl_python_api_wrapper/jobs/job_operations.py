from cribl_python_api_wrapper.lib.http_operations import *


def get_jobs(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/jobs",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of jobs: %s" % str(e))
