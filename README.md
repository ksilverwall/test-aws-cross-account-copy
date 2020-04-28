Testing Cross Account Copy
---

## 1. Set Environment Variables

```
SRC_CFN_PROFILE
SRC_ACCOUNT_ID
SRC_PACKAGE_BUCKET_NAME
DST_CFN_PROFILE
DST_ACCOUNT_ID
DST_PACKAGE_BUCKET_NAME
DST_BUCKET_NAME
```


## 2. Create Dst Resources

```
sam package \
  --profile ${DST_CFN_PROFILE} \
  --template-file ./sam-dst.yml \
  --output-template-file ./packaged-dst.yml \
  --s3-bucket ${DST_PACKAGE_BUCKET_NAME}

sam deploy \
  --profile ${DST_CFN_PROFILE} \
  --stack-name test-transfer-dst \
  --template-file ./packaged-dst.yml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    DstBucketName=${DST_BUCKET_NAME} \
    ExternalAccountId=${SRC_ACCOUNT_ID}
```

## 3. Note Kms Arn

```
DST_KMS_ARN
```

## 4. Create Src Resources

```
sam package \
  --profile ${SRC_CFN_PROFILE} \
  --template-file ./sam-src.yml \
  --output-template-file ./packaged-src.yml \
  --s3-bucket ${SRC_PACKAGE_BUCKET_NAME}

sam deploy \
  --profile ${SRC_CFN_PROFILE} \
  --stack-name test-transfer-src \
  --template-file ./packaged-src.yml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    DstBucketName=${DST_BUCKET_NAME} \
    KmsArn=${DST_KMS_ARN}
```

