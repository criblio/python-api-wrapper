from cribl_python_api_wrapper.lib.http_operations import *


def get_pipelines(base_url, cribl_auth_token, worker_group=None, fleet=None, verify=True):
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
            return get(base_url + "/m/" + group + "/pipelines/", headers=headers, payload=payload, verify=verify)
        else:
            return get(base_url + "/pipelines", headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of pipelines: %s " % str(e))


def get_pipeline_by_id(base_url, cribl_auth_token, pipeline_id, worker_group=None, fleet=None, verify=True):
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
            return get(base_url + "/m/" + group + "/pipelines" + "/" + pipeline_id,
                       headers=headers, payload=payload, verify=verify)
        else:
            return get(base_url + "/pipelines" + "/" + pipeline_id,
                       headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to get pipeline %s: %s " % (pipeline_id, str(e)))


def create_pipeline(base_url, cribl_auth_token, create_config, worker_group=None, fleet=None, verify=True):
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
            return post(base_url + "/m/" + group + "/pipelines/",
                        headers=headers, payload=payload, verify=verify)
        else:
            return post(base_url + "/pipelines",
                        headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create pipeline: %s " % str(e))


def update_pipeline(base_url, cribl_auth_token, pipeline_id, update_config, worker_group=None, fleet=None, verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = update_config

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return patch(base_url + "/m/" + group + "/pipelines/" + pipeline_id,
                         headers=headers, payload=payload, verify=verify)
        else:
            return patch(base_url + "/pipelines/" + pipeline_id,
                         headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to update pipeline: %s " % str(e))


def delete_pipeline(base_url, cribl_auth_token, pipeline_id, worker_group=None, fleet=None, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return delete(base_url + "/m/" + group + "/pipelines/" + pipeline_id,
                          headers=headers, verify=verify)
        else:
            return delete(base_url + "/pipelines/" + pipeline_id,
                          headers=headers, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete input %s: %s" % (pipeline_id, str(e)))


def create_pipeline_in_pack(base_url, cribl_auth_token, create_config, pack_id, worker_group=None, fleet=None,
                            group=None,
                            verify=True):
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
            return post(base_url + "/m/" + group + "/p/" + pack_id + "/pipelines",
                        headers=headers, payload=payload, verify=verify)
        else:
            return post(base_url + "/p/" + pack_id + "/pipelines",
                        headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create pipeline in pack: %s " % str(e))


def update_pipeline_in_pack(base_url, cribl_auth_token, pipeline_id, update_config, pack_id, worker_group=None,
                            fleet=None, verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = update_config

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return patch(base_url + "/m/" + group + "/p/" + pack_id + "/pipelines/" + pipeline_id,
                         headers=headers, payload=payload, verify=verify)
        else:
            return patch(base_url + "/p/" + pack_id + "/pipelines/" + pipeline_id,
                         headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to update pipeline in pack: %s " % str(e))


def delete_pipeline_in_pack(base_url, cribl_auth_token, pipeline_id, pack_id, worker_group=None, fleet=None,
                            verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        else:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return delete(base_url + "/m/" + group + "/p/" + pack_id + "/pipelines/" + pipeline_id,
                          headers=headers, verify=verify)
        else:
            return delete(base_url + "/pipelines/" + pipeline_id,
                          headers=headers, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete pipeline in pack: %s" % str(e))
