from cribl_python_api_wrapper.lib.http_operations import *


def get_licenses(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/system/licenses",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of licenses: %s" % str(e))


def get_license_by_id(base_url, cribl_auth_token, license_id):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/system/licenses/" + license_id,
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get license %s from Cribl: %s" % (
            license_id, str(e)))


def get_license_usage_metrics(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/system/licenses/usage",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get license usage metrics: %s" % str(e))


def create_license(base_url, cribl_auth_token, create_config):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = create_config

    try:
        return post(base_url + "/system/licenses", headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create license: %s" % str(e))


def delete_license(base_url, cribl_auth_token, license_id):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        return delete(base_url + "/system/licenses/" + license_id, headers=headers)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete license %s: %s" % (license_id, str(e)))
