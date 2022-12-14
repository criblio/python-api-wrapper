from .output_operations import create_output, update_output, delete_output
from cribl.lib.data_validation import validate_payload
import inflection

source_type = "splunk_hec"

all_fields = {
    "id": str,
    "type": str,
    "pipeline": str,
    "systemFields": list,
    "environment": str,
    "streamtags": list,
    "loadBalanced": bool,
    "nextQueue": str,
    "tcpRouting": str,
    "concurrency": int,
    "maxPayloadSizeKB": int,
    "maxPayloadEvents": int,
    "compress": bool,
    "rejectUnauthorized": bool,
    "timeoutSec": int,
    "flushPeriodSec": int,
    "extraHttpHeaders": list,
    "failedRequestLoggingMode": str,
    "safeHeaders": list,
    "enableMultiMetrics": bool,
    "authType": str,
    "onBackpressure": str,
    "url": str,
    "useRoundRobinDns": bool,
    "excludeSelf": bool,
    "urls": list,  # of objects
    "dnsResolvePeriodSec": int,
    "loadBalanceStatsPeriodSec": int,
    "token": str,
    "textSecret": str,
    "pqMaxFileSize": str,
    "pqMaxSize": str,
    "pqPath": str,
    "pqCompress": str,
    "pqOnBackpressure": str,
    "pqControls": str  # undocumented
}

required_fields = ["id", "type", "url"]


def create_splunk_hec_destination(base_url, cribl_auth_token, source_id, url,
                                  pipeline=None,
                                  system_fields=None,
                                  environment=None,
                                  streamtags=None,
                                  load_balanced=False,
                                  next_queue="indexQueue",
                                  tcp_routing="nowhere",
                                  concurrency=5,
                                  max_payload_size_kb=4096,
                                  max_payload_events=0,
                                  compress=False,
                                  reject_unauthorized=False,
                                  timeout_sec=30,
                                  flush_period_sec=1,
                                  extra_http_headers=None,
                                  failed_request_logging_mode="none",
                                  safe_headers=None,
                                  enable_multi_metrics=False,
                                  auth_type="manual",
                                  on_backpressure="block",
                                  urls=None,
                                  dns_resolve_period_sec=600,
                                  load_balance_stats_period_sec=300,
                                  token=None,
                                  text_secret=None,
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


def update_splunk_hec_destination(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
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


def delete_splunk_hec_destination(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_output(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
