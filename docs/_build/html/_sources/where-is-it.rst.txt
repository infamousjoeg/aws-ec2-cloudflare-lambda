###############
🌎 Where Is It?
###############

I released my AWS Lambda function under 
[main.py](https://github.com/infamousjoeg/aws-ec2-cloudflare-lambda/blob/master/main.py).  It invokes  `main.handler` on 
trigger action -- therefore, you'll find in 
[main.py](https://github.com/infamousjoeg/aws-ec2-cloudflare-lambda/blob/master/main.py) a defined handler function that 
contains the actions to take.

You can use the exported [AWS SAM template](https://docs.aws.amazon.com/lambda/latest/dg/serverless_app.html) to 
orchestrate setting up your AWS Lambda function using the same Python script.  Just don't forget to populate values into 
your Environment Variables before enabling the CloudWatch Event trigger!

![How to Deploy SAM 
Template](https://github.com/infamousjoeg/joeco.de/blob/gh-pages/assets/images/Messages%20Image(2549426905).png?raw=true)

![CloudFormation Success 
Screenshot](https://github.com/infamousjoeg/joeco.de/blob/gh-pages/assets/images/Messages%20Image(3292846589).png?raw=true)

![Lambda Function Created 
Automatically](https://github.com/infamousjoeg/joeco.de/blob/gh-pages/assets/images/Messages%20Image(2459700380).png?raw=true)

## 📦 Release

You may download the latest SAM template release from the [GitHub project 
page](https://github.com/infamousjoeg/aws-ec2-cloudflare-lambda/releases).
