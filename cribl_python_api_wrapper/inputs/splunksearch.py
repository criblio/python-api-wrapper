from .input_operations import create_input, update_input, delete_input
from cribl_python_api_wrapper.lib.data_validation import validate_payload
import inflection

source_type = "splunk_search"

all_fields = {
    "id": str,
    "type": str,
    "disabled": bool,
    "pipeline": str,
    "sendToRoutes": bool,
    "environment": str,
    "pqEnabled": bool,
    "streamtags": list,
    "connections": list,
    "pq": dict,
    "searchHead": str,
    "search": str,
    "earliest": str,
    "latest": str,
    "cronSchedule": str,
    "endpoint": str,
    "outputMode": str,
    "endpointParams": list,
    "endpointHeaders": list,
    "logLevel": str,
    "requestTimeout": int,
    "useRoundRobinDns": bool,
    "keepAliveTime": int,
    "maxMissedKeepAlives": int,
    "metadata": list,
    "breakerRulesets": dict,
    "staleChannelFlushMs": int,
    "authType": str,
    "username": str,
    "password": str,
    "token": str,
    "credentialsSecret": str,
    "textSecret": str
}

required_fields = ["id", "type", "searchHead", "search", "cronSchedule", "endpoint", "outputMode"]


def create_splunksearch_source(base_url, cribl_auth_token, source_id, search_head, search, cron_schedule, endpoint,
                               output_mode, disabled=False,
                               pipeline=None,
                               send_to_routes=True,
                               persistent_queue_enabled=False,
                               streamtags=None,
                               environment=None,
                               connections=None,
                               pq=None,
                               earliest="-16m@m",
                               latest="-1m@m",
                               endpoint_params=None,
                               endpoint_headers=None,
                               log_level=None,
                               request_timeout=0,
                               use_round_robin_dns=False,
                               keep_alive_time=30,
                               max_missed_keep_alives=3,
                               metadata=None,
                               breaker_rulesets=None,
                               stale_channel_flush_ms=10000,
                               auth_type=None,
                               username=None,
                               password=None,
                               token=None,
                               credentials_secret=None,
                               text_secret=None,
                               worker_group=None
                               ):
    payload = {
        "id": source_id,
        "type": source_type
    }

    for field in all_fields.keys():
        cml_field = inflection.underscore(field)
        if cml_field in locals() and locals()[cml_field] is not None:
            payload[field] = locals()[cml_field]
    print("payload: %s" % payload)
    try:
        payload, missing_required_fields, incorrectly_formatted_fields = \
            validate_payload(payload, all_fields, required_fields)
        if len(missing_required_fields) != 0:
            raise Exception("Missing the following required fields for create: %s" % missing_required_fields)
        elif len(incorrectly_formatted_fields) != 0:
            raise Exception(
                "The following fields were incorrectly formatted. Check payload and try again: %s" %
                incorrectly_formatted_fields)
        else:
            return create_input(base_url, cribl_auth_token, payload, worker_group)

    except:
        raise


def update_splunksearch_source(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
    update_data["id"] = source_id
    update_data["type"] = source_type

    try:
        update_data, missing_required_fields, incorrectly_formatted_fields = \
            validate_payload(update_data, all_fields, required_fields)

        if len(missing_required_fields) != 0:
            raise Exception("Missing the following required fields for update: %s" % missing_required_fields)
        elif len(incorrectly_formatted_fields) != 0:
            raise Exception(
                "The following fields were incorrectly formatted. Check payload and try again: %s" %
                incorrectly_formatted_fields)
        else:
            return update_input(base_url, cribl_auth_token, source_id, update_data, worker_group)

    except:
        raise


def delete_splunksearch_source(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_input(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
