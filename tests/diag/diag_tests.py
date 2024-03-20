import sys
from cribl_python_api_wrapper.auth import *
from cribl_python_api_wrapper.diag import *
from cribl_python_api_wrapper.workers import *


def diag_testing():
    worker_data = get_workers(base_url=base_url, cribl_auth_token=cribl_auth_token, )
    print("workers: %s" % worker_data.json())

    response = get_health(base_url=base_url, cribl_auth_token=cribl_auth_token)
    print("response: %s" % response.text)

    response = get_leader_system_info(base_url=base_url, cribl_auth_token=cribl_auth_token)
    print("response: %s" % response.text)

    workers = []

    if 'items' in worker_data.json():
        for worker in worker_data.json()["items"]:
            workers.append(worker)

    for worker in workers:
        response = get_worker_system_info(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_id=worker["id"])
        print("response - get_worker_system_info(): %s" % response.text)

        print(f"writing diagnostic bundle to disk.")
        print("worker: %s" % worker)
        response = get_diagnostic_bundle(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                         hostname=worker["info"]["hostname"],
                                         save_to_directory="/Users/rfranz/github/python-api-wrapper/")
        print("response: %s" % response)


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

base_url, username, password, worker_group = read_config(filename=sys.argv[2])
show_edge_workers = False

cribl_auth_token = None

if "cribl.cloud" in base_url:
    cribl_auth_token = password
else:
    try:
        auth_response = api_get_auth_data(base_url=base_url, username=username, password=password)
        collectors = None
        if auth_response.json() and "token" in auth_response.json():
            cribl_auth_token = auth_response.json()["token"]
    except Exception as e:
        print(f"Could not retrieve bearer cribl_auth_token. Reason: %s" % str(e))
        exit()

if cribl_auth_token is not None:
    diag_testing()
else:
    print(f"Bearer cribl_auth_token not returned from API. Exiting.")
    exit()
