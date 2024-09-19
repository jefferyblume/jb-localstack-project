import boto3
import time
import pytest

@pytest.fixture
def aws_clients():
    # Use 'localhost:4566' as the endpoint URL
    s3 = boto3.client('s3', endpoint_url='http://localhost:4566')
    logs = boto3.client('logs', endpoint_url='http://localhost:4566')
    return s3, logs

def test_s3_to_lambda_trigger(aws_clients):
    s3_client, logs_client = aws_clients

    bucket_name = 'my-test-bucket'
    test_file_key = 'test_file.txt'
    log_group_name = '/aws/lambda/s3-event-handler'

    # Upload a test file to S3
    s3_client.put_object(Bucket=bucket_name, Key=test_file_key, Body='Hello, World!')

    # Wait for the Lambda function to process the event
    time.sleep(5)

    # Retrieve logs
    log_streams_response = logs_client.describe_log_streams(logGroupName=log_group_name)
    log_streams = log_streams_response.get('logStreams', [])
    assert log_streams, "No log streams found. Lambda function did not execute."

    # Get the latest log stream
    latest_stream = max(log_streams, key=lambda x: x['creationTime'])
    log_stream_name = latest_stream['logStreamName']

    # Get log events from the log stream
    log_events_response = logs_client.get_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name
    )
    log_events = log_events_response.get('events', [])
    messages = [event['message'] for event in log_events]

    # Check if the Lambda function processed the event
    event_received = any('Event Received:' in msg for msg in messages)
    assert event_received, "Lambda function did not process the event."

    # Clean up
    s3_client.delete_object(Bucket=bucket_name, Key=test_file_key)
