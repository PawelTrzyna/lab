import boto3


ecs = boto3.client("ecs", endpoint_url="http://localhost:4510")
response = ecs.register_task_definition(
    family="sample-task",
    containerDefinitions=[
        {
            "name": "sample-container",
            "image": "busybox",
            "command": ["echo", "Hello, World!"]
        }
    ],
)

task_definition_arn = response["taskDefinition"]["taskDefinitionArn"]

response = ecs.create_cluster(clusterName="sample-cluster")

cluster_arn = response["cluster"]["clusterArn"]

response = ecs.run_task(
    cluster=cluster_arn,
    taskDefinition=task_definition_arn,
)

task_arn = response["tasks"][0]["taskArn"]

print("Task ARN:", task_arn)
