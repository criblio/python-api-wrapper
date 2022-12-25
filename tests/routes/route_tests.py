from cribl_python_api_wrapper.routes import *


def routes_testing(base_url, cribl_auth_token, worker_group):
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

    config = {
        "name": "test route 6",
        "final": True,
        "disabled": True,
        "pipeline": "apptraffic-reduce",
        "description": "Testing of route append",
        "filter": "__inputId.startsWith('syslog:in_syslog')",
        "output": "devnull"
    }

    print("Attempting to add new route %s" % config["name"])
    try:
        response = add_route(base_url, cribl_auth_token, route_config=config, position="start",
                             worker_group=worker_group)

        print("Response: %s" % response.json())
    except Exception as e:
        print("Exception: %s" % str(e))

    print(f'Testing get_routes_by_id()...')

    try:
        response = get_routes_by_id(base_url=base_url, cribl_auth_token=cribl_auth_token, route_id="default",
                                    worker_group=worker_group)
        print("Response: %s" % response.json())
    except Exception as e:
        print("Exception: %s" % str(e))

    try:
        response = delete_route(base_url=base_url, cribl_auth_token=cribl_auth_token, route_id="test route 5",
                                worker_group=worker_group)
        print("Response: %s" % response.json())
    except Exception as e:
        print("Exception: %s" % str(e))

    try:
        response = delete_route(base_url=base_url, cribl_auth_token=cribl_auth_token, route_id="test route 6",
                                worker_group=worker_group)
        print("Response: %s" % response.json())
    except Exception as e:
        print("Exception: %s" % str(e))
