import boto3


def upload(filename, bucket):
    client = boto3.client('s3')
    with open(filename, "rb") as f:
        client.upload_fileobj(f, bucket, filename)


upload("data.csv", "hohlokidbucket")
upload("plot.png", "hohlokidbucket")
