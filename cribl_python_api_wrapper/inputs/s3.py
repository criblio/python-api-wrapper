from .input_operations import create_input, update_input, delete_input
from cribl_python_api_wrapper.lib.data_validation import validate_payload
import inflection

source_type = "s3"

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
    "queueName": str,
    "fileFilter": str,
    "awsAccountId": str,
    "awsAuthenticationMethod": str,
    "awsSecretKey": str,
    "region": str,
    "endpoint": str,
    "signatureVersion": str,
    "reuseConnections": bool,
    "rejectUnauthorized": bool,
    "breakerRulesets": list,
    "staleChannelFlushMs": int,
    "maxMessages": int,
    "visibilityTimeout": int,
    "numReceivers": int,
    "socketTimeout": int,
    "skipOnError": bool,
    "enableAssumeRole": bool,
    "assumeRoleArn": str,
    "assumeRoleExternalId": str,
    "enableSQSAssumeRole": bool,
    "preprocess": dict,
    "metadata": list,
    "parquetChunkDownloadTimeout": int,
    "pollTimeout": int,
    "awsApiKey": str,
    "awsSecret": str
}

required_fields = ["id", "type", "queueName"]


def create_s3_source(base_url, cribl_auth_token, source_id, queue_name, region, disabled=False,
                     pipeline=None,
                     send_to_routes=True,
                     persistent_queue_enabled=False,
                     streamtags=None,
                     environment=None,
                     connections=None,
                     pq=None,
                     file_filter=None,
                     aws_account_id=None,
                     aws_secret_key=None,
                     endpoint=None,
                     signature_version="v4",
                     reuse_connections=True,
                     reject_unauthorized=True,
                     breaker_rulesets=None,
                     max_messages=1,
                     visibility_timeout=600,
                     num_receivers=1,
                     socket_timeout=300,
                     skip_on_error=False,
                     enable_assume_role=False,
                     assume_role_arn=None,
                     assume_role_external_id=None,
                     enable_sqs_assume_role=False,
                     preprocess=None,
                     metadata=None,
                     parquet_chunk_size_mb=5,
                     parquet_chunk_download_timeout=600,
                     poll_timeout=1,
                     aws_api_key=None,
                     aws_secret=None,
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
            return create_input(base_url, cribl_auth_token, payload, worker_group)

    except:
        raise


def update_s3_source(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
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


def delete_s3_source(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_input(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
