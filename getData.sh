#!/bin/bash

Echo "Deleting old data..."
rm -r /Users/jp/stockExchange/Data
Echo "Data deleted."
scp -i /Users/jp/Keys/AWS_EC2_KEY.pem -r ec2-user@ec2-52-14-226-1.us-east-2.compute.amazonaws.com:stockExchange/Data /Users/jp/stockExchange/Data