from cribl_python_api_wrapper.lib.http_operations import *


def capture_data(base_url, cribl_auth_token, capture_params, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = capture_params

    try:
        if worker_group is not None:
            response = post(base_url + "/m/" + worker_group + "/system/capture",
                            headers=headers, payload=payload)
        else:
            response = post(base_url + "/system/capture",
                            headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to capture incoming data: %s " % str(e))

    return response


def preview_data_pipelining(base_url, cribl_auth_token, preview_data_params, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = preview_data_params

    try:
        if worker_group is not None:
            response = post(base_url + "/m/" + worker_group + "/system/capture",
                            headers=headers, payload=payload)
        else:
            response = post(base_url + "/system/capture",
                            headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to preview data: %s " % str(e))

    return response
