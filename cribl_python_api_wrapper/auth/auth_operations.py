from cribl_python_api_wrapper.lib.http_operations import *


def api_get_auth_data(base_url, username, password, verify=True):
    """
    Call API to get authorization data and token
    :param base_url:
    :param username:
    :param password:
    :param verify:
    :return authorization JSON object:
    """
    headers = {"Content-type": "application/json"}
    payload = {"username": username,
               "password": password}
    try:
        return post(base_url + "/auth/login",
                    headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to get auth data from Cribl: %s" % str(e))


def get_cloud_access_token(client_id, client_secret, login_server="https://login.cribl.cloud/oauth/token",
                           audience="https://api.cribl.cloud"):
    """
    Get access token from Cloud login service
    :param client_id:
    :param client_secret:
    :param login_server:
    :param audience:
    :return:
    """
    headers = {"Content-type": "application/json"}
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": audience
    }

    try:
        return post(login_server, headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to fetch cloud access token: %s" % str(e))
