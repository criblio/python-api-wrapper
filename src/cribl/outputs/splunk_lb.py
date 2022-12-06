from .output_operations import create_output, update_output, delete_output
from ..lib.data_validation import validate_payload
import inflection

source_type = "splunk_lb"

all_fields = {
    "id": str,
    "type": str,
    "pipeline": str,
    "systemFields": list,
    "environment": str,
    "streamtags": list,
    "dnsResolvePeriodSec": int,
    "loadBalanceStatsPeriodSec": int,
    "maxConcurrentSenders": int,
    "nestedFields": str,
    "throttleRatePerSec": str,
    "onBackpressure": str,
    "indexerDiscovery": bool,
    "tls": dict,
    "connectionTimeout": int,
    "writeTimeout": int,
    "enableMultiMetrics": bool,
    "enableACK": bool,
    "authType": str,
    "indexerDiscoveryConfigs": dict,
    "excludeSelf": bool,
    "hosts": list,  # of destination objects
    "pqMaxFileSize": str,
    "pqMaxSize": str,
    "pqPath": str,
    "pqCompress": str,
    "pqOnBackpressure": str,
    "authToken": str,
    "textSecret": str,
    "pqControls": str  # undocumented
}

required_fields = ["id", "type", "hosts"]


def create_splunk_lb_destination(base_url, cribl_auth_token, source_id, hosts,
                                 pipeline=None,
                                 system_fields=None,
                                 environment=None,
                                 streamtags=None,
                                 dns_resolve_period_sec=600,
                                 load_balance_stats_period_sec=300,
                                 max_concurrent_senders=0,
                                 nested_fields="none",
                                 throttle_rate_per_sec="0",
                                 on_backpressure="block",
                                 indexer_discovery=False,
                                 tls=None,
                                 connection_timeout=10000,
                                 write_timeout=60000,
                                 enable_multi_metrics=False,
                                 enable_ack=True,
                                 pq_max_file_size="1 MB",
                                 pq_max_size=None,
                                 pq_path="$CRIBL_HOME/state/queues",
                                 pq_compress="none",
                                 pq_on_backpressure="block",
                                 auth_token=None,
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


def update_splunk_lb_destination(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
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


def delete_splunk_lb_destination(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_output(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
