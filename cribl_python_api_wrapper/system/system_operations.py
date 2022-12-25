from cribl_python_api_wrapper.lib.http_operations import *


def get_system_settings(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/system/settings",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get system settings from Cribl: %s" % str(e))


def restart_cribl(base_url, cribl_auth_token):
    headers = {"Authorization": "Bearer " + cribl_auth_token}
    payload = None
    try:
        return post(base_url + "/system/settings/restart",
                    headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to restart instance: %s" % str(e))
