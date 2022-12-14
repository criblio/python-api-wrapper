from cribl.lib.http_operations import *


def api_get_auth_data(base_url, username, password):
    headers = {"Content-type": "application/json"}
    payload = {"username": username,
               "password": password}
    try:
        return post(base_url + "/auth/login",
                    headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get auth data from Cribl: %s" % str(e))
