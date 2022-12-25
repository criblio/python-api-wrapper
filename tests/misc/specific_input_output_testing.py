import sys
import json

from cribl_python_api_wrapper.auth import *

from cribl_python_api_wrapper.inputs.kafka import *
from cribl_python_api_wrapper.inputs.http import *
from cribl_python_api_wrapper.inputs.elastic import *
from cribl_python_api_wrapper.inputs.splunk import *
from cribl_python_api_wrapper.inputs.splunksearch import *
from cribl_python_api_wrapper.inputs.splunkhec import *
from cribl_python_api_wrapper.inputs.azure_blob import *
from cribl_python_api_wrapper.inputs.confluent_cloud import *
from cribl_python_api_wrapper.inputs.grafana import *
from cribl_python_api_wrapper.inputs.windows_event_logs import *
from cribl_python_api_wrapper.inputs.windows_event_forwarder import *
from cribl_python_api_wrapper.inputs.tcp import *
from cribl_python_api_wrapper.inputs.s3 import *

from cribl_python_api_wrapper.outputs.syslog import *
from cribl_python_api_wrapper.outputs.s3 import *
from cribl_python_api_wrapper.outputs.splunk import *
from cribl_python_api_wrapper.outputs.splunk_lb import *
from cribl_python_api_wrapper.outputs.splunk_hec import *
from cribl_python_api_wrapper.outputs.output_router import *
from cribl_python_api_wrapper.outputs.webhook import *
from cribl_python_api_wrapper.outputs.sqs import *


def read_config(filename):
    file = open(filename, "r")
    json_data = json.load(file)

    if "worker_group" in json_data:
        return json_data["base_url"], json_data["username"], json_data["password"], json_data["worker_group"]
    else:
        return json_data["base_url"], json_data["username"], json_data["password"], None


