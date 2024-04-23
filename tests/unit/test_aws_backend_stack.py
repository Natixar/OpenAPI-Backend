import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_backend.aws_backend_stack import AwsBackendStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_backend/aws_backend_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsBackendStack(app, "aws-backend")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
