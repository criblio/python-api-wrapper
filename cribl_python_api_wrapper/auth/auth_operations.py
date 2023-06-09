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


def get_cloud_access_token(client_id, client_secret):
    headers = {"Content-type": "application/json"}
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": "https://api.cribl.cloud"
    }
    try:
        return post("https://login.cribl.cloud/oauth/token", headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to fetch cloud access token: %s" % str(e))
