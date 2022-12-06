import time

from cribl.outputs import *

sleep_time = 3  # seconds


def outputs_testing(base_url, cribl_auth_token, worker_group=None):
    print(f'Testing get_outputs()...')
    response = get_outputs(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
    print(f"Response: %s" % response.json())

    print(f'\n\n\nTesting get_output_by_id()...')
    response = get_output_by_id(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                output_id="out_splunk", worker_group=worker_group)
    print(f"Response: %s" % response.json())

    print(f'\n\n\nTesting get_output_statuses()...')
    response = get_output_statuses(base_url, cribl_auth_token, worker_group)
    print(f'Response: %s' % response.json())

    print(f'\n\n\nTesting get_output_status_by_id()...')
    response = get_output_status_by_id(base_url, cribl_auth_token, "out_splunk", worker_group)
    print(f'output_status: %s' % response.json())

    print(f'\n')

    # # Splunk
    test_outputs(base_url, cribl_auth_token, "out_splunk_si_api", "splunk", worker_group, {
        "host": "nuc-ubuntu",
        "port": 19777
    }, {
                     "host": "nuc-ubuntu",
                     "port": 19778
                 })


def test_outputs(base_url, cribl_auth_token, output_id, output_type, worker_group, create_attributes,
                 update_attributes):
    print(f"Creating output " + output_id)
    create_attributes["id"] = output_id
    create_attributes["type"] = output_type
    response = create_output(base_url=base_url, cribl_auth_token=cribl_auth_token, create_config=create_attributes,
                             worker_group=worker_group)

    print(f'create output response: %s' % response.json())
    print(f"Sleeping - check UI for newly created output.\n")
    time.sleep(sleep_time)

    update_attributes["type"] = output_type
    print(f"Updating output " + output_id)
    response = update_output(base_url=base_url, cribl_auth_token=cribl_auth_token, output_id=output_id,
                             update_config=update_attributes, worker_group=worker_group)

    print(f"update output response: %s" % response.json())
    print(f"Sleeping - check output for update.\n")
    time.sleep(sleep_time)

    print(f"Deleting output " + output_id)
    response = delete_output(
        base_url=base_url, cribl_auth_token=cribl_auth_token, output_id=output_id, worker_group=worker_group)
    print(f"delete output response: %s" % response.json())

    print(f"\n")
