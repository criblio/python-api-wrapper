import time

from cribl_python_api_wrapper.pipelines import *

sleep_time = 3  # seconds


def pipelines_testing(base_url, cribl_auth_token, worker_group):
    print(f'Testing get_pipelines()...')
    response = get_pipelines(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
    print(f"Response: %s" % response.json())

    print(f'\n\n\nTesting get_pipeline_by_id()...')
    response = get_pipeline_by_id(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                  pipeline_id="main", worker_group=worker_group)
    print(f"Response: %s" % response.json())

    create_config = {
        "conf": {
            "functions": [
                {
                    "id": "eval",
                    "disabled": False,
                    "filter": "true",
                    "conf": {
                        "add": [
                            {
                                "name": "cribl",
                                "value": "'yes'"
                            }
                        ],
                        "remove": [

                        ]
                    }
                }
            ]
        }
    }

    update_config = {
        "conf": {
            "functions": [
                {
                    "id": "eval",
                    "disabled": False,
                    "filter": "true",
                    "conf": {
                        "add": [
                            {
                                "name": "cribl",
                                "value": "'yes'"
                            },
                            {
                                "name": "somefield",
                                "value": "somevalue"
                            }
                        ],
                        "remove": [

                        ]
                    }
                }
            ]
        }
    }

    test_pipelines(base_url=base_url, cribl_auth_token=cribl_auth_token, pipeline_id="rob_test_pipeline",
                   create_attributes=create_config, update_attributes=update_config, worker_group=worker_group)

    print(f'\n')


def test_pipelines(base_url, cribl_auth_token, pipeline_id, worker_group, create_attributes,
                   update_attributes):
    print(f"Creating pipeline " + pipeline_id)
    create_attributes["id"] = pipeline_id

    response = create_pipeline(base_url=base_url, cribl_auth_token=cribl_auth_token, create_config=create_attributes,
                               worker_group=worker_group)

    print(f'create pipeline response: %s' % response.json())
    print(f"Sleeping - check UI for newly created pipeline.\n")
    time.sleep(sleep_time)

    print(f"Updating pipeline " + pipeline_id)
    response = update_pipeline(base_url=base_url, cribl_auth_token=cribl_auth_token, pipeline_id=pipeline_id,
                               update_config=update_attributes, worker_group=worker_group)

    print(f"update pipeline response: %s" % response.json())
    print(f"Sleeping - check pipeline for update.\n")
    time.sleep(sleep_time)

    print(f"Deleting pipeline " + pipeline_id)
    response = delete_pipeline(
        base_url=base_url, cribl_auth_token=cribl_auth_token, pipeline_id=pipeline_id, worker_group=worker_group)
    print(f"delete pipeline response: %s" % response.json())

    print(f"\n")
