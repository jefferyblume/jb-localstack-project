#!/bin/bash

# Ensure the script exits on any error
set -e

# Create a test file to upload
echo "Hello, LocalStack!" > test_file.txt

# Upload the file to the S3 bucket
awslocal s3 cp test_file.txt s3://my-test-bucket/

# Wait for a few seconds to allow the Lambda function to process
sleep 5

# Delete the file from the S3 bucket
awslocal s3 rm s3://my-test-bucket/test_file.txt

# Wait again for the Lambda function
sleep 5

# Cleanup the test file
rm test_file.txt
