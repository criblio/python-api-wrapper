import time

from cribl_python_api_wrapper.inputs import *

sleep_time = 3  # seconds


def inputs_testing(base_url, cribl_auth_token, worker_group=None):
    print(f'Testing get_inputs()...')
    response = get_inputs(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
    print(f"Response: %s" % response.json())

    print(f'\n\n\nTesting get_input_by_id()...')
    response = get_input_by_id(base_url=base_url, cribl_auth_token=cribl_auth_token,
                               input_id="in_syslog", worker_group=worker_group)
    print(f"Response: %s" % response.json())

    print(f'\n\n\nTesting get_input_statuses()...')
    response = get_input_statuses(base_url, cribl_auth_token, worker_group)
    print(f'Response: %s' % response.json())

    print(f'\n\n\nTesting get_input_status_by_id()...')
    response = get_input_status_by_id(base_url, cribl_auth_token, "in_syslog", worker_group)
    print(f'input_status: %s' % response.json())

    print(f'\n')

    # # Splunk
    test_inputs(base_url, cribl_auth_token, "in_splunk_si_api", "splunk", worker_group, {
        "host": "nuc-ubuntu",
        "port": 19777
    }, {
                    "host": "nuc-ubuntu",
                    "port": 19778
                })

    # # Splunk HEC
    # test_inputs(base_url, cribl_auth_token, "in_splunk_hec_api", "splunk_hec", worker_group, {
    #     "host": "nuc-ubuntu",
    #     "port": 19777,
    #     "splunkHecAPI": "/services/collector"
    # }, {
    #     "host": "nuc-ubuntu",
    #     "port": 19778,
    #     "splunkHecAPI": "/services/collector"
    # })

    # # test_inputs_hec(base_url, cribl_auth_token,
    # #                 "in_splunk_hec", "some token", worker_group)

    # # Splunk Search
    # test_inputs(base_url, cribl_auth_token, "in_splunk_search_api", "splunk_search", worker_group, {
    #     "searchHead": "https://localhost:8089",
    #     "search": "index=_internal",
    #     "cronSchedule": "*/15 * * * *",
    #     "endpoint": "/services/search/jobs/export",
    #     "outputMode": "json"
    # }, {
    #     "searchHead": "https://localhost:8089",
    #     "search": "host=*",
    #     "cronSchedule": "*/15 * * * *",
    #     "endpoint": "/services/search/jobs/export",
    #     "outputMode": "json"
    # })

    # # HTTP
    # test_inputs(base_url, cribl_auth_token, "in_http_api", "http", worker_group, {
    #     "host": "nuc-ubuntu",
    #     "port": 19777
    # }, {
    #                 "host": "nuc-ubuntu",
    #                 "port": 19778
    #             })

    # # Azure Blob
    # test_inputs(base_url, cribl_auth_token, "in_azure_blob_api", "azure_blob", worker_group, {
    #     "queueName": "queueA",
    #     "connectionString": "my connection string",
    #     "numReceivers": 2
    # }, {
    #     "queueName": "queueB",
    #     "connectionString": "my connection string",
    #     "numReceivers": 2
    # })

    # # ElasticSearch API
    # test_inputs(base_url, cribl_auth_token, "in_elastic_api", "elastic", worker_group, {
    #     "host": "nuc-ubuntu",
    #     "port": 19777,
    #     "elasticAPI": "/"
    # }, {
    #     "host": "nuc-ubuntu",
    #     "port": 19778,
    #     "elasticAPI": "/"
    # })

    # # Confluent Cloud
    # test_inputs(base_url, cribl_auth_token, "in_confluent_cloud_api", "confluent_cloud", worker_group, {
    #     "brokers": ["broker1", "broker2"],
    #     "topics": ["topic1", "topic2"]
    # }, {
    #     "brokers": ["broker3", "broker4"],
    #     "topics": ["topic3", "topic4"]
    # })

    # # Kafka
    # test_inputs(base_url, cribl_auth_token, "in_kafka_api", "kafka", worker_group, {
    #     "brokers": ["broker1", "broker2"],
    #     "topics": ["topic1", "topic2"]
    # }, {
    #     "brokers": ["broker3", "broker4"],
    #     "topics": ["topic3", "topic4"]
    # })

    # Grafana
    # test_inputs(base_url, cribl_auth_token, "in_grafana_api", "grafana", worker_group, {
    #     "host": "nuc-ubuntu",
    #     "port": 19777,
    #     "prometheusAPI": "/api/prom/push"
    # }, {
    #     "host": "nuc-ubuntu",
    #     "port": 19778,
    #     "prometheusAPI": "/api/prom/push"
    # })

    # Loki
    # test_inputs(base_url, cribl_auth_token, "in_loki_api", "loki", worker_group, {
    #     "host": "nuc-ubuntu",
    #     "port": 19777,
    #     "lokiAPI": "/loki/api/v1/push"
    # }, {
    #     "host": "nuc-ubuntu",
    #     "port": 19778,
    #     "lokiAPI": "/loki/api/v1/push"
    # })

    # Prometheus Remote Write
    # test_inputs(base_url, cribl_auth_token, "in_prometheus_rw_api", "prometheus_rw", worker_group, {
    #     "host": "nuc-ubuntu",
    #     "port": 19777,
    #     "prometheusAPI": "/api/prom/push"
    # }, {
    #     "host": "nuc-ubuntu",
    #     "port": 19778,
    #     "prometheusAPI": "/api/prom/push"
    # })

    # Prometheus
    # test_inputs(base_url, cribl_auth_token, "in_prometheus_api", "prometheus", worker_group, {
    #     "host": "nuc-ubuntu",
    #     "port": 19777,
    #     "discoveryType": "ec2",
    #     "interval": 60,
    #     "logLevel": "info",
    #     "targetList": ["http://localhost:9090/metrics"],
    #     "nameList": [{ "type": "string", "title": "DNS Names" }],
    #     "recordType": "SRV",
    #     "scrapeProtocol": "http",
    #     "scrapePath": "/metrics",
    #     "scrapePort": 64000

    # }, {
    #     "host": "nuc-ubuntu",
    #     "port": 19778,
    #     "discoveryType": "ec2",
    #     "interval": 60,
    #     "logLevel": "info",
    #     "targetList": ["http://localhost:9090/metrics"],
    #     "nameList": [{ "type": "string", "title": "DNS Names" }],
    #     "recordType": "SRV",
    #     "scrapeProtocol": "http",
    #     "scrapePath": "/metrics",
    #     "scrapePort": 64000
    # })

    # TODO revisit O365
    # Office365 Activity
    # test_inputs(base_url, cribl_auth_token, "in_office365_mgmt_api", "office365_mgmt", worker_group, {
    #     "tenantId": "tenant",
    #     "appId": "application",
    #     "planType": "dod",
    #     "authType": "manual",
    #     "clientSecret": "secret",
    #     "publisherIdentifier": "123",
    #     "metadata": [{"name": "name", "value": "value"}],
    #     "contentType": [{"contentType": "Active Directory", "description": "Poll interval minutes (1-60)", "interval": 15, "logLevel": "info", "enabled": "true"}]
    # }, {
    #     "tenantId": "tenant",
    #     "appId": "application",
    #     "planType": "dod",
    #     "authType": "manual",
    #     "clientSecret": "secret123",
    #     "publisherIdentifier": "123",
    #     "metadata": [{"name": "name", "value": "value"}],
    #     "contentType": [{"contentType": "Active Directory", "description": "Poll interval minutes (1-60)", "interval": 15, "logLevel": "info", "enabled": "true"}]
    # })

    # Eventhub
    # test_inputs(base_url, cribl_auth_token, "in_eventhub_api", "eventhub", worker_group, {
    #     "brokers": ["broker1", "broker2"],
    #     "topics": ["topic1", "topic2"]
    # }, {
    #     "brokers": ["broker3", "broker4"],
    #     "topics": ["topic3", "topic4"]
    # })

    # Exec
    # test_inputs(base_url, cribl_auth_token, "in_exec_api", "exec", worker_group, {
    #     "command": "ls -lrt"
    # }, {
    #     "command": "echo \"hello\""
    # })

    # Firehose
    # test_inputs(base_url, cribl_auth_token, "in_firehose_api", "firehose", worker_group, {
    #     "host": "nuc-ubuntu",
    #     "port": 19777
    # }, {
    #     "host": "nuc-ubuntu",
    #     "port": 19778
    # })

    # Google Pubsub
    # API can't process serviceAccountCredentials
    # test_inputs(base_url, cribl_auth_token, "in_google_pubsub_api", "google_pubsub", worker_group, {
    #     "topicName": "topic",
    #     "subscriptionName": "subscription",
    #     "googleAuthMethod": "manual",
    #     "serviceAccountCredentials": "{\"project_id\": \"project\", \"client_id\":\"account\", \"auth_uri\":\"auth\",\"token_uri\":\"token\",\"auth_provider_x509_cert_url\":\"auth\"}"
    # }, {
    #     "topicName": "topic1",
    #     "subscriptionName": "subscription1",
    #     "googleAuthMethod": "auto"
    # })

    # # Kinesis
    # test_inputs(base_url, cribl_auth_token, "in_kinesis_api", "kinesis", worker_group, {
    #     "streamName": "aStream",
    #     "region": "us-west-1"
    # }, {
    #     "streamName": "aStream",
    #     "region": "us-east-1"
    # })

    # S3
    # test_inputs(base_url, cribl_auth_token, "in_s3_api", "s3", worker_group, {
    #     "queueName": "aQueue",
    #     "region": "us-west-1"
    # }, {
    #     "queueName": "aQueue",
    #     "region": "us-east-1"
    # })


def test_inputs(base_url, cribl_auth_token, input_id, input_type, worker_group, create_attributes, update_attributes):
    print(f"Creating input " + input_id)
    create_attributes["id"] = input_id
    create_attributes["type"] = input_type
    response = create_input(base_url=base_url, cribl_auth_token=cribl_auth_token, create_config=create_attributes,
                            worker_group=worker_group)

    print(f'create input response: %s' % response.json())
    print(f"Sleeping - check UI for newly created input.\n")
    time.sleep(sleep_time)

    update_attributes["type"] = input_type
    print(f"Updating input " + input_id)
    response = update_input(base_url=base_url, cribl_auth_token=cribl_auth_token, input_id=input_id,
                            update_config=update_attributes, worker_group=worker_group)

    print(f"update input response: %s" % response.json())
    print(f"Sleeping - check input for update.\n")
    time.sleep(sleep_time)

    print(f"Deleting input " + input_id)
    response = delete_input(
        base_url=base_url, cribl_auth_token=cribl_auth_token, input_id=input_id, worker_group=worker_group)
    print(f"delete input response: %s" % response.json())

    print(f"\n")
