from cribl_python_api_wrapper.lib.http_operations import *


def get_workers(base_url, cribl_auth_token, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None
    try:
        return get(base_url + "/master/workers?filterExp=info.cribl.distMode%3D%3D%22worker%22",
                   headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to get list of workers: %s" % str(e))


def get_workers_and_edge_nodes(base_url, cribl_auth_token, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None
    try:
        return get(base_url + "/master/workers", headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to get list of workers and Edge nodes: %s" % str(e))


def restart_workers(base_url, cribl_auth_token, verify=True):
    headers = {
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None
    try:
        return patch(base_url + "/master/workers/restart", headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to restart workers: %s" % str(e))
