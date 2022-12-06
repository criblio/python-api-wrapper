from cribl.functions import *


def functions_testing(base_url, cribl_auth_token, worker_group=None):
    print(f'Testing get_functions...')
    response = get_functions(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
    print(f"Response: %s" % response.json())

    print(f'Testing get_function_by_id...')
    response = get_function_by_id(base_url=base_url, cribl_auth_token=cribl_auth_token, function_id="dns_lookup",
                                  worker_group=worker_group)
    print(f"Response: %s" % response.json())
