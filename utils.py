import boto3
import config


def create_boto_client(client_name):
    """
        create a boto client based on the cred
        provided in class initializaion
    """
    aws_access_key_id = config.aws_access_key_id
    aws_secret_access_key = config.aws_secret_access_key
    aws_region = config.aws_region

    client = boto3.client(
                        client_name,
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=aws_region
                        )
    
    return client