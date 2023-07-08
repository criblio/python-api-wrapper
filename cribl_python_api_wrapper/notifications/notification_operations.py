from cribl_python_api_wrapper.lib.http_operations import *


def get_notifications(base_url, cribl_auth_token, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/notifications", headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to get list of "
                        "notification definitions: %s" % str(e))


def create_notification(base_url, cribl_auth_token, notification_config, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = notification_config

    try:
        return post(base_url + "/notifications", headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create notification definitions: %s" % str(e))


def update_notification(base_url, cribl_auth_token, notification_id, notification_config, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = notification_config
    try:
        return patch(base_url + "/notifications" + "/" + notification_id, payload=payload, headers=headers,
                     verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to update notification: %s" % str(e))
