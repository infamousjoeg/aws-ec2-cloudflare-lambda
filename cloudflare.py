# Testing Cloudflare API Use Case

import CloudFlare

zone_id = 'fe3c97fbe85af911ac4817c8298a04b3'
dns_id = '905eb317b3f1aa72ec31a821f21909fa'
instance_ip = '8.8.8.8'
dns_record = [
    {'name':'cdemo.cybr.rocks', 'type':'A', 'content':instance_ip}
]

def main():
    cf = CloudFlare.CloudFlare()
    r = cf.zones.dns_records.post(zone_id, data=dns_record)
    print ('A record updated successfully for cdemo.cybr.rocks')
    exit(0)

if __name__ == '__main__':
    main()