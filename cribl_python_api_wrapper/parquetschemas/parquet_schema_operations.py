from cribl_python_api_wrapper.lib.http_operations import *


def get_parquet_schemas(base_url, cribl_auth_token, worker_group=None, fleet=None, group=None, verify=True):
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
            return get(base_url + "/m/" + group + "/lib/parquet-schemas",
                       headers=headers, payload=payload, verify=verify)
        else:
            return get(base_url + "/lib/parquet-schemas",
                       headers=headers, payload=payload)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get parquet_schema information from Cribl: %s" % str(e))


def get_parquet_schema(base_url, cribl_auth_token, parquet_schema_id, worker_group=None, fleet=None, group=None, verify=True):
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
            return get(base_url + "/m/" + group + "/lib/parquet-schemas" + "/" + parquet_schema_id,
                       headers=headers, payload=payload, verify=verify)
        else:
            return get(base_url + "/lib/parquet-schemas" + "/" + parquet_schema_id,
                       headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create pipeline: %s " % str(e))


def create_parquet_schema(base_url, cribl_auth_token, config, worker_group=None, fleet=None, group=None, verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return post(base_url + "/m/" + group + "/lib/parquet-schemas/",
                        headers=headers, payload=payload, verify=verify)
        else:
            return post(base_url + "/lib/parquet-schemas",
                        headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create parquet_schema: %s " % str(e))


def update_parquet_schema(base_url, cribl_auth_token, parquet_schema_id, config, worker_group=None, fleet=None, group=None,
                  verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config

    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return patch(base_url + "/m/" + group + "/lib/parquet-schemas/" + parquet_schema_id,
                         headers=headers, payload=payload, verify=verify)
        else:
            return patch(base_url + "/lib/parquet-schemas/" + parquet_schema_id,
                         headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to update parquet_schema: %s " % str(e))


def delete_parquet_schema(base_url, cribl_auth_token, parquet_schema_id, worker_group=None, fleet=None, group=None, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        if worker_group is not None and fleet is None:
            group = worker_group
        elif fleet is not None and worker_group is None:
            group = fleet
        elif fleet is not None and worker_group is not None:
            raise Exception("Worker group and fleet were both set; operation can be performed on only one worker group"
                            " or fleet at a time.")
        if group is not None:
            return delete(base_url + "/m/" + group + "/lib/parquet-schemas/" + parquet_schema_id,
                          headers=headers, verify=verify)
        else:
            return delete(base_url + "/lib/parquet-schemas/" + parquet_schema_id,
                          headers=headers, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete input %s: %s" % (parquet_schema_id, str(e)))
