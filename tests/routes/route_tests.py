import json
import sys
from cribl_python_api_wrapper.routes import *
from cribl_python_api_wrapper.auth import *
from time import sleep


def read_config(filename):
    file = open(filename, "r")
    json_data = json.load(file)

    if "worker_group" in json_data:
        return json_data["base_url"], json_data["username"], json_data["password"], json_data["worker_group"]
    else:
        return json_data["base_url"], json_data["username"], json_data["password"]


def routes_testing():
    print(f'Testing get_routes()...')
    response = get_routes(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
    print(f"Response: %s" % response.json())

    config = {
        "name": "test route 5",
        "final": True,
        "disabled": True,
        "pipeline": "apptraffic-reduce",
        "description": "Testing of route append",
        "filter": "__inputId=='datagen:datagen'",
        "output": "devnull"
    }

    print("Attempting to add new route %s" % config["name"])
    try:
        response = add_route(base_url, cribl_auth_token, route_config=config, position="start",
                             worker_group=worker_group)

        print("Response: %s" % response.json())
    except Exception as e:
        print("Exception: %s" % str(e))

    sleep(15)

    config = {
        "name": "test route 6",
        "final": True,
        "disabled": True,
        "pipeline": "apptraffic-reduce",
        "description": "Testing of route append",
        "filter": "__inputId.startsWith('syslog:in_syslog')",
        "output": "devnull"
    }
    sleep(15)

    print("Attempting to add new route %s" % config["name"])
    try:
        response = add_route(base_url, cribl_auth_token, route_config=config, position="start",
                             worker_group=worker_group)

        print("Response: %s" % response.json())
    except Exception as e:
        print("Exception: %s" % str(e))

    print(f'Testing get_routes_by_id()...')

    sleep(15)
    try:
        response = get_routes_by_id(base_url=base_url, cribl_auth_token=cribl_auth_token, route_id="default",
                                    worker_group=worker_group)
        print("Response: %s" % response.json())
    except Exception as e:
        print("Exception: %s" % str(e))

    sleep(15)
    try:
        response = delete_route(base_url=base_url, cribl_auth_token=cribl_auth_token, route_id="test route 5",
                                worker_group=worker_group)
        print("Response: %s" % response.json())
    except Exception as e:
        print("Exception: %s" % str(e))

    sleep(15)
    try:
        response = delete_route(base_url=base_url, cribl_auth_token=cribl_auth_token, route_id="test route 6",
                                worker_group=worker_group)
        print("Response: %s" % response.json())
    except Exception as e:
        print("Exception: %s" % str(e))


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
        response = api_get_auth_data(base_url=base_url, username=username, password=password)
        collectors = None
        if response.json() and "token" in response.json():
            cribl_auth_token = response.json()["token"]
    except Exception as e:
        print(f"Could not retrieve bearer cribl_auth_token. Reason: %s" % str(e))
        exit()

if cribl_auth_token is not None:
    routes_testing()
else:
    print(f"Bearer cribl_auth_token not returned from API. Exiting.")
    exit()
