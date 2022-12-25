# Python API Wrapper Module

## Overview
The API wrapper module provides a developer with basic create/update/delete utilities for multiple areas of the Stream API. 
Additionally, many input/output-specific modules have been incorporated into this to help facilitate
easier creation of these items in a Stream deployment, such as S3 and Splunk sources and destinations. 


### Prerequisites
- Python 3.7 and above

- build module (e.g. `pip3 install build`) 

### General Structure
The distribution can be visualized as follows:
```
├── cribl_python_api_wrapper
│   ├── auth
│   ├── collectors
│   ├── event_breaker_rules
│   ├── executors
│   ├── functions
│   ├── groups
│   ├── inputs
│   ├── lib
│   ├── lookups
│   ├── outputs
│   ├── packs
│   ├── parsers
│   ├── pipelines
│   ├── preview
│   ├── routes
│   ├── system
│   ├── users
│   ├── utilities
│   └── versioning
└── tests
    ├── event_breaker_rules
    ├── functions
    ├── groups
    ├── inputs
    ├── lib
    ├── misc
    ├── outputs
    ├── packs
    ├── pipelines
    ├── preview
    ├── routes
    ├── system
    ├── users
    ├── utilities
    └── versioning
```

### Build
To build the API wrapper module, execute the following command - srcdir will contain the `pyproject.toml` file, which contains configuration for the build process:

`python3 -m build /path/to/srcdir`

This will create two files:

- `cribl_python_api_wrapper-1.1.0-py3-none-any.whl`

- `cribl_python_api_wrapper-1.1.0.tar.gz`

The `.whl` file will be used for the installation which will be covered in the next section. 

### Installation
The wheel file can be installed via the following command (change the path as appropriate):

`python3 -m pip install /path/to/dist/cribl_python_api_wrapper-1.1.0-py3-none-any.whl --force-reinstall`

