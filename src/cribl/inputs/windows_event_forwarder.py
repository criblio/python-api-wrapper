from .input_operations import create_input, update_input, delete_input
from cribl.lib.data_validation import validate_payload
import inflection

source_type = "wef"

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
    "port": int,
    "tls": dict,
    "ipWhitelistRegex": str,
    "maxActiveReq": int,
    "enableProxyHeader": bool,
    "captureHeaders": bool,
    "caFingerprint": str,
    "allowMachineIdMismatch": bool,
    "subscriptions": list
}

subscription_fields = {
    "subscriptionName": str,
    "version": str,
    "contentFormat": str,
    "heartbeatInterval": int,
    "batchTimeout": int,
    "readExistingEvents": bool,
    "sendBookmarks": bool,
    "compress": bool,
    "targets": list,
    "querySelector": str
}

tls_fields = {
    "disabled": bool,
    "rejectUnauthorized": bool,
    "requestCert": bool,
    "certificateName": str,
    "privKeyPath": str,
    "passphrase": str,
    "certPath": str,
    "caPath": str,
    "commonNameRegex": str,
    "minVersion": str,
    "maxVersion": str

}

required_fields = ["id", "type", "host", "port", "tls", "subscriptions"]
required_tls_fields = ["privKeyPath", "caPath", "certPath"]
required_subscription_fields = ["subscriptionName", "contentFormat", "heartbeatInterval", "batchTimeout", "targets"]


def create_windows_event_forwarder_source(base_url, cribl_auth_token, source_id, host, port, tls, subscriptions,
                                          disabled=False,
                                          pipeline=None,
                                          send_to_routes=True,
                                          persistent_queue_enabled=False,
                                          streamtags=None,
                                          environment=None,
                                          connections=None,
                                          pq=None,
                                          max_active_req=256,
                                          enable_proxy_header=False,
                                          capture_headers=False,
                                          ca_fingerprint=None,
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
            raise Exception(f"Missing the following required fields for source creation: %s" % missing_required_fields)
        elif len(incorrectly_formatted_fields) != 0:
            raise Exception(
                f"The following fields were incorrectly formatted. Check payload and try again: %s" %
                incorrectly_formatted_fields)

        else:
            return create_input(base_url, cribl_auth_token, payload, worker_group)
            # validate required subscription field
            # payload["subscriptions"], missing_required_fields, incorrectly_formatted_fields = \
            #     validate_payload(payload["subscriptions"], subscription_fields, required_subscription_fields)
            # if len(missing_required_fields) != 0:
            #     raise Exception(
            #         f"Missing the following required fields for subscription payload: %s" % missing_required_fields)
            # elif len(incorrectly_formatted_fields) != 0:
            #     raise Exception(
            #         f"The following fields were incorrectly formatted for "
            #         "subscription payload. Check payload and try again: %s" %
            #         incorrectly_formatted_fields)
            # else:
            #     payload["tls"], missing_required_fields, incorrectly_formatted_fields = \
            #         validate_payload(payload["tls"], tls_fields, required_tls_fields)
            #
            #     if len(missing_required_fields) != 0:
            #         raise Exception(
            #             f"Missing the following required fields for tls payload: %s" % missing_required_fields)
            #     elif len(incorrectly_formatted_fields) != 0:
            #         raise Exception(
            #             f"The following fields were incorrectly formatted for "
            #             "tls payload. Check payload and try again: %s" %
            #             incorrectly_formatted_fields)
            #     else:

    except:
        raise


def update_windows_event_forwarder_source(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
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


def delete_windows_event_forwarder_source(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_input(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
