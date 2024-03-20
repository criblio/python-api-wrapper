import sys

from cribl_python_api_wrapper.auth import *
from cribl_python_api_wrapper.notifications import *


def notifications_testing():
    resp = get_notifications(base_url=base_url, cribl_auth_token=cribl_auth_token, )
    print("response: %s" % resp.json())
    #
    # resp = get_notification_target_by_id(base_url=base_url, cribl_auth_token=cribl_auth_token,
    #                                      notification_target_id="test_webhook")
    # print("response: %s" % resp.json())


def read_config(filename):
    file = open(filename, "r")
    json_data = json.load(file)

    if "worker_group" in json_data:
        return json_data["base_url"], json_data["username"], json_data["password"], json_data["worker_group"]
    else:
        return json_data["base_url"], json_data["username"], json_data["password"], None


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(f'Usage: %s --config-file <filename>' % sys.argv[0])
        exit()

    base_url, username, password, worker_group = read_config(filename=sys.argv[2])

    cribl_auth_token = None
    try:
        response = api_get_auth_data(base_url=base_url, username=username, password=password, verify=False)
        print("response: %s" % response.text)
        collectors = None
        if response.json() and "token" in response.json():
            cribl_auth_token = response.json()["token"]
    except Exception as e:
        print(f"Could not retrieve bearer cribl_auth_token. Reason: %s" % str(e))
        exit()

    if cribl_auth_token is not None:
        notifications_testing()
    else:
        print(f"Bearer cribl_auth_token not returned from API. Exiting.")
        exit()
