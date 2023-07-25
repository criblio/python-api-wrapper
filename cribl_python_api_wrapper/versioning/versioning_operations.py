from cribl_python_api_wrapper.lib.http_operations import *


def get_branches(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/version/branch",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list branches: %s" % str(e))


def get_versioning_availability(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/version/info",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get version availability: %s" % str(e))


def get_commit_details(base_url, cribl_auth_token, commit_hash="HEAD", group_id="default"):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = {
        "commit": commit_hash,
        "group": group_id
    }

    try:
        return get(base_url + "/version/show",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get commit (%s) details: %s" % (commit_hash, str(e)))


def get_working_tree_status(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/version/status",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list branches: %s" % str(e))


def create_commit(base_url, cribl_auth_token, commit_config, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = commit_config

    try:
        return post(base_url + "/version/commit", headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create commit: %s" % str(e))


def get_changed_file_count(base_url, cribl_auth_token):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/version/count",
                   headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list branches: %s" % str(e))
