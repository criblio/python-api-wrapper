from cribl_python_api_wrapper.lib.http_operations import *


def get_health(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/health",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get health %s" % str(e))


def get_leader_system_info(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/system/info",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get health %s" % str(e))


def get_worker_system_info(base_url, cribl_auth_token, worker_id):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/w/" + worker_id + "/system/info",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get health %s" % str(e))


def get_diagnostic_bundle(base_url, cribl_auth_token, hostname, save_to_directory, options=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None
    bundle_name = None

    try:
        if options is not None:
            response = get(base_url + "/system/diag/download" + "?" + options,
                           headers=headers, payload=payload, stream=True)
        else:
            response = get(base_url + "/system/diag/download",
                           headers=headers, payload=payload, stream=True)

        if response.status_code == 200:
            from datetime import datetime
            import os
            if os.path.exists(save_to_directory) is False:
                os.mkdir(save_to_directory)
            now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
            diagnostic_bundle = open(save_to_directory + "/" + hostname + "-" + now + ".tar.gz", "wb")
            diagnostic_bundle.write(response.content)
            diagnostic_bundle.close()

            bundle_name = save_to_directory + "/" + hostname + "-" + now + ".tar.gz"

    except Exception as e:
        raise Exception("General exception raised while attempting to get diagnostic bundle: %s" % str(e))
    return bundle_name
