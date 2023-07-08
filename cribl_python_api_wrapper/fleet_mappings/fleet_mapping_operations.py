from cribl_python_api_wrapper.lib.http_operations import *


def get_fleet_mappings(base_url, cribl_auth_token, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None
    try:
        return get(base_url + "/fleet-mappings", payload=payload, headers=headers, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to get fleet mappings: %s" % str(e))


def create_fleet_mapping(base_url, cribl_auth_token, fleet_mapping_config, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = fleet_mapping_config
    try:
        return post(base_url + "/fleet-mappings", payload=payload, headers=headers, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create fleet mappings: %s" % str(e))


def update_fleet_mapping(base_url, cribl_auth_token, fleet_mapping_id, fleet_mapping_config, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = fleet_mapping_config
    try:
        return patch(base_url + "/fleet-mappings" + "/" + fleet_mapping_id, payload=payload, headers=headers,
                     verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create fleet mappings: %s" % str(e))

