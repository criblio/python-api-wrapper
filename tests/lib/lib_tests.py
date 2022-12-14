from cribl.lib.http_operations import *


def lib_tests(base_url, cribl_auth_token):
    # return get(base_url + "/master/groups",
    #                    headers=headers, payload=payload)
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}

    response = get("http://localhost:19001/api/v1/master/workers", headers=headers, payload=None)

    print("Response: %s" % response.text)
