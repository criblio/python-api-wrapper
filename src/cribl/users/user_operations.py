from cribl.lib.http_operations import *


def get_users(base_url, cribl_auth_token, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/system/users",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/system/users",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of users: %s" % str(e))


def get_user_by_id(base_url, cribl_auth_token, user_id, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/system/users/" + user_id,
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/m/" + worker_group + "/system/users/" + user_id,
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get user %s from Cribl: %s" % (
            user_id, str(e)))


def create_user(base_url, cribl_auth_token, create_config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    payload = create_config

    try:
        if worker_group is not None:
            return post(base_url + "/m/" + worker_group + "/system/users",
                        headers=headers, payload=payload)
        else:
            return post(base_url + "/system/users", headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create user: %s" % str(e))


def update_user(base_url, cribl_auth_token, user_id, update_config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = update_config

    try:
        if worker_group is not None:
            return patch(base_url + "/m/" + worker_group + "/system/users/" + user_id,
                         headers=headers, payload=payload)
        else:
            return patch(base_url + "/system/users/" + user_id, headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to update user %s: %s" % (user_id, str(e)))


def delete_user(base_url, cribl_auth_token, user_id, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        if worker_group is not None:
            return delete(base_url + "/m/" + worker_group + "/system/users/" + user_id,
                          headers=headers)
        else:
            return delete(base_url + "/system/users/" + user_id, headers=headers)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete user %s: %s" % (user_id, str(e)))
