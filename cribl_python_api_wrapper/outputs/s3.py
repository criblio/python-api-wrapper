from .output_operations import create_output, update_output, delete_output
from cribl_python_api_wrapper.lib.data_validation import validate_payload
import inflection

source_type = "s3"

all_fields = {
    "id": str,
    "type": str,
    "pipeline": str,
    "systemFields": list,
    "environment": str,
    "streamtags": list,
    "bucket": str,
    "region": str,
    "awsAuthenticationMethod": str,
    "awsSecretKey": str,
    "endpoint": str,
    "signatureVersion": str,
    "reuseConnections": bool,
    "rejectUnauthorized": bool,
    "enableAssumeRole": bool,
    "assumeRoleArn": str,
    "assumeRoleExternalId": str,
    "stagePath": str,
    "addIdToStagePath": bool,
    "removeEmptyDirs": bool,
    "destPath": str,
    "objectACL": str,
    "storageClass": str,
    "serverSideEncryption": str,
    "kmsKeyId": str,
    "partitionExpr": str,
    "format": str,
    "baseFileName": str,
    "fileNameSuffix": str,
    "maxFileSizeMB": int,
    "maxFileOpenTimeSec": int,
    "maxFileIdleTimeSec": int,
    "maxOpenFiles": int,
    "onBackpressure": str,
    "awsApiKey": str,
    "awsSecret": str,
    "compress": str,
    "parquetRowGroupSize": str,
    "parquetPageSize": str,
    "parquetVersion": str,
    "parquetDataPageVersion": str,
    "shouldLogInvalidRows": bool,
    "emptyDirCleanupSec": int
}

required_fields = ["id", "type", "bucket", "region", "stagePath", "destPath"]


def create_s3_destination(base_url, cribl_auth_token, source_id, bucket, region, stage_path, dest_path,
                          pipeline=None,
                          system_fields=None,
                          environment=None,
                          streamtags=None,
                          aws_authentication_method="auto",
                          aws_secret_key=None,
                          endpoint=None,
                          signature_version="v4",
                          reuse_connections=True,
                          reject_unauthoriazed=True,
                          enable_assume_role=False,
                          assume_role_arn=None,
                          add_id_to_stage_path=True,
                          remove_empty_dirs=False,
                          object_acl="private",
                          storage_class=None,
                          kms_key_id=None,
                          partition_expr="C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
                          format="json",
                          base_file_name="`CriblOut`",
                          file_name_suffix='`.${C.env["CRIBL_WORKER_ID"]}.${__format}${__compression === "gzip" ? ".gz" : ""}`',
                          max_file_size_mb=32,
                          max_file_idle_time_sec=30,
                          max_open_files=100,
                          on_backpressure="block",
                          aws_api_key=None,
                          aws_secret=None,
                          compress="none",
                          parquet_row_group_size="16 MB",
                          parquet_page_size="1MB",
                          parquet_version="PARQUET_2_6",
                          parquet_data_page_version="DATA_PAGE_V1",
                          should_log_invalid_rows=False,
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


def update_s3_destination(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
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


def delete_s3_destination(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_output(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
