from cribl_python_api_wrapper.lib.http_operations import *
import os.path

import warnings


def export_pack_merge_safe(base_url, cribl_auth_token, pack_id, save_to_directory, worker_group=None, fleet=None,
                           group=None, verify=True, use_session=False):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            response = get(base_url + "/m/" + group + "/packs/" + pack_id + "/export?mode=merge_safe",
                           headers=headers, payload=payload, verify=verify, use_session=use_session)
        else:
            response = get(base_url + "/packs/" + pack_id + "export?mode=merge_safe",
                           headers=headers, payload=payload, verify=verify, use_session=use_session)

        if response.status_code == 200:
            pack = open(save_to_directory + "/" + pack_id + ".crbl", "wb")
            pack.write(response.content)
            pack.close()

    except Exception as e:
        raise Exception("General exception raised while attempting to export pack: %s " % str(e))

    return response


def export_pack_merge(base_url, cribl_auth_token, pack_id, save_to_directory, worker_group=None, fleet=None,
                      group=None, verify=True, use_session=False):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            response = get(base_url + "/m/" + group + "/packs/" + pack_id + "/export?mode=merge",
                           headers=headers, payload=payload, verify=verify, use_session=use_session)
        else:
            response = get(base_url + "/packs/" + pack_id + "export?mode=merge",
                           headers=headers, payload=payload, verify=verify, use_session=use_session)

        if response.status_code == 200:
            pack = open(save_to_directory + "/" + pack_id + ".crbl", "wb")
            pack.write(response.content)
            pack.close()

    except Exception as e:
        raise Exception("General exception raised while attempting to export pack: %s " % str(e))

    return response


def get_pack_list(base_url, cribl_auth_token, worker_group=None, fleet=None, group=None, verify=True,
                  use_session=False):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return get(base_url + "/m/" + group + "/packs",
                       headers=headers, payload=payload, verify=verify, use_session=use_session)
        else:
            return get(base_url + "/packs",
                       headers=headers, payload=payload, verify=verify, use_session=use_session)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of installed packs: %s " % str(e))


def get_pipelines_in_pack(base_url, cribl_auth_token, pack_id, worker_group=None, fleet=None, group=None, verify=True,
                          use_session=False):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return get(base_url + "/m/" + group + "/p/" + pack_id + "/pipelines",
                       headers=headers, payload=payload, verify=verify, use_session=use_session)
        else:
            return get(base_url + "/p/" + pack_id + "/pipelines",
                       headers=headers, payload=payload, verify=verify, use_session=use_session)
    except Exception as e:
        raise Exception("General exception raised while attempting to get list of pipelines in pack: %s " % str(e))


def get_routes_in_pack(base_url, cribl_auth_token, pack_id, worker_group=None, fleet=None, group=None, verify=True,
                       use_session=False):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return get(base_url + "/m/" + group + "/p/" + pack_id + "/routes",
                       headers=headers, payload=payload, verify=verify, use_session=use_session)
        else:
            return get(base_url + "/p/" + pack_id + "/routes",
                       headers=headers, payload=payload, verify=verify, use_session=use_session)
    except Exception as e:
        raise Exception("General exception raised while attempting to get list of pipelines in pack: %s " % str(e))


def upload_and_install_pack(base_url, cribl_auth_token, pack_file, worker_group=None, fleet=None, group=None,
                            verify=True,
                            use_session=False):
    headers = {"Authorization": "Bearer " + cribl_auth_token}

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            response = put(base_url + "/m/" + group + "/packs?filename=" + os.path.basename(pack_file),
                           headers=headers, data=open(pack_file, 'rb'), verify=verify, use_session=use_session)
        else:
            response = put(base_url + "/packs?filename=" + os.path.basename(pack_file), headers=headers,
                           data=open(pack_file, 'rb'), verify=verify, use_session=use_session)

        if response.status_code == 200:
            if "source" in response.json():
                pack_source = response.json()["source"]
                headers = {"Content-type": "application/json",
                           "Authorization": "Bearer " + cribl_auth_token}
                payload = {
                    "source": pack_source
                }
            else:
                return response

            if worker_group is not None:
                response = post(base_url + "/m/" + worker_group + "/packs",
                                headers=headers, payload=payload, verify=verify, use_session=use_session)
            else:
                response = post(base_url + "/packs",
                                headers=headers, payload=payload, verify=verify, use_session=use_session)
    except Exception as e:
        raise Exception("General exception raised while attempting to upload and install pack: %s " % str(e))

    return response


def upload_pack(base_url, cribl_auth_token, pack_file, worker_group=None, fleet=None, group=None, verify=True,
                use_session=False):
    headers = {"Authorization": "Bearer " + cribl_auth_token}

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            response = put(base_url + "/m/" + group + "/packs?filename=" + os.path.basename(pack_file),
                           headers=headers, data=open(pack_file, 'rb'), verify=verify, use_session=use_session)
        else:
            response = put(base_url + "/packs?filename=" + os.path.basename(pack_file), headers=headers,
                           data=open(pack_file, 'rb'), verify=verify, use_session=use_session)
    except Exception as e:
        raise Exception("General exception raised while attempting to upload pack: %s " % str(e))

    return response


def install_pack(base_url, cribl_auth_token, pack_source, pack_id=None, worker_group=None, fleet=None, verify=True,
                 use_session=False):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = {
        "source": pack_source
    }

    warnings.warn("install_pack is deprecated. Use create_pack instead.", DeprecationWarning)

    group = None

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")

        if group is not None:
            response = post(base_url + "/m/" + group + "/packs",
                            headers=headers, payload=payload, verify=verify, use_session=use_session)
        else:
            response = post(base_url + "/packs",
                            headers=headers, payload=payload, verify=verify, use_session=use_session)
    except Exception as e:
        raise Exception("General exception raised while attempting to install pack: %s " % str(e))

    return response


def create_pack(base_url, cribl_auth_token, create_config, worker_group=None, fleet=None, group=None, verify=True,
                use_session=False):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = create_config

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")

        if group is not None:
            response = post(base_url + "/m/" + group + "/packs",
                            headers=headers, payload=payload, verify=verify, use_session=use_session)
        else:
            response = post(base_url + "/packs",
                            headers=headers, payload=payload, verify=verify, use_session=use_session)
    except Exception as e:
        raise Exception("General exception raised while attempting to install pack: %s " % str(e))

    return response
