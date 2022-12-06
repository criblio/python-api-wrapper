from .output_operations import create_output, update_output, delete_output
from ..lib.data_validation import validate_payload
import inflection

source_type = "webhook"

all_fields = {
    "id": str,
    "type": str,
    "pipeline": str,
    "systemFields": list,
    "environment": str,
    "streamtags": list,
    "url": str,
    "method": str,
    "format": str,
    "concurrency": int,
    "maxPayloadSizeKB": int,
    "maxPayloadEvents": int,
    "compress": bool,
    "rejectUnauthorized": bool,
    "timeoutSec": int,
    "flushPeriodSec": int,
    "extraHttpHeaders": list,  # of objects
    "useRoundRobinDns": bool,
    "failedRequestLoggingMode": str,
    "safeHeaders": list,
    "onBackpressure": str,
    "authType": str,
    "customSourceExpression": str,
    "customDropWhenNull": bool,
    "customEventDelimiter": str,
    "customContentType": str,
    "pqMaxFileSize": str,
    "pqMaxSize": str,
    "pqPath": str,
    "pqCompress": str,
    "pqOnBackpressure": str,
    "pqControls": dict,  # undocumented
    "username": str,
    "password": str,
    "token": str,
    "credentialsSecret": str,
    "textSecret": str
}

required_fields = ["id", "type", "url"]


def create_webhook_destination(base_url, cribl_auth_token, source_id, url,
                               pipeline=None,
                               system_fields=None,
                               environment=None,
                               streamtags=None,
                               method="POST",
                               format="ndjson",
                               concurrency=5,
                               max_payload_size_kb=4096,
                               max_payload_events=0,
                               compress=False,
                               reject_unauthorized=False,
                               timeout_sec=30,
                               flush_period_sec=1,
                               extra_http_headers=None,
                               use_round_robin_dns=False,
                               failed_request_logging_mode="none",
                               safe_headers=None,
                               on_backpressure="block",
                               auth_type="none",
                               custom_source_expression="__httpOut",
                               custom_drop_when_null=False,
                               custom_event_delimiter="\n",
                               custom_content_type="application/x-ndjson",
                               pq_max_file_size="1 MB",
                               pq_max_size=None,
                               pq_path="$CRIBL_HOME/state/queues",
                               pq_compress="none",
                               pq_on_backpressure="block",
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


def update_webhook_destination(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
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


def delete_webhook_destination(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_output(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
