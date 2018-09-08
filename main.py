# main.py

from pkg.func import getEC2InstanceIPv4
from pkg.func import setCloudflareARecord
import os

instance_name = os.getenv('EC2_INSTANCE_NAME')
cf_zone = os.getenv('CLOUDFLARE_ZONE_ID')
cf_dns = os.getenv('CLOUDFLARE_DNS_ID')
cf_email = os.getenv('CLOUDFLARE_EMAIL')
cf_api_key = os.getenv('CLOUDFLARE_API_KEY')
cf_arecord_name = os.getenv('CLOUDFLARE_A_NAME')

def handler(event, context):
    # Get EC2 Instance Public IPv4 Address
    public_ipv4_address = getEC2InstanceIPv4(instance_name)
    # FOR TESTING:
    #public_ipv4_address = "1.2.3.4"

    # Update Cloudflare A record with the EC2 Instance public IPv4 address
    cf_status_code = setCloudflareARecord(public_ipv4_address, cf_email, cf_api_key, \
        cf_arecord_name, cf_zone, cf_dns)

# FOR TESTING:
#def main():
#    handler("nothing", "nothing")
#
#if __name__ == "__main__":
#    main()