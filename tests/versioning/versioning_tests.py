from cribl_python_api_wrapper.versioning import *
from cribl_python_api_wrapper.inputs import *
from cribl_python_api_wrapper.groups import *

import time


def versioning_testing(base_url, cribl_auth_token, worker_group=None):
    # print(f'Testing get_branches()...')
    # response = get_branches(base_url=base_url, cribl_auth_token=cribl_auth_token, )
    # print(f"Response: %s" % response.json())
    #
    # print(f'\n\n\nTesting get_versionining_availability()...')
    # response = get_versioning_availability(base_url=base_url, cribl_auth_token=cribl_auth_token, )
    # print(f"Response: %s" % response.json())
    #

    print(f'\n\n\nTesting create input and commit...')
    create_attributes = {
        "queueName": "aQueue",
        "region": "us-west-1"
    }
    input_id = "in_s3_api_3"
    input_type = "s3"

    create_attributes["id"] = input_id
    create_attributes["type"] = input_type

    response = create_input(base_url=base_url, cribl_auth_token=cribl_auth_token, create_config=create_attributes,
                            worker_group=worker_group)
    print(f"Response: %s" % response.json())

    time.sleep(5)

    #
    # print(f'\n\n\nTesting get_commit_details()...')
    # response = get_commit_details(base_url=base_url, cribl_auth_token=cribl_auth_token, )
    # print(f"Response: %s" % response.json())
    #
    # print(f'\n\n\nTesting get_working_tree_status()...')
    # response = get_working_tree_status(base_url=base_url, cribl_auth_token=cribl_auth_token, )
    # print(f"Response: %s" % response.json())

    print(f"Testing create_commit()...")
    response = create_commit(base_url=base_url, cribl_auth_token=cribl_auth_token, commit_config={
        "group": worker_group,
        "branch": "master",
        "message": "test commit - 12/5/2022"
    }, )
    print(f"Response: %s" % response.json())
    commit_version = response.json()['items'][0]['commit']
    print("Commit version: %s" % commit_version)
    time.sleep(5)

    print(f'Testing deploy_commit()...')
    response = deploy_commit(base_url=base_url, cribl_auth_token=cribl_auth_token, version=commit_version,
                             worker_group=worker_group)
    print(f"Response: %s" % response.json())
    print(f"Code: %s" % response.status_code)

    # print(f'\n\n\nTesting get_count_of_changed_files()...')
    # response = get_changed_file_count(base_url=base_url, cribl_auth_token=cribl_auth_token,)
    # print(f"Response: %s" % response.json())
