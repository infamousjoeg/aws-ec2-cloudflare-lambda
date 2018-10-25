#######################
📢 Use Case Explanation
#######################

I like to use a very specific domain name when I demo [CyberArk Conjur](https://conjur.org) because it's easier for me to 
remember and it also looks better to the customer.  Even so, if it doesn't look good to them -- it still looks better to 
me!

I noticed quickly that when I'd set the public IPv4 address of my [AWS](https://aws.amazon.com) 
[EC2](https://aws.amazon.com/ec2/) instance that I demo from to an A record for `cdemo.cybr.rocks` in 
[Cloudflare](https://cloudflare.com)'s DNS, it'd be good for that Instance running.  However, after I stopped the EC2 
instance and, eventually, restarted it again, it boots with a different public IPv4 address.

Now, I'm sure I could just use an [Elastic 
IP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) and assign it and call it a day... 
but that costs money -- even when it's not being used!  I can save money, even over the Elastic IP lease, triggering the 
[AWS Lambda](https://aws.amazon.com/lambda/) function only when my _Instance State_ changes.

Finally, to the use case: upon a defined Instance's _Instance State_ changing to "Running", grab the defined Instance's 
public IPv4 address and update a defined [A record](https://support.dnsimple.com/articles/a-record/) in Cloudflare's DNS.
