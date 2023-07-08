from cribl_python_api_wrapper.lib.http_operations import *


def get_groups(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/master/groups",
                   headers=headers, payload=payload)
    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get list of worker groups: %s" % str(e))


def create_worker_group(base_url, cribl_auth_token, create_config):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = create_config

    try:
        return post(base_url + "/master/groups", headers=headers, payload=payload)
    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get create worker group: %s" % str(e))


def create_fleet(base_url, cribl_auth_token, create_config):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = create_config

    # ensure this is set to true
    payload["isFleet"] = True

    try:
        return post(base_url + "/master/groups", headers=headers, payload=payload)
    except Exception as e:
        raise Exception(
            "General exception raised while attempting to create fleet: %s" % str(e))


def create_subfleet(base_url, cribl_auth_token, parent_fleet_id, create_config):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = create_config

    # set inherits field to parent_fleet_id
    create_config["inherits"] = parent_fleet_id

    try:
        return post(base_url + "/master/groups", headers=headers, payload=payload)
    except Exception as e:
        raise Exception(
            "General exception raised while attempting to create subfleet: %s" % str(e))


def delete_worker_group(base_url, cribl_auth_token, worker_group_id):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return delete(base_url + "/master/groups/" + worker_group_id, headers=headers, payload=payload)
    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get delete worker group: %s" % str(e))


def deploy_commit(base_url, cribl_auth_token, version, worker_group=None, fleet=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json", "Authorization": "Bearer " + cribl_auth_token}
    payload = {
        "version": version
    }
    try:
        if worker_group is not None and fleet is None:
            return patch(base_url + "/master/groups/" + worker_group + "/deploy",
                         headers=headers, payload=payload)
        elif fleet is not None and worker_group is None:
            return patch(base_url + "/master/groups/" + fleet + "/deploy",
                         headers=headers, payload=payload)
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to commit configuration to Cribl: %s" % str(e))
