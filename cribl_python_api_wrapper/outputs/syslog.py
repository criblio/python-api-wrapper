from .output_operations import create_output, update_output, delete_output
from cribl_python_api_wrapper.lib.data_validation import validate_payload
import inflection

source_type = "syslog"

all_fields = {
    "id": str,
    "type": str,
    "pipeline": str,
    "systemFields": list,
    "environment": str,
    "streamtags": list,
    "protocol": str,
    "facility": int,
    "severity": int,
    "appName": str,
    "messageFormat": str,
    "timestampFormat": str,
    "throttleRatePerSec": str,
    "octetCountFraming": bool,
    "loadBalanced": bool,
    "connectionTimeout": int,
    "writeTimeout": int,
    "tls": dict,
    "onBackpressure": str,
    "host": str,
    "port": int,
    "maxRecordSize": int,
    "pqMaxSize": str,
    "pqPath": str,
    "pqCompress": str,
    "pqOnBackpressure": str,
    "pqControls": str  # undocumented
}

required_fields = ["id", "type", "host", "port"]


def create_syslog_destination(base_url, cribl_auth_token, source_id, host, port,
                              pipeline=None,
                              system_fields=None,
                              environment=None,
                              streamtags=None,
                              protocol="tcp",
                              facility=1,
                              severity=5,
                              app_name="Cribl",
                              message_format="rfc3164",
                              timestamp_format="syslog",
                              throttle_rate_per_sec="0",
                              octet_count_framing=False,
                              load_balanced=False,
                              connection_timeout=10000,
                              write_timeout=60000,
                              tls=None,
                              on_backpressure="block",
                              pq_max_file_size="1 MB",
                              pq_max_size=None,
                              pq_path="$CRIBL_HOME/state/queues",
                              pq_compress="none",
                              pq_on_backpressure="block",
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
            return create_output(base_url, cribl_auth_token, payload, worker_group)

    except:
        raise


def update_syslog_destination(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
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
            return update_output(base_url, cribl_auth_token, source_id, update_data, worker_group)

    except:
        raise


def delete_syslog_destination(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_output(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
