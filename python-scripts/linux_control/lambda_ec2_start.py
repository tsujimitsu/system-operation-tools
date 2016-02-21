# -*- coding: utf-8 -*-
import boto3


def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.start_instances(
        InstanceIds = [
            'i-XXXXXXXX',
            'i-XXXXXXXX'
        ]
    )

    print response
