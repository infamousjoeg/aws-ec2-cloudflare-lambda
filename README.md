# AWS EC2 to Cloudflare Lambda Function

This is the initial working release.

## How To Use

1. Upload deployment.zip to your created AWS Lambda function.
2. Create an event trigger for the AWS Lambda function.
3. Make sure the IAM Execution Role has "EC2ReadOnlyAccess" to read the public IPv4 address set.
4. Populate values in the AWS Lambda function for all environment variables used in `main.py`.

## License

MIT
