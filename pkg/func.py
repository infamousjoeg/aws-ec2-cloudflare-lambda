# Package containing all custom functions

import os
import boto3
import requests
from collections import defaultdict

def getEC2InstanceIPv4(instance_name):
    # Connect to EC2
    ec2 = boto3.resource('ec2')

    # Get information for all running instances
    running_instances = ec2.instances.filter(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']
    }])

    ec2info = defaultdict()
    for instance in running_instances:
        for tag in instance.tags:
            if 'Name' in tag['Key']:
                name = tag['Value']
        # Check for requested instance name
        if name == instance_name:
            public_ip_address = instance.public_ip_address
    
    return public_ip_address


def setCloudflareARecord(public_ip_address, email, api_key, arecord_name, zone_id, dns_id):
    url = 'https://api.cloudflare.com/client/v4/zones/{0}/dns_records/{1}'.format(zone_id, dns_id)
    payload = "{\n\t\"type\":\"A\",\n\t\"name\":\"" + str(arecord_name) + "\",\n\t\"content\":\"" + str(public_ip_address) + "\"\n}"
    headers = {
        'X-Auth-Email': email,
        'X-Auth-Key': api_key,
        'Content-Type': "application/json"
    }
    
    response = requests.request("PUT", url, data=payload, headers=headers)

    return response.status_code