def test_specific_inputs_outputs_crud():
    response = create_http_source(base_url=base_url, cribl_auth_token=cribl_auth_token, source_id="my_http_source",
                                  host="localhost", port=18000,
                                  disabled=False, worker_group=worker_group)
    print("create response: %s " % response.text)

    update_data = {
        "host": "nuc-ubuntu",
        "port": 12345,
        "disabled": False,
    }
    response = update_http_source(base_url=base_url, cribl_auth_token=cribl_auth_token, source_id="my_http_source",
                                  update_data=update_data,
                                  worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_http_source(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                  source_id="my_http_source", worker_group=worker_group)
    print("response: %s " % response.text)

    response = create_kafka_source(base_url, cribl_auth_token, "kafka_source",
                                   brokers=["localhost:9092"],
                                   topics=["my topic"],
                                   worker_group=worker_group)
    print("response: %s " % response.text)

    update_data = {
        "brokers": [
            "localhost:9092",
            "localhost:9093",
            "localhost:9094"
        ],
        "topics": [
            "topic1", "topic2", "topic3"
        ],
        "fromBeginning": False,
        "connectionTimeout": 30000
    }
    response = update_kafka_source(base_url, cribl_auth_token, "kafka_source", update_data,
                                   worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_kafka_source(base_url, cribl_auth_token, "kafka_source", worker_group=worker_group)
    print("response: %s " % response.text)

    response = create_elastic_source(base_url, cribl_auth_token, "elastic_source",
                                     host="localhost",
                                     port=20010,
                                     worker_group=worker_group)
    print("response: %s " % response.text)

    update_data = {
        "host": "localhost",
        "port": 20010,
        "maxActiveReq": 128,
        "elasticAPI": "/elasticAPI",
        "apiVersion": "8.3.2"
    }

    response = update_elastic_source(base_url, cribl_auth_token, "elastic_source", update_data,
                                     worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_elastic_source(base_url, cribl_auth_token, "elastic_source", worker_group=worker_group)
    print("response: %s " % response.text)

    response = create_splunk_source(base_url, cribl_auth_token, "splunk_source", host="localhost", port=20010,
                                    worker_group=worker_group)
    print("response: %s " % response.text)

    update_data = {
        "host": "localhost",
        "port": 20020,
        "staleChannelFlushMs": 20000,
        "maxActiveCxn": 20
    }

    response = update_splunk_source(base_url, cribl_auth_token, "splunk_source", update_data,
                                    worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_splunk_source(base_url, cribl_auth_token, "splunk_source", worker_group=worker_group)
    print("delete response: %s " % response.text)

    response = create_splunksearch_source(base_url, cribl_auth_token, "splunksearch_source",
                                          search_head="https://localhost:8089",
                                          search="index=myAppLogs",
                                          cron_schedule="*/15 * * * *",
                                          endpoint="/services/search/jobs/export",
                                          output_mode="json",
                                          worker_group=worker_group)
    print("create response: %s " % response.text)

    update_data = {
        "searchHead": "https://192.168.1.100:8089",
        "search": "index=apptraffic",
        "cronSchedule": "*/15 * * * *",
        "endpoint": "/services/search/jobs/export",
        "outputMode": "json"
    }
    response = update_splunksearch_source(base_url, cribl_auth_token, "splunksearch_source", update_data,
                                          worker_group=worker_group)
    print("update response: %s " % response.text)

    response = delete_splunksearch_source(base_url, cribl_auth_token, "splunksearch_source",
                                          worker_group=worker_group)
    print("delete response: %s " % response.text)

    response = create_splunkhec_source(base_url, cribl_auth_token, "splunk_hec_source", host="localhost",
                                       port=22002, splunk_hec_api="/services/collector", worker_group=worker_group)
    print("create response: %s " % response.text)

    update_data = {
        "host": "localhost",
        "port": 22200,
        "splunkHecAPI": "/services/collector2"
    }

    response = update_splunkhec_source(base_url, cribl_auth_token, "splunk_hec_source", update_data,
                                       worker_group=worker_group)
    print("update response: %s " % response.text)

    response = delete_splunkhec_source(base_url, cribl_auth_token, "splunk_hec_source", worker_group=worker_group)
    print("delete response: %s " % response.text)

    response = create_azure_blob_source(base_url, cribl_auth_token, "azure_blob_source", "myQueue",
                                        "myConnectString",
                                        worker_group=worker_group)
    print("create response: %s " % response.text)

    update_data = {
        "staleChannelFlushMs": 20000,
        "queueName": "myQueue",
        "connectionString": "myConnectString"
    }

    response = update_azure_blob_source(base_url, cribl_auth_token, "azure_blob_source", update_data,
                                        worker_group=worker_group)
    print("update response: %s " % response.text)

    response = delete_azure_blob_source(base_url, cribl_auth_token, "azure_blob_source", worker_group=worker_group)
    print("delete response: %s " % response.text)

    response = create_confluent_cloud_source(base_url, cribl_auth_token, "confluent_cloud_source",
                                             brokers=["localhost:9092"],
                                             topics=["my topic"],
                                             worker_group=worker_group)
    print("response: %s " % response.text)

    update_data = {
        "brokers": [
            "localhost:9092",
            "localhost:9093",
            "localhost:9094"
        ],
        "topics": [
            "topic1", "topic2", "topic3"
        ],
        "fromBeginning": False,
        "connectionTimeout": 30000
    }
    response = update_confluent_cloud_source(base_url, cribl_auth_token, "confluent_cloud_source", update_data,
                                             worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_confluent_cloud_source(base_url, cribl_auth_token, "confluent_cloud_source",
                                             worker_group=worker_group)
    print("response: %s\n\n\n\n " % response.text)

    response = create_grafana_source(base_url, cribl_auth_token, "grafana_source", host="localhost", port=20010,
                                     prometheus_api="/api/prom/push", loki_api="/loki/api/v1/push",
                                     worker_group=worker_group)
    print("response: %s " % response.text)

    update_data = {
        "host": "localhost",
        "port": 20020,
        "requestTimeout": 5,
        "prometheusAPI": "/api/prom/push",
        "lokiAPI": "/loki/api/v1/push"
    }

    response = update_grafana_source(base_url, cribl_auth_token, "grafana_source", update_data,
                                     worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_grafana_source(base_url, cribl_auth_token, "grafana_source", worker_group=worker_group)
    print("delete response: %s " % response.text)

    response = create_windows_event_logs_source(base_url, cribl_auth_token, "wel_source",
                                                ["Application", "Security", "System"], worker_group=worker_group)
    print("response: %s " % response.text)

    update_data = {
        "logNames": ["Application", "Security"]
    }

    response = update_windows_event_logs_source(base_url, cribl_auth_token, "wel_source", update_data,
                                                worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_windows_event_logs_source(base_url, cribl_auth_token, "wel_source", worker_group=worker_group)
    print("response: %s " % response.text)

    subscription_data = [
        {"subscriptionName": "My subscription",
         "version": "1.0",
         "contentFormat": "Raw",
         "heartbeatInterval": 60,
         "batchTimeout": 60,
         "targets": ["*"]
         }
    ]

    tls_data = {
        "privKeyPath": "/path/to/key",
        "certPath": "/path/to/cert",
        "caPath": "/path/to/ca"
    }

    response = create_windows_event_forwarder_source(base_url, cribl_auth_token, source_id="wef_source",
                                                     host="localhost", port=5986,
                                                     tls=tls_data, subscriptions=subscription_data,
                                                     worker_group=worker_group)

    print("response: %s " % response.text)

    response = create_tcp_source(base_url, cribl_auth_token, "tcp_source", "localhost", 22010,
                                 worker_group=worker_group)
    print("response: %s " % response.text)

    update_data = {
        "host": "localhost",
        "port": 22011,
    }

    response = update_tcp_source(base_url, cribl_auth_token, "tcp_source", update_data, worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_tcp_source(base_url, cribl_auth_token, "tcp_source", worker_group=worker_group)
    print("response: %s " % response.text)

    response = create_s3_source(base_url, cribl_auth_token, "s3_source",
                                queue_name="https://hostname:9999/queueName", region="us-east-1",
                                worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_s3_source(base_url, cribl_auth_token=cribl_auth_token, source_id="s3_source",
                                worker_group=worker_group)
    print("response: %s " % response.text)

    response = create_syslog_destination(base_url, cribl_auth_token=cribl_auth_token, host="localhost", port=50314,
                                         source_id="syslog_dest",
                                         worker_group=worker_group)
    print("response: %s " % response.text)

    update_data = {
        "host": "localhost",
        "port": 50514
    }

    response = update_syslog_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                         update_data=update_data, source_id="syslog_dest",
                                         worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_syslog_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                         source_id="syslog_dest", worker_group=worker_group)
    print("response: %s " % response.text)

    response = create_s3_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                     source_id="s3_destination", bucket="myBucket",
                                     region="us-east-1",
                                     stage_path="/staging", dest_path="/destination",
                                     worker_group=worker_group)

    print("response: %s " % response.text)

    update_data = {
        "bucket": "myBucket",
        "region": "us-west-2",
        "stagePath": "/staging",
        "destPath": "/destination"
    }

    response = update_s3_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                     source_id="s3_destination",
                                     update_data=update_data, worker_group=worker_group)
    print("response: %s " % response.text)

    response = delete_s3_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                     source_id="s3_destination",
                                     worker_group=worker_group)
    print("response: %s " % response.text)

    response = create_splunk_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                         source_id="splunk_destination", host="splunk-srv", port=9997,
                                         worker_group=worker_group)
    print("\nresponse: %s " % response.text)

    update_data = {
        "host": "splunk-srv",
        "port": 9997,
        "connectionTimeout": 5000,
        "throttleRatePerSec": "1.0 MB"
    }

    response = update_splunk_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                         source_id="splunk_destination", update_data=update_data,
                                         worker_group=worker_group)
    print("\nresponse: %s " % response.text)

    response = delete_splunk_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                         source_id="splunk_destination", worker_group=worker_group)

    print("\nresponse: %s " % response.text)

    response = create_splunk_lb_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                            source_id="splunk_lb_destination",
                                            hosts=[{
                                                "host": "splunk-srv",
                                                "port": 9997,
                                            }],
                                            worker_group=worker_group)
    print("\nresponse: %s " % response.text)

    update_data = {
        "hosts": [
            {
                "host": "splunk-srv",
                "port": 9997
            },
            {
                "host": "splunk-srv",
                "port": 9998
            }
        ]
    }

    response = update_splunk_lb_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                            source_id="splunk_lb_destination",
                                            update_data=update_data,
                                            worker_group=worker_group)
    print("\nresponse: %s " % response.text)

    response = delete_splunk_lb_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                            source_id="splunk_lb_destination",
                                            worker_group=worker_group)
    print("\nresponse: %s " % response.text)

    response = create_splunk_hec_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                             source_id="splunk_hec_destination",
                                             url="http://localhost:8088/services/collector/event",
                                             token="myToken",
                                             worker_group=worker_group)

    print("\nresponse: %s " % json.loads(response.text))
    update_data = {
        "url": "http://localhost:8089/services/collector/event",
        "onBackpressure": "drop"
    }

    response = update_splunk_hec_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                             source_id="splunk_hec_destination", update_data=update_data,
                                             worker_group=worker_group)
    print("\nresponse: %s " % response.text)

    response = delete_splunk_hec_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                             source_id="splunk_hec_destination", worker_group=worker_group)

    rules = [{
        "filter": "true",
        "output": "devnull:devnull",
        "description": "route to devnull",
    }]

    response = create_output_router_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                                source_id="AcmeCO_output_router", rules=rules,
                                                worker_group=worker_group)

    response = create_webhook_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                          source_id="webhook_dst", url="http://localhost:10999",
                                          method="PUT", worker_group=worker_group)

    print("\nresponse: %s " % response.text)

    update_data = {
        "url": "http://localhost:10999",
        "method": "POST",
        "maxPayloadSizeKB": 8192
    }

    response = update_webhook_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                          source_id="webhook_dst", update_data=update_data,
                                          worker_group=worker_group)
    print("\nresponse: %s " % response.text)

    response = delete_webhook_destination(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                          source_id="webhook_dst", worker_group=worker_group)
    print("\nresponse: %s " % response.text)

    response = create_sqs_destination(base_url=base_url, cribl_auth_token=cribl_auth_token, source_id="sqs_dst",
                                      queue_name="https://host:port/myQueueName", queue_type="standard",
                                      worker_group=worker_group)
    print("\nresponse: %s " % response.text)
    update_data = {
        "queueName": "https://host:port/myQueueName",
        "queueType": "standard",
        "region": "us-east-1"
    }

    response = update_sqs_destination(base_url=base_url, cribl_auth_token=cribl_auth_token, source_id="sqs_dst",
                                      update_data=update_data, worker_group=worker_group)
    print("\nresponse: %s " % response.text)

    response = delete_sqs_destination(base_url=base_url, cribl_auth_token=cribl_auth_token, source_id="sqs_dst",
                                      worker_group=worker_group)
    print("\nresponse: %s " % response.text)


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(f'Usage: %s --config-file <filename>' % sys.argv[0])
        exit()

    base_url, username, password, worker_group = read_config(filename=sys.argv[2])

    cribl_auth_token = None
    try:
        cribl_auth_token = api_get_auth_token(
            base_url=base_url, username=username, password=password)
        collectors = None
    except:
        print(f"Could not retrieve bearer cribl_auth_token. Exiting.")
        exit()
