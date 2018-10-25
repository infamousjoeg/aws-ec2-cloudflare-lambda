#########################
🤖 My Engineered Solution
#########################

* First and foremost, it should be open sourced on GitHub.

  * <https://github.com/infamousjoeg/aws-ec2-cloudflare-lambda>
  * Language should be [Python](https://www.python.org/). _(My most comfortable language currently.)_

* Any custom functions should be put in a [Python module package](https://docs.python.org/2/tutorial/modules.html) format 
for easy distribution later.

* The AWS Lambda function's [execution 
role](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role) should have 
the following permissions:

  * [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
  * [SNS](https://aws.amazon.com/sns/) (_Publish_)
  * EC2 (_EC2ReadOnlyAccess_ IAM Role)

* The _Instance State_ change should be a [CloudWatch Event 
trigger](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html) in the function.

* The function should be universally adoptable.  It should make the following variables available to the Python script as 
Environment Variables:

  * `EC2_INSTANCE_NAME`
  * `CLOUDFLARE_EMAIL`
  * `CLOUDFLARE_API_KEY`
  * `CLOUDFLARE_A_NAME`
  * `CLOUDFLARE_DNS_ID`
  * `CLOUDFLARE_ZONE_ID`

* The function should use the [AWS SDK](https://aws.amazon.com/sdk-for-python/) to describe the EC2 instance provided and 
retrieve the public IPv4 address assigned.

* The function should use [Cloudflare's RESTful API](https://api.cloudflare.com/) to update the specified A record in the 
DNS & Zone given using the E-Mail and API Key provided for authentication to do so.  Updating it to the previously 
retrieved public IPv4 address.
