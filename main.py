# main.py

from pkg.func import getEC2InstanceIPv4
import json
import CloudFlare

def handler(event, context):
    # Get cdemo EC2 Instance Public IPv4 Address
    cdemoIPv4 = getEC2InstanceIPv4('cdemo')

    # Authenticate to Cloudflare API
    cf = CloudFlare.CloudFlare()

    # Update A Record in Cloudflare DNS

    # SNS Publish Success or Failure