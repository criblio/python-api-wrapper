from cribl_python_api_wrapper.lib.http_operations import *


def get_mappings(base_url, cribl_auth_token, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None
    try:
        return get(base_url + "/mappings", payload=payload, headers=headers, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to get mappings: %s" % str(e))


def create_mapping(base_url, cribl_auth_token, mapping_config, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = mapping_config
    try:
        return post(base_url + "/mappings", payload=payload, headers=headers, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create mappings: %s" % str(e))


def update_mapping(base_url, cribl_auth_token, mapping_id, mapping_config, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = mapping_config
    try:
        return patch(base_url + "/mappings" + "/" + mapping_id, payload=payload, headers=headers,
                     verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to update mapping: %s" % str(e))
