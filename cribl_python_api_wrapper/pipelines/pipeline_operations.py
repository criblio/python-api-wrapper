from cribl_python_api_wrapper.lib.http_operations import *


def get_pipelines(base_url, cribl_auth_token, worker_group):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/pipelines/",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/pipelines",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get list of pipelines: %s " % str(e))


def get_pipeline_by_id(base_url, cribl_auth_token, pipeline_id, worker_group):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/pipelines" + "/" + pipeline_id,
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/pipelines" + "/" + pipeline_id,
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to get pipeline %s: %s " % (pipeline_id, str(e)))


def create_pipeline(base_url, cribl_auth_token, create_config, worker_group):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = create_config

    try:
        if worker_group is not None:
            return post(base_url + "/m/" + worker_group + "/pipelines/",
                        headers=headers, payload=payload)
        else:
            return post(base_url + "/pipelines",
                        headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to create pipeline: %s " % str(e))


def update_pipeline(base_url, cribl_auth_token, pipeline_id, update_config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = update_config

    try:
        if worker_group is not None:
            return patch(base_url + "/m/" + worker_group + "/pipelines/" + pipeline_id,
                         headers=headers, payload=payload)
        else:
            return patch(base_url + "/pipelines/" + pipeline_id,
                         headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to update pipeline: %s " % str(e))


def delete_pipeline(base_url, cribl_auth_token, pipeline_id, worker_group=None):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        if worker_group is not None:
            return delete(base_url + "/m/" + worker_group + "/pipelines/" + pipeline_id,
                          headers=headers)
        else:
            return delete(base_url + "/pipelines/" + pipeline_id,
                          headers=headers)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete input %s: %s" % (pipeline_id, str(e)))
