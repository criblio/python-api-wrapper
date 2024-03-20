from cribl_python_api_wrapper.collectors import *


def collector_testing(base_url, cribl_auth_token, worker_group):
    response = get_collection_jobs(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                   worker_group=worker_group)

    if "items" in response.json():
        for item in response.json()["items"]:
            if item["type"] == "collection":
                print("item: %s" % item["id"])
