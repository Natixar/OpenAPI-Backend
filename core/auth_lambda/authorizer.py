""" Module core/auth_lambda/authorizer.py

    The lambda is used by API Gateway to authorize the API calls. It is able to recognize
    both AWS IAM (awsSigv4) and OIDC tokens. If no authorization token is provided or the
    current authorization token is invalid, the lambda follows an OIDC flow and sends back
    a redirect to the login page.

    Created on 30/04/2024
    By Jean-Marc Le Peuvédic
    © CalCool Studios SAS 2021-2024
    © Natixar SAS 2024
"""
# TODO List

# Import system libraries
import json

# Import public libraries
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit

# Import application modules


def handler(event: dict, context: LambdaContext):
    """ Asynchronously invoked handler receiving Authorization events from APIGateway.
    :param event: An AuthorizationEvent
    :param context: A LambdaContext
    :return:
    """
    try:
        token = event['authorizationToken']
        method_arn = event['methodArn']
    
        # Check if this is an AWS Signature
        if token.startswith("AWS"):
            # Handle AWS IAM and Roles Anywhere verification
            is_valid = verify_aws_signature(token)
        else:
            # Handle OIDC token verification
            is_valid = verify_oidc_token(token)
    
        if is_valid:
            return generate_policy('user', 'Allow', method_arn)
        else:
            return generate_policy('user', 'Deny', method_arn)

def verify_aws_signature(token):
    # Logic to verify AWS signature
    return True  # Placeholder for actual validation logic

def verify_oidc_token(token):
    # Logic to verify OIDC token
    return True  # Placeholder for actual validation logic

def generate_policy(principal_id, effect, resource):
    # Generate an IAM policy document
    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': effect,
                'Resource': resource
            }]
        }
    }