### Requests Library
The requests library (https://requests.readthedocs.io/en/latest/) is utilized by the API wrapper module for HTTP operations. 

### Use in Python Scripts
Before anything, the developer must retrieve an authorization token from the Cribl instance. The following values must be provided:
- base_url - the base URL of for the API, e.g. `http://<host>:<port>/api/v1`
- username - the user that will be making the API calls, e.g. admin
- password - the user's password

Once these are available to the script, the API token can be fetched as follows:
```
       from cribl_python_api_wrapper.auth import *
        
       response = api_get_auth_data(base_url=base_url, username=username, password=password)
        
       if response.json() and "token" in response.json():
            cribl_auth_token = response.json()["token"]

```
The "token" should be present in the response's JSON payload if the request is successful. This value should be saved and used in subsequent calls to the API.

#### Get/Create/Update/Delete of Configuration Items
The configuration items from the above list follow a get/create/update/delete
pattern. Using `inputs` as an example, the following methods are available:

- `get_inputs(base_url, cribl_auth_token, worker_group=None)`

- `get_input_by_id(base_url, cribl_auth_token, input_id, worker_group=None)`

- `create_input(base_url, cribl_auth_token, create_config, worker_group=None)`

- `update_input(base_url, cribl_auth_token, input_id, update_config, worker_group=None)`

- `delete_input(base_url, cribl_auth_token, input_id, worker_group=None)`

#### Status information for Configuration Items
Status information can be retrieved from one or more inputs/outputs:

- `get_input_statuses(base_url, cribl_auth_token, worker_group=None)`

- `get_input_status_by_id(base_url, cribl_auth_token, input_name, worker_group=None)`

- `get_output_statuses(base_url, cribl_auth_token, worker_group=None)`

- `get_output_status_by_id(base_url, cribl_auth_token, output_name, worker_group=None)`

The response JSON will contain status (health and metrics) information for the input or output.

##### URL
In each of these methods, we pass the base URL, which is structured as `http://<host>:<port>/api/v1`. 
These methods will work out how to construct the full URL based on the endpoint being called.

##### Cribl Auth Token
`cribl_auth_token` must be passed with each request to the API. The method called will create the required HTTP headers and add
the bearer token to them.

##### Worker Group
If the Cribl deployment is single mode, the worker_group need not be passed to the method. 

If the Cribl deployment is distributed, the worker_group must be set to the name of the Worker Group in which the changes are 
to be made.

##### Return Values
Each method will return a Response (https://requests.readthedocs.io/en/latest/api/?highlight=Response#requests.Response) object. This will allow the caller access 
to the full contents of the API response - JSON payload, response code, headers, response text, etc.

When calling these methods, the JSON payload from the response can be accessed via the Response's json() method, for example:
```
    inputs = get_inputs(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
    print(f"Input (JSON body): %s" % json.dumps(inputs.json(), indent=4))
```

This will yield the following - a list called 'items', which contains a JSON object for each input configured for the worker group (truncated):
```
{
    "items": [
        {
            "id": "http",
            "disabled": true,
            "type": "http",
            "host": "0.0.0.0",
            "port": 10080,
            "elasticAPI": "/elastic",
            "criblAPI": "/cribl",
            "splunkHecAPI": "/services/collector",
            "status": {
                "health": "Green",
                "timestamp": 1669306686561,
                "metrics": {
                    "numRequests": 0,
                    "numPushed": 0,
                    "numHealth": 0,
                    "numErrors": 0,
                    "numDropped": 0,
                    "activeCxn": 0,
                    "openCxn": 0,
                    "closeCxn": 0,
                    "rejectCxn": 0,
                    "abortCxn": 0,
                    "numInProgress": 0
                }
            }
        },
        .
        .
        .
    ]
}
```

##### Payloads
Payloads sent to the API for create and update operations must be formatted in JSON and have the required parameters depending 
upon the item that being created. 

#### A Note on Route Operations
Handling routes through the API is a bit different from the other configuration items. In a Stream deployment, there is one route table with an ID of "default", which is just a list of route objects.
Creating a route is actually updating "default" route table by adding the route object to the list, so the HTTP method used is PATCH, and not POST. Similarly, deleting a route involves
updating the "default" route table by removing the route object from the list.

To make things easier, the API wrapper module provides the following methods to deal with the route table:

- `get_routes(base_url, cribl_auth_token, worker_group)`

- `get_routes_by_id(base_url, cribl_auth_token, route_id, worker_group)`

- `add_route(base_url, cribl_auth_token, route_config, position="start", worker_group=None)`

- `delete_route(base_url, cribl_auth_token, route_id, worker_group=None)`

The add/delete methods update the route table accordingly; the add_route option also allows the developer to specify whether to place the route
at the beginning or end of the list by exposing a `position` parameter. The value, a string, can be either:
- `start`

- `end`

If no position is specified, the route is added to the beginning of the list.

#### Specific input and output types

Where applicable, the API wrapper module offers helper functions to create/update/delete specific inputs and outputs. This is done for the developer in order to avoid constructing the entire 
JSON payload when creating one of these components.

An example of the create/update/delete cycle for an HTTP source input can be depicted as follows:
```
        from cribl_python_api_wrapper.inputs.http import *
        
        response = create_http_source(base_url=base_url, cribl_auth_token=cribl_auth_token, 
                                      source_id="my_http_source",
                                      host="localhost", 
                                      port=18000,
                                      disabled=False,
                                      enable_proxy_header=False
                                      worker_group=worker_group)
        print(f"create response: %s " % response.text)

        update_data = {
            "host": "nuc-ubuntu",
            "port": 12345,
            "pqEnabled": True,
            "enableProxyHeader": True
        }
        response = update_http_source(base_url=base_url, cribl_auth_token=cribl_auth_token, source_id="my_http_source",
                                      update_data=update_data,
                                      worker_group=worker_group)
        print(f"update response: %s " % response.text)

        response = delete_http_source(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                      source_id="my_http_source", worker_group=worker_group)
        print(f"delete response: %s " % response.text)
```

#### Expert Mode
Any area of the API may be called via the API wrapper module using the generic methods in lib/http_operations.py:

- `get(url, headers, payload)`

- `post(url, headers, payload)`

- `put(url, headers, data)`

- `patch(url, headers, payload)`

- `delete(url, headers)`

You must explicitly work out the URL to call, construct the headers appropriately, and pass the correct payload 
(or no payload, if not required by the HTTP method in use). The API documentation should be followed when using these
methods.

#### Notes
- Each function must have the base_url and cribl_auth token passed to it. In distributed deployments, the worker group name must be passed to most functions (besides system-wide items such as versioning, system, etc) as shown above.
- Parameters in API wrapper module functions, such as `enable_proxy_header` in the create function, follow snake case. 
- Update functions require a parameter called `update_data`. This is a JSON object that contains the required fields (in this case, host and port) as well as other fields that the developer wishes to change. 
- Note that camel case is used for the field names in these updates in order to align with the API. See documentation at https://docs.cribl.io/api.
- In this example, `enable_proxy_header` in the `create_http_source` function corresponds to the `enableProxyHeader` field in the update data. 
- It is recommended to use an IDE such as PyCharm or VSCode to assist in development. Auto-complete/code completion should help provide guidance on how to call methods if not explicitly documented.

#### Supplemental API Documentation
Information on all aspects of the API can be found in the Cribl UI (Settings -> API Reference) or 
at https://docs.cribl.io/api/
- This can be referred to for more details on schemas, how to construct payloads when creating/updating configuration items, etc.