from cribl_python_api_wrapper.lib.http_operations import *


def get_system_messages(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/system/messages",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get system messages: %s" % str(e))


def delete_system_message(base_url, cribl_auth_token, message_id):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return delete(base_url + "/system/messages" + "/" + message_id,
                      headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete system message: %s" % str(e))
