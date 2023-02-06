from .input_operations import create_input, update_input, delete_input
from cribl_python_api_wrapper.lib.data_validation import validate_payload
import inflection

source_type = "syslog"

# dict of all fields for this collector type. used for validation of payload.
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
    "host": str,
    "udpPort": int,
    "tcpPort": int,
    "maxBufferSize": int,
    "ipWhitelistRegex": str,
    "timestampTimezone": str,
    "singleMsgUdpPackets": bool,
    "enableProxyHeader": bool,
    "keepFieldsList": list,
    "octetCounting": bool,
    "allowNonStandardAppName": bool,
    "tls": dict,
    "metadata": list
}

required_fields = ["id", "type", "host"]


def create_syslog_source(base_url, cribl_auth_token, source_id, host, disabled=False,
                         pipeline=None, send_to_routes=True, persistent_queue_enabled=False,
                         streamtags=None, environment=None, connections=None, pq=None,
                         udp_port=10514,
                         tcp_port=10514,
                         max_buffer_size=1000,
                         ip_whitelist_regex="/.*/",
                         timestamp_timezone="local",
                         single_msg_udp_packets=False,
                         enable_proxy_header=False,
                         keep_fields_list=None,
                         octet_counting=False,
                         allow_non_standard_app_name=False,
                         tls=None,
                         metadata=None,
                         worker_group=None):
    payload = {
        "id": source_id,
        "type": source_type
    }

    for field in all_fields.keys():
        cml_field = inflection.underscore(field)
        if cml_field in locals() and locals()[cml_field] is not None:
            payload[field] = locals()[cml_field]
    try:
        payload, missing_required_fields, incorrectly_formatted_fields = \
            validate_payload(payload, all_fields, required_fields)
        if len(missing_required_fields) != 0:
            raise Exception("Missing the following required fields for update: %s" % missing_required_fields)
        elif len(incorrectly_formatted_fields) != 0:
            raise Exception(
                "The following fields were incorrectly formatted. Check payload and try again: %s" %
                incorrectly_formatted_fields)
        else:
            return create_input(base_url, cribl_auth_token, payload, worker_group)

    except:
        raise


def update_syslog_source(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
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


def delete_syslog_source(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_input(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
