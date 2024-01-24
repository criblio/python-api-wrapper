from cribl_python_api_wrapper.lib.http_operations import *
import os


def get_lookups(base_url, cribl_auth_token, worker_group=None, verify=True, use_session=False):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/system/lookups",
                       headers=headers, payload=payload, verify=verify, use_session=use_session)
        else:
            return get(base_url + "/system/lookups",
                       headers=headers, payload=payload, verify=verify, use_session=use_session)

    except Exception as e:
        raise Exception("General exception raised while attempting to get lookups from Cribl: %s" % str(e))


def create_lookup(base_url, cribl_auth_token, create_config, worker_group=None, fleet=None, verify=True,
                  use_session=False):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = create_config

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return post(base_url + "/m/" + group + "/system/lookups",
                        headers=headers, payload=payload, verify=verify, use_session=use_session)
        else:
            return post(base_url + "/system/lookups",
                        headers=headers, payload=payload, verify=verify, use_session=use_session)
    except Exception as e:
        raise Exception("General exception raised while attempting to create lookup: %s " % str(e))


def export_lookup_file(base_url, cribl_auth_token, lookup_filename, save_to_directory=".",
                       worker_group=None, fleet=None, verify=True, use_session=False):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            response = get(base_url + "/m/" + group + "/system/lookups" + "?filename=" + lookup_filename,
                           headers=headers, payload=payload, verify=verify, use_session=use_session)
        else:
            response = get(base_url + "/system/lookups" + "?filename=" + lookup_filename,
                           headers=headers, payload=payload, verify=verify, use_session=use_session)

        if response.status_code == 200:
            lookup_filename = open(save_to_directory + "/" + lookup_filename, "wb")
            lookup_filename.write(response.content)
            lookup_filename.close()

    except Exception as e:
        raise Exception("General exception raised while attempting to export pack: %s " % str(e))

    return response


def upload_lookup_file(base_url, cribl_auth_token, lookup_file, worker_group=None, fleet=None, verify=True,
                       use_session=False):
    headers = {"Authorization": "Bearer " + cribl_auth_token}

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return put(base_url + "/m/" + group + "/system/lookups?filename=" + os.path.basename(lookup_file),
                       headers=headers, data=open(lookup_file, 'rb'), verify=verify, use_session=use_session)
        else:
            return put(base_url + "/system/lookups?filename=" + + os.path.basename(lookup_file),
                       headers=headers, data=open(lookup_file, 'rb'), verify=verify, use_session=use_session)
    except Exception as e:
        raise Exception("General exception raised while attempting to create lookup: %s " % str(e))
