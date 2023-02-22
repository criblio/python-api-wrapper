from cribl_python_api_wrapper.messages import *


def messages_testing(base_url, cribl_auth_token):
    print(f'Testing get_system_messages()...')
    response = get_system_messages(base_url=base_url, cribl_auth_token=cribl_auth_token)
    print(f"Response: %s" % response.json())

    print(f'Testing delete_system_message()...')
    response = delete_system_message(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                     message_id="no-data")
    print(f"Response: %s" % response.text)
