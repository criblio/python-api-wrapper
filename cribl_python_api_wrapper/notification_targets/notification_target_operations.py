from cribl_python_api_wrapper.lib.http_operations import *


def get_notification_targets(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/notification-targets",
                   headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to get list of notification_targets: %s" % str(e))


def get_notification_target_by_id(base_url, cribl_auth_token, notification_target_id):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/notification-targets/" + notification_target_id,
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get notification targets %s from Cribl: %s" % (
            notification_target_id, str(e)))


def create_notification_target(base_url, cribl_auth_token, create_config):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = create_config

    try:
        return post(base_url + "/notification-targets", headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create notification-targets: %s" % str(e))


def update_notification_target(base_url, cribl_auth_token, notification_target_id, update_config):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = update_config

    try:
        return patch(base_url + "/notification-targets/" + notification_target_id,
                     headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to update notification-targets %s: %s" % (
            notification_target_id, str(e)))


def delete_notification_target(base_url, cribl_auth_token, notification_target_id):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        return delete(base_url + "/notification-targets/" + notification_target_id,
                      headers=headers)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete notification-targets %s: %s" % (
            notification_target_id, str(e)))
