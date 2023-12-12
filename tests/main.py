import sys

from cribl_python_api_wrapper.auth import *
from inputs.input_tests import *
from outputs.outputs_tests import *
from pipelines.pipeline_tests import *
from routes.route_tests import *
from users.user_tests import *
from system.system_tests import *
from versioning.versioning_tests import *
from groups.group_tests import *
from functions.function_tests import *
from preview.preview_tests import *

from lib.lib_tests import *
from packs.pack_tests import *


def read_config(filename):
    file = open(filename, "r")
    json_data = json.load(file)

    if "worker_group" in json_data:
        if "ebr_data_file" in json_data:
            return json_data["base_url"], json_data["username"], json_data["password"], json_data["worker_group"], \
                   json_data["ebr_data_file"]
        return json_data["base_url"], json_data["username"], json_data["password"], json_data["worker_group"], None
    else:
        if "ebr_data_file" in json_data:
            return json_data["base_url"], json_data["username"], json_data["password"], None, json_data["ebr_data_file"]
        else:
            return json_data["base_url"], json_data["username"], json_data["password"], None


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(f'Usage: %s --config-file <filename>' % sys.argv[0])
        exit()

    base_url, username, password, worker_group, ebr_data_file = read_config(filename=sys.argv[2])

    cribl_auth_token = None
    try:
        response = api_get_auth_data(base_url=base_url, username=username, password=password)
        collectors = None
        if response.json() and "token" in response.json():
            cribl_auth_token = response.json()["token"]
    except Exception as e:
        print(f"Could not retrieve bearer cribl_auth_token. Reason: %s" % str(e))
        exit()

    if cribl_auth_token is not None:
        # inputs_testing(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
        # outputs_testing(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
        # routes_testing(base_url, cribl_auth_token, worker_group)
        # pipelines_testing(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
        # users_testing(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
        # system_testing(base_url, cribl_auth_token)
        # build_event_breaker_rules_from_csv(base_url=base_url, cribl_auth_token=cribl_auth_token,
        #                                    ebr_data_file=ebr_data_file, worker_group=worker_group)
        # versioning_testing(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
        # groups_testing(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
        # functions_testing(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
        # lib_tests(base_url=None, cribl_auth_token=cribl_auth_token)
        # preview_testing(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
        # packs_testing(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
        # utilities_testing(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)

        pass

    else:
        print(f"Bearer cribl_auth_token not returned from API. Exiting.")
        exit()
