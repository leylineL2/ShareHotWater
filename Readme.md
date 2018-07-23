Share Hot Water
====

お湯を沸かす際にAWS エンタープライズボタン押してSlackに通知を飛ばすLambda

## Requirement

aws-cli/1.15.50 

## Instrall
```
git clone https://github.com/leylineL2/ShareHotWater
cd ShareHotWater
aws cloudformation package --template-file template.yml --output-template-file package.yml  --s3-bucket <UPLOAD_BUCKET_NAME> --profile <YOUR_PROFILE>
aws cloudformation deploy --template-file package.yml --stack-name <STACK_NAME> --capabilities CAPABILITY_IAM --profile <YOUR_PROFILE>
```
その後、AWS WebコンソールでAWS IoT 1-ClickでデプロイされたLambdaをプロジェクトで紐づける
