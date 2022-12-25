from cribl_python_api_wrapper.routes.route_operations import *
from cribl_python_api_wrapper.pipelines.pipeline_operations import *
from cribl_python_api_wrapper.inputs.input_operations import *
from cribl_python_api_wrapper.outputs.output_operations import *
from cribl_python_api_wrapper.packs.pack_operations import *


def fetch_config(base_url, cribl_auth_token, worker_group):
    route_data = get_routes(base_url, cribl_auth_token, worker_group)
    pipeline_data = get_pipelines(base_url, cribl_auth_token, worker_group)
    input_data = get_inputs(base_url, cribl_auth_token, worker_group)
    output_data = get_outputs(base_url, cribl_auth_token, worker_group)
    packs = get_pack_list(base_url, cribl_auth_token, worker_group)

    return route_data, pipeline_data, input_data, output_data, packs
