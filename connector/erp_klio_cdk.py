""" Module connector/erp_klio.py
================================================
 **Natixar Cardiff Klio ERP Connector Stack.**
================================================

© Natixar SAS & CalCool Studios SASU, 2024 All Rights Reserved

This ERP connector operates in push-mode, in real-time when operators
scan and input inbound and outbound shipments in a factory. The collected
data includes origin, nature and quantity of goods.

ERP-KLIO API Endpoint Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The API endpoint is available to receive data via the POST method.
The endpoint is `https://api.natixar.pro/erp-klio`. It will be redirected by a
proxy to the path `/` of a dedicated AWS execute-api endpoint.

Clients should continue to use POST requests on this endpoint. Additionally, if a
GET method is implemented, it will return status information about the connector
itself, such as a GET request to `/erp-klio/hello` which will check if the connection is
operational.
"""

# TODO List

# Import system libraries
from typing import cast

# Import public libraries
from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    #    aws_rolesanywhere as RolesAnywhere,
    #    aws_events as Events,
)
from constructs import Construct

# AWS CDK Construct L3: OpenApiGatewayRestApi
from aws_prototyping_sdk.type_safe_api import (
    TypeSafeRestApi,
    TypeSafeApiIntegration, TypeSafeApiIntegrationOptions, LambdaIntegration,
    OperationDetails, IamAuthorizer,
    ApiKeyOptions
)

from aws_cdk.aws_lambda import IFunction
from aws_cdk.aws_apigateway import ApiKeySourceType

# Import application modules
import core


class KlioStack(Stack):
    """
    KlioStack content:

    #. An IAM Authorizer
    #. A Lambda Integration
    #. A Type-Safe REST API
        https://docs.aws.amazon.com/cli/latest/reference/apigateway/import-rest-api.html
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Global parameters
        assert isinstance(scope.node.find_child("NatixarCoreStack"), core.CoreStack)
        event_bus = cast(core.CoreStack, scope.node.find_child("NatixarCoreStack")).event_bus

        # Copy dependencies ../core/openapi.json and ../core/parameters.json



        # ------------------------------------------------------------
        # IAM Authorizer (based on Access Key / Secret)
        iam_authorizer = IamAuthorizer()

        # ------------------------------------------------------------
        # Lambda Integration
        lambda_integration = LambdaIntegration(
            cast(IFunction, lambda_.Function(
                self, "NatixarKlioLambda",
                runtime=lambda_.Runtime.PYTHON_3_11,
                code=lambda_.Code.from_asset("connector/erp_klio_lambda"),
                handler="erp_klio_lambda.handler",
                environment={
                    "EVENT_BUS_NAME": event_bus.event_bus_name
                }
            ))
        )
        # ------------------------------------------------------------
        # ApiGateway API defined by openapi in external file
        type_safe_api = TypeSafeRestApi(
            self, "NatixarKlioAPI",
            spec_path="connector/erp-klio-openapi.json",
            operation_lookup={  # Defines IDs for operations defined in the JSON file
                "AddData": OperationDetails(method="POST", path="/{scenarioId}"),
                "GetLastId": OperationDetails(method="GET", path="/{scenarioId}/last-id")  # Must not include basePath
            },
            integrations={
                "AddData": TypeSafeApiIntegration(
                    integration=lambda_integration,
                    options=TypeSafeApiIntegrationOptions(api_key_required=True)
                ),
                "GetLastId": TypeSafeApiIntegration(
                    integration=lambda_integration,
                    options=TypeSafeApiIntegrationOptions(api_key_required=True)
                )
            },  # A mapping of API operation to its OpenApiIntegration
            # Optional parameters
            description="REST API for the push-mode Cardiff Klio ERP connector",  # Optional
            endpoint_export_name="NatixarCardiffKlioErpPushApi",  # Optional: Other CDK Apps can use the endpoint
            fail_on_warnings=True,  # Optional: default is False
            api_key_options=ApiKeyOptions(source=ApiKeySourceType.HEADER),  # Optional: always requires API key
            default_authorizer=iam_authorizer,
            # Other optional parameters
            # cloud_watch_role: bool,
            # deploy: bool,
            # deploy_options: StageOptions,
            # disable_execute_api_endpoint: bool, default false => implement default execute-api endpoint
            # domain_name: DomainNameOptions
            # endpoint_types: list[EndpointType]
            # rest_api_name: str, CDK id of the (internal) RestApi construct
            # retain_deployments: bool, default false
            # cors_options: CorsOptions,
            # min_compression_size: Size,
            # web_acl_options: TypeSafeApiWebAclOptions
        )

        # type_safe_api.api.root.add_method("POST")
