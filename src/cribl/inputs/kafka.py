from .input_operations import create_input, update_input, delete_input
from ..lib.data_validation import validate_payload
import inflection

source_type = "kafka"

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
    "brokers": list,
    "topics": list,
    "groupId": str,
    "fromBeginning": bool,
    "kafkaSchemaRegistry": dict,
    "connectionTimeout": int,
    "requestTimeout": int,
    "sasl": dict,
    "tls": dict,
    "sessionTimeout": int,
    "rebalanceTimeout": int,
    "heartbeatInterval": int,
    "autoCommitInterval": int,
    "autoCommitThreshold": int,
    "maxBytesPerPartition": int,
    "maxBytes": int,
    "metadata": list
}

required_fields = ["id", "type", "brokers", "topics"]


def create_kafka_source(base_url, cribl_auth_token, source_id, brokers, topics, disabled=False,
                        pipeline=None, send_to_routes=None, persistent_queue_enabled=False,
                        streamtags=None, environment=None, connections=None, pq=None,
                        group_id="Cribl",
                        from_beginning=True,
                        kafka_schema_registry=None,
                        connection_timeout=10000,
                        request_timeout=1000,
                        sasl=None, tls=None,
                        session_timeout=30000,
                        rebalance_timeout=60000,
                        heartbeat_interval=3000,
                        auto_commit_interval=1000,
                        max_bytes_per_partition=1048576,
                        max_bytes=10485760,
                        metadata=None, worker_group=None):
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


def update_kafka_source(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
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


def delete_kafka_source(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_input(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
