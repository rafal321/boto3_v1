#!/usr/bin/env python3.6

import boto3
import pprint

ec2_re = boto3.resource('ec2', region_name='eu-west-1')

for each in ec2_re.instances.all():     # this is object
    print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    print(each.state, each.state['Name'])
    print(each.public_ip_address)
    print(each, each.instance_id)
    print('-- SECURITY GROUPS --')
    print(each.security_groups[0]['GroupId'], each.security_groups[0]['GroupName'])
    print('--- sg looping resource---')
    for sgg in each.security_groups:
        print(f"Printing security groups: {sgg}")
    print('-- NETWORK INTERFACES --')
    print(each.network_interfaces)
    print('-- TAGS --')
    for t in each.tags:                 # because it is nested dictionary
        print(t)
        print(t['Value'])
print('==============================================')
print('=== CLIENT ===================================')

ec2_cli = boto3.client('ec2', region_name='eu-west-1')

# pprint.pprint(ec2_cli.describe_instances())   = aws ec2 describe-instances
for eachh in ec2_cli.describe_instances()['Reservations']:
    for eachh_in in eachh['Instances']:
        print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
        #pprint.pprint(eachh_in)                - prints everything
        print(eachh_in['InstanceId'], eachh_in['State'])
        print(eachh_in['InstanceId'], eachh_in['State']['Name'])
        print('-- SECURITY GROUPS --')
        print(eachh_in['SecurityGroups'])      #- prints all sg
        print(eachh_in['SecurityGroups'][0])
        print('--- sg looping ---')
        for sg in eachh_in['SecurityGroups']:
            print(sg['GroupName'])
        print('-- TAGS --')
        for tt in eachh_in['Tags']:
            print(tt)
            print(tt['Value'])
