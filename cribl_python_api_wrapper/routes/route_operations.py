from cribl_python_api_wrapper.lib.http_operations import *


def get_routes(base_url, cribl_auth_token, worker_group):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/routes",
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/routes", headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to get route listing from Cribl: %s" % str(e))


def get_routes_by_id(base_url, cribl_auth_token, route_id, worker_group):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        if worker_group is not None:
            return get(base_url + "/m/" + worker_group + "/routes" + "/" + route_id,
                       headers=headers, payload=payload)
        else:
            return get(base_url + "/routes" + "/" + route_id, headers=headers, payload=payload)
    except Exception as e:
        raise Exception("General exception raised while attempting to get route listing from Cribl: %s" % str(e))


def add_route(base_url, cribl_auth_token, route_config, position="start", worker_group=None):
    # Attempt to add new route
    try:
        # get a list of the existing routes
        current_routes = get_routes(base_url, cribl_auth_token, worker_group).json()
        route_exists = False

        if "items" in current_routes and len(current_routes["items"]) != 0:
            current_route_config = current_routes["items"][0]

            for current_route in current_route_config["routes"]:
                if route_config["name"] == current_route["name"]:
                    route_exists = True
                    break
            # don't add the route if we find the name in the list. API does not stop us from adding
            # routes with duplicate names.
            if route_exists is False:
                if position == "end":
                    current_routes["items"][0]["routes"].append(route_config)
                else:
                    # default to beginning of routes
                    current_routes["items"][0]["routes"].insert(0, route_config)

                return _update_routes(base_url, cribl_auth_token,
                                      {"id": "default", "routes": current_routes["items"][0]["routes"]},
                                      worker_group=worker_group)
            else:
                raise Exception("Route %s already exists." % route_config["name"])
    except Exception as e:
        raise Exception("General exception raised while attempting to add route: %s" % str(e))


def delete_route(base_url, cribl_auth_token, route_id, worker_group=None):
    try:
        current_routes = get_routes(base_url, cribl_auth_token, worker_group).json()
        route_idx = -1

        if "items" in current_routes and len(current_routes["items"]) != 0:
            current_route_config = current_routes["items"][0]
            index = 0
            for current_route in current_route_config["routes"]:
                if route_id == current_route["name"]:
                    route_idx = index
                    break
                index += 1
            if route_idx != -1:
                current_routes["items"][0]["routes"].pop(route_idx)
                try:
                    return _update_routes(base_url, cribl_auth_token,
                                          {"id": "default", "routes": current_routes["items"][0]["routes"]},
                                          worker_group=worker_group)
                except Exception:
                    raise
            else:
                raise Exception("Route %s does not exist." % route_id)
    except Exception as e:
        raise Exception("General exception raised while attempting to delete route: %s" % str(e))


def _update_routes(base_url, cribl_auth_token, config, worker_group=None):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config
    try:
        if worker_group is not None:
            return patch(base_url + "/m/" + worker_group + "/routes/" + worker_group, headers=headers, payload=payload)
        else:
            return patch(base_url + "/routes/default", headers=headers, payload=payload)

    except Exception as e:
        raise Exception("General exception raised while attempting to add routes to Cribl: %s" % str(e))
