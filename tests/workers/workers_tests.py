import json
import sys
import urllib3

from cribl_python_api_wrapper.auth import *
from cribl_python_api_wrapper.workers import *


def workers_testing():
    workers = get_workers(base_url=base_url, cribl_auth_token=cribl_auth_token, verify=False)
    print("workers: %s" % workers.json())

    workers_and_edge_nodes = get_workers_and_edge_nodes(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                                        verify=False)
    print("workers and edge nodes: %s" % workers_and_edge_nodes.json())

    result = restart_workers(base_url=base_url, cribl_auth_token=cribl_auth_token,
                             verify=False)

    print("Restart request result: %s" % result.json() + " | status code: %s" % result.status_code)


def read_config(filename):
    file = open(filename, "r")
    json_data = json.load(file)

    if "worker_group" in json_data:
        return json_data["base_url"], json_data["username"], json_data["password"], json_data["worker_group"]
    else:
        return json_data["base_url"], json_data["username"], json_data["password"]


if len(sys.argv) != 3:
    print(f'Usage: %s --config-file <filename>' % sys.argv[0])
    exit()

urllib3.disable_warnings()

base_url, username, password, worker_group = read_config(filename=sys.argv[2])
show_edge_workers = False

cribl_auth_token = None

if "cribl.cloud" in base_url:
    cribl_auth_token = password
else:
    try:
        response = api_get_auth_data(base_url=base_url, username=username, password=password, verify=False)
        if response.json() and "token" in response.json():
            cribl_auth_token = response.json()["token"]
    except Exception as e:
        print(f"Could not retrieve bearer cribl_auth_token. Reason: %s" % str(e))
        exit()

if cribl_auth_token is not None:
    workers_testing()
else:
    print(f"Bearer cribl_auth_token not returned from API. Exiting.")
    exit()
