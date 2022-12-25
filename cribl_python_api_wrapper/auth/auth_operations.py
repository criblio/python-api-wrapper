from cribl_python_api_wrapper.lib.http_operations import *


def api_get_auth_data(base_url, username, password):
    """
    Call API to get authorization data and token
    :param base_url:
    :param username:
    :param password:
    :return authorization JSON object:
    """
    headers = {"Content-type": "application/json"}
    payload = {"username": username,
               "password": password}
    try:
        return post(base_url + "/auth/login",
                    headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get auth data from Cribl: %s" % str(e))
