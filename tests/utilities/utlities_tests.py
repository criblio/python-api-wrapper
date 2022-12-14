from cribl.utilities import *


def utilities_testing(base_url, cribl_auth_token, worker_group):
    route_data, pipeline_data, input_data, output_data, packs = \
        fetch_config(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)

    print(f"route data: %s" % route_data.json())
    print(f"\n\n\npipeline data: %s" % pipeline_data.json())
    print(f"\n\n\ninput data: %s" % input_data.json())
    print(f"\n\n\noutput data: %s" % output_data.json())
