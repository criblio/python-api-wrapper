import sys

from cribl_python_api_wrapper.auth import *
from cribl_python_api_wrapper.event_breaker_rules import *


def read_config(filename):
    file = open(filename, "r")
    json_data = json.load(file)

    if "worker_group" in json_data:
        return json_data["base_url"], json_data["username"], json_data["password"], json_data["worker_group"]
    else:
        return json_data["base_url"], json_data["username"], json_data["password"]


# def export_lookup_file(base_url, cribl_auth_token, lookup_filename, save_to_directory, worker_group=None, fleet=None,
#                        verify=True):


def event_breaker_rules_testing():
    print(f'Testing get_event_breaker_rules()...')
    response = get_event_breaker_rules(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group,
                                       verify=False)
    print(f"Response: %s" % response.json())


if __name__ == '__main__':
    import urllib3

    urllib3.disable_warnings()
    if len(sys.argv) != 3:
        print(f'Usage: %s --config-file <filename>' % sys.argv[0])
        exit()

    base_url, username, password, worker_group = read_config(filename=sys.argv[2])
    show_edge_workers = False

    cribl_auth_token = None

    if "cribl.cloud" in base_url:
        cribl_auth_token = password
    else:
        try:
            response = api_get_auth_data(base_url=base_url, username=username, password=password, verify=False)
            collectors = None
            if response.json() and "token" in response.json():
                cribl_auth_token = response.json()["token"]
        except Exception as e:
            print(f"Could not retrieve bearer cribl_auth_token. Reason: %s" % str(e))
            exit()

    if cribl_auth_token is not None:
        event_breaker_rules_testing()
    else:
        print(f"Bearer cribl_auth_token not returned from API. Exiting.")
        exit()
