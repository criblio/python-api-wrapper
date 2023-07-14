import json
import sys
from cribl_python_api_wrapper.lookups import *
from cribl_python_api_wrapper.auth import *
from time import sleep


def read_config(filename):
    file = open(filename, "r")
    json_data = json.load(file)

    if "worker_group" in json_data:
        return json_data["base_url"], json_data["username"], json_data["password"], json_data["worker_group"]
    else:
        return json_data["base_url"], json_data["username"], json_data["password"]


# def export_lookup_file(base_url, cribl_auth_token, lookup_filename, save_to_directory, worker_group=None, fleet=None,
#                        verify=True):


def lookups_testing():
    print(f'Testing get_lookups()...')
    response = get_lookups(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group,
                           verify=False)
    print(f"Response: %s" % response.json())

    print("Testing export_lookup_file()...")
    response = export_lookup_file(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group,
                                  lookup_filename="host_timezone_mapping.csv", verify=False)

    # upload file first, then create lookup
    print("Testing upload_lookup_file()...")
    response = upload_lookup_file(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                  lookup_file="./services_names_port_numbers2.csv", worker_group=worker_group,
                                  verify=False)
    filename = None
    if "filename" in response.json():
        filename = response.json()["filename"]

    print("Response: %s" % response.json())

    config = {
        "id": "service_names_port_numbers2",
        "fileInfo": {
            "filename": filename
        }
    }

    print("Testing create_lookup()...")
    response = create_lookup(base_url=base_url, cribl_auth_token=cribl_auth_token, create_config=config,
                             worker_group=worker_group, verify=False)

    print("Response: %s" % response.text)


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
        lookups_testing()
    else:
        print(f"Bearer cribl_auth_token not returned from API. Exiting.")
        exit()
