# AWS EC2 to Cloudflare Lambda Function

[This is the initial working release.](https://github.com/infamousjoeg/aws-ec2-cloudflare-lambda/releases/tag/v1.0)

## How To Use

1. Upload [release/deployment.zip](release/deployment.zip) to your created AWS Lambda function.
2. Create an event trigger for the AWS Lambda function.
3. Make sure the IAM Execution Role has "EC2ReadOnlyAccess" to read the public IPv4 address set.
4. Populate values in the AWS Lambda function for all environment variables used in `main.py`.

## Blog Post

[https://joeco.de/serverless/automating-cloudflare-dns-record-updates-with-aws-lambda-python/](https://joeco.de/serverless/automating-cloudflare-dns-record-updates-with-aws-lambda-python/)

## Template

You can find a SAM Template example at [release/AWSEC2CloudflareLambda.yaml](release/AWSEC2CloudflareLambda.yaml)

## License

MIT
