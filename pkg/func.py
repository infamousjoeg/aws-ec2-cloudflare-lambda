# Package containing all custom functions

import os
import boto3
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


# Function to read contents of file
def setEnvVarsFromFile(filename):
    with open(filename) as f:
        for line in f:
            if 'export' not in line:
                continue
            if line.startswith('#'):
                continue
            # Remove leading `export `
            # then, split name / value pair
            key, value = line.replace('export ', '', 1).strip().split('=', 1)
            os.environ[key] = value
