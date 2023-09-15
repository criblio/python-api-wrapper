from cribl_python_api_wrapper.lib.http_operations import *


def get_system_settings(base_url, cribl_auth_token, verify=True):
    """
    Deprecated - use individual endpoints
    :param base_url:
    :param cribl_auth_token:
    :param verify:
    :return:
    """
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/system/settings",
                   headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get system settings from Cribl: %s" % str(e))


def get_system_settings_auth(base_url, cribl_auth_token, verify=True):
    """
    Get auth settings
    :param base_url:
    :param cribl_auth_token:
    :param verify:
    :return:
    """
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/system/settings/auth",
                   headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get auth settings from Cribl: %s" % str(e))


def update_system_settings_auth(base_url, cribl_auth_token, update_config, verify=True):
    """

    :param base_url:
    :param cribl_auth_token:
    :param update_config:
    :param verify:
    :return:
    """
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = update_config

    try:
        return patch(base_url + "/system/settings/auth",
                     headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to update auth settings from Cribl: %s" % str(e))


def restart_cribl(base_url, cribl_auth_token, verify=True):
    headers = {"Authorization": "Bearer " + cribl_auth_token}
    payload = None
    try:
        return post(base_url + "/system/settings/restart",
                    headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to restart instance: %s" % str(e))
