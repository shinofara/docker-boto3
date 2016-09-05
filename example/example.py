#!/usr/bin/env python
#coding: utf-8
import boto3

session = boto3.Session(profile_name="example")
client = session.client("ec2")

print client.describe_instances()
