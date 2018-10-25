#####################
👟 "Step" Development
#####################

I made a name for this development method because I don't really know what it's called.  However, it's a process to 
development I found to be profoundly effective in a majority of my situations.  Those being where I'm a solo developer, 
tester, and releaser all wrapped into one.

The idea behind Step Development is rather easy -- take your decomposed "easily repeatable process" and script it one 
bullet point at a time.  Testing it one bullet point at a time.  While also, essentially, releasing it one bullet point at 
a time.

**✅ Step #1: Get the EC2 Instance's Public IPv4 Address**

The first bullet point in my decomposition is to grab the running EC2 instance's public IPv4 address once it is assigned 
fresh off a new run state.  I created and tested the function released in 
[pkg/func.py](https://github.com/infamousjoeg/aws-ec2-cloudflare-lambda/blob/master/pkg/func.py#L8) in my Terminal within 
MacOS.

**✅ Step #2: Authenticate to Cloudflare**

The second bullet point in my decomposition is to browse to Cloudflare, while my third is to login to Cloudflare.  Since 
this is automation, we'll kill two birds with one stone over the REST API.  Better yet, after investigating the 
[Cloudflare REST API Documentation](https://api.cloudflare.com/), it looks like we can authenticate _while_ also updating 
the A record.  

SCORE!  Nothing to do this step!

**✅ Step #3: Update A Record in Cloudflare DNS via REST API**

Finally, the meat 🥩 and potatoes 🥔 of the function!

I created [cloudflare.py](https://github.com/infamousjoeg/aws-ec2-cloudflare-lambda/blob/master/cloudflare.py) as a means 
to creating and testing this function released in 
[pkg/func.py](https://github.com/infamousjoeg/aws-ec2-cloudflare-lambda/blob/master/pkg/func.py#L8).  I decided to keep it 
because it's a great example of how to interact with Cloudflare's REST API using Python in a raw manner.

Back to the function, though.  It authenticates with the provided Cloudflare e-mail address and API key.  After 
confirmation of successful authentication, it then updates the A record associated with the A record name provided via DNS 
ID in the domain managed in Cloudflare associated with the provided Zone ID.
