import os
import boto3
import re


def get_logger():
    from logging import getLogger, INFO

    log = getLogger()
    log.setLevel(INFO)

    return log


def run(logger):
    s3 = boto3.client('s3')

    dst_bucket = os.getenv('DestinationBucketName')
    dst_prefix = os.getenv('DestinationPrefix')
    kms_arn = os.getenv('KmsArn')

    s3.put_object(
        Bucket=dst_bucket ,
        Key=os.path.join(dst_prefix, 'sample.txt'),
        Body="ABCDEFG".encode('utf-8'),
        ServerSideEncryption='aws:kms',
        SSEKMSKeyId=kms_arn,
    )

    zzz = s3.get_object(
        Bucket=dst_bucket ,
        Key=os.path.join(dst_prefix, 'sample.txt'),
    )

    logger.info(zzz['Body'].read())

    logger.info("complete!!")


def lambda_handler(event, context):
    logger = get_logger()
    try:
        logger.info('event: {}'.format(event))

        run(logger)

        return {'statusCode': 200}
    except Exception as e:
        logger.exception(e)
        return {'statusCode': 500}
