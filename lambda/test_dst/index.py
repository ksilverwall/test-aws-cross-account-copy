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

    src_bucket = os.getenv('SharedBucketName')

    zzz = s3.get_object(
        Bucket=src_bucket,
        Key=os.path.join('sources', 'sample.txt'),
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

