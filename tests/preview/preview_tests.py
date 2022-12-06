from cribl.preview import *


def preview_testing(base_url, cribl_auth_token, worker_group):
    capture_params = {
        "filter": "__inputId.startsWith('syslog:in_syslog:')",
        "level": 1,
        "maxEvents": 20

    }
    response = capture_data(base_url=base_url, cribl_auth_token=cribl_auth_token, capture_params=capture_params,
                            worker_group=worker_group)
    print("response: %s" % response.text)


