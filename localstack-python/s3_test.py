import boto3
from colorama import Fore, Style
import localstack_client.session as ls_boto3

from pprint import pprint

client = ls_boto3.client("s3")


def main():
    BUCKET_NAME = "bite-my-shiny-metal-ass"
    S3_OBJECT_KEY = "message"

    print(f"{Fore.GREEN} Creating my bucket{Style.RESET_ALL}")
    create_bucket(BUCKET_NAME)

    print()

    print(f"{Fore.GREEN}Listing all buckets{Style.RESET_ALL}")
    list_buckets()

    print()

    print(f"{Fore.GREEN}Uploading object to bucket{Style.RESET_ALL}")
    upload_object(f"localstack-python/{S3_OBJECT_KEY}.txt", BUCKET_NAME, S3_OBJECT_KEY)

    print()

    print(f"{Fore.GREEN}Listing objects in bucket{Style.RESET_ALL}")
    list_objects(BUCKET_NAME, S3_OBJECT_KEY)

    print(
        f"{Fore.YELLOW}You should check the localstack logs now dummy{Style.RESET_ALL}"
    )


def create_bucket(name):
    response = client.create_bucket(Bucket=name)
    pprint(response)


def list_buckets():
    response = client.list_buckets()
    pprint(response)


def upload_object(file_name, bucket_name, key):
    response = client.upload_file(Filename=file_name, Bucket=bucket_name, Key=key)
    pprint(response)


def list_objects(bucket_name, key):
    response = client.get_object(Bucket=bucket_name, Key=key)
    pprint(response)


if __name__ == "__main__":
    main()
