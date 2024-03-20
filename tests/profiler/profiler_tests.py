from cribl_python_api_wrapper.profiler import *


def profiler_testing(base_url, cribl_auth_token, worker_id):
    response = get_profiler_objects(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                    worker_id=worker_id)
    print("response: %s" % response.text)
