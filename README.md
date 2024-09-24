## LocalStack S3 to Lambda Example

This project demonstrates how to use LocalStack to develop and test AWS infrastructure locally using Terraform. It sets up an S3 bucket and a Lambda function that is triggered by S3 bucket events (object creation and deletion).

## Prerequisites
Before you begin, ensure you have the following installed on your machine:

Docker: For containerization. Download Docker

AWS CLI: To interact with AWS services. Install AWS CLI

Terraform: For infrastructure-as-code. Download Terraform

Git: For version control. Download Git

Python 3.8: To write the Lambda function. Download Python

awslocal: AWS CLI wrapper for LocalStack. Install it using:

pip install awscli-local

## Project Structure

localstack-s3-lambda/

├── docker-compose.yml           # Configuration file to start LocalStack

├── lambda_function/             # Directory containing the Lambda function code

│   └── lambda_function.py       # Lambda function code

├── lambda_function.zip          # Zipped Lambda function ready for deployment

├── main.tf                      # Terraform configuration file defining AWS resources

├── README.md                    # Project documentation (this file)

├── run.sh                       # Script to interact with AWS resources using awslocal

└── logs/                        # Directory to store LocalStack debug logs

    └── localstack_debug.log     # LocalStack debug log


## Setup Instructions

1. Clone this repo and navigate to the proper directory.

git clone https://github.com/jefferyblume/jb-localstack-project.git

cd jb-localstack-project

2. Start LocalStack

docker-compose up -d

Verify it's running:

docker ps

You should see LocalStack in the container list.

3. Initialize Terraform

terraform init

4. Apply Terraform configuration

terraform apply -auto-approve

5. Install AWS local

pip install awscli-local

6. Run the interaction script

./run.sh

This script performs the following:

This script performs the following actions:

Creates a test file named test_file.txt.
Uploads the file to the S3 bucket (my-test-bucket).
Deletes the file from the S3 bucket.
Cleans up the test file from your local system.

7. Check localstack logs

docker logs localstack

Expected Behavior

When you run run.sh, the following should occur:

File Upload: The test file is uploaded to the S3 bucket, triggering the Lambda function.
Lambda Execution: The Lambda function executes and prints the event data to the logs.
File Deletion: The test file is deleted from the S3 bucket, again triggering the Lambda function.
Lambda Execution: The Lambda function executes a second time for the deletion event.

8. Cleanup

Get rid of AWS resources

terraform destroy -auto-approve

Stop LocalStack

docker-compose down

9. Common Issues

LocalStack Not Starting: Ensure Docker is running and no other services are using port 4566.

Lambda Function Not Triggered: Check IAM permissions and ensure the S3 bucket notification is correctly configured.

Errors in Terraform Apply: Double-check your Terraform configuration for typos or missing dependencies.
