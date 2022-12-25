from cribl_python_api_wrapper.system import *


def system_testing(base_url, cribl_auth_token):
    print(f'\n\n\nTesting get_system_settings()...')
    response = get_system_settings(base_url=base_url, cribl_auth_token=cribl_auth_token)
    print(f"Response: %s" % response.json())

    print(f'\n\n\nTesting restart_cribl()...')
    response = restart_cribl(base_url=base_url, cribl_auth_token=cribl_auth_token)
    print(f"Response: %s" % response.json())

