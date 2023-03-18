import boto3

ec2 = boto3.client("ec2", endpoint_url="http://localhost:4597")

response = ec2.run_instances(
    ImageId="ami-0c55b159cbfafe1f0",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1
)

print("Instance ID:", response["Instances"][0]["InstanceId"])
