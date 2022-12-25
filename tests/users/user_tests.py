from cribl_python_api_wrapper.users import *


def users_testing(base_url, cribl_auth_token, worker_group=None):
    print(f'Testing get_users()...')
    response = get_users(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
    print(f"Response: %s" % response.json())

    print(f'\n\n\nTesting get_user_by_id()...')
    response = get_user_by_id(base_url=base_url, cribl_auth_token=cribl_auth_token,
                              user_id="admin", worker_group=worker_group)
    print(f"Response: %s" % response.json())

    user_config = {
        "disabled": False,
        "email": "b@b.com",
        "first": "A",
        "id": "rfranz-api-admin",
        "last": "B",
        "password": "admin123",
        "username": "rfranz-api-admin",
        "roles": ["admin"]
    }

    print(f'\n\n\nTesting create_user()...')
    response = create_user(base_url=base_url, cribl_auth_token=cribl_auth_token,
                           create_config=user_config, worker_group=worker_group)

    print(f"Response: %s" % response.json())

    user_config = {
        "disabled": False,
        "email": "mynewemailaddress@host.com",
        "first": "A",
        "id": "rfranz-api-admin",
        "last": "B",
        "password": "admin12345678",
        "username": "rfranz-api-admin",
        "roles": ["admin"]
    }

    print(f'\n\n\nTesting update_user()...')
    response = update_user(base_url=base_url, cribl_auth_token=cribl_auth_token,
                           update_config=user_config, user_id="rfranz-api-admin", worker_group=worker_group)

    print(f"Response: %s" % response.json())

    print(f'\n\n\nTesting delete_user()...')
    response = delete_user(base_url=base_url, cribl_auth_token=cribl_auth_token,
                           user_id="rfranz-api-admin", worker_group=worker_group)
    print(f"Response: %s" % response.json())

    print(f'\n')
