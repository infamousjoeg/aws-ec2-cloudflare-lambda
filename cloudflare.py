# Testing Cloudflare API Use Case

import requests
import os

cf_email = os.getenv('CLOUDFLARE_EMAIL')
cf_api_key = os.getenv('CLOUDFLARE_API_KEY')
cf_zone_id = os.getenv('CLOUDFLARE_ZONE_ID')
cf_dns_id = os.getenv('CLOUDFLARE_DNS_ID')
arecord_name = "cdemo.cybr.rocks"
ip_address = "54.243.159.71"

url = 'https://api.cloudflare.com/client/v4/zones/{0}/dns_records/{1}'.format(cf_zone_id, cf_dns_id)

payload = "{\n\t\"type\":\"A\",\n\t\"name\":\"" + str(arecord_name) + "\",\n\t\"content\":\"" + str(ip_address) + "\"\n}"
headers = {
    'X-Auth-Email': cf_email,
    'X-Auth-Key': cf_api_key,
    'Content-Type': "application/json"
    }

def main():
    response = requests.request("PUT", url, data=payload, headers=headers)
    
    print(response.text)


if __name__ == '__main__':
    main()