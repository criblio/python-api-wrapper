from .output_operations import create_output, update_output, delete_output
from cribl_python_api_wrapper.lib.data_validation import validate_payload
import inflection

source_type = "sqs"

all_fields = {
    "id": str,
    "type": str,
    "pipeline": str,
    "systemFields": list,
    "environment": str,
    "streamtags": list,
    "queueName": str,
    "queueType": str,
    "awsAccountId": str,
    "messageGroupId": str,
    "createQueue": bool,
    "awsAuthenticationMethod": str,
    "awsSecretKey": str,
    "region": str,
    "endpoint": str,
    "signatureVersion": str,
    "reuseConnections": bool,
    "rejectUnauthorized": bool,
    "enableAssumeRole": bool,
    "assumeRoleArn": str,
    "assumeRoleExternalId": str,
    "maxQueueSize": int,
    "maxRecordSizeKB": int,
    "flushPeriodSec": int,
    "maxInProgress": int,
    "onBackpressure": str,
    "awsApiKey": str,
    "awsSecret": str,
    "pqMaxFileSize": str,
    "pqMaxSize": str,
    "pqPath": str,
    "pqCompress": str,
    "pqOnBackpressure": str,
    "pqControls": dict  # undefined

}

required_fields = ["id", "type", "queueName", "queueType"]


def create_sqs_destination(base_url, cribl_auth_token, source_id, queue_name, queue_type,
                          pipeline=None,
                          system_fields=None,
                          environment=None,
                          streamtags=None,
                          aws_account_id=None,
                          message_group_id="cribl",
                          create_queue=True,
                          aws_authentication_method="auto",
                          aws_secret_key=None,
                          region=None,
                          endpoint=None,
                          signature_version="v4",
                          reuse_connections=True,
                          reject_unauthorized=True,
                          enable_assume_role=False,
                          assume_role_arn=None,
                          assume_role_external_id=None,
                          max_queue_size=100,
                          max_record_size_kb=256,
                          flush_period_sec=1,
                          max_in_progress=10,
                          on_backpressure="block",
                          aws_api_key=None,
                          aws_secret=None,
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


def update_sqs_destination(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
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


def delete_sqs_destination(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_output(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
