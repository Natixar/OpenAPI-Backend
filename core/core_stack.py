""" module core/core_stack.py
-----------------------------------------------------------------
 **Natixar Impact Assessment Tool Core Stack.**
-----------------------------------------------------------------

© Natixar SAS & CalCool Studios SASU, 2024 All Rights Reserved

The impact assessment tool is built around a database that stores
environmental, social and governance impact causes. For instance,
the database stores the occurrence of a transportation operation,
and the back-end, on the fly converts the recorded information into
greenhouse gas emissions using the most accurate methods.
This file describes the core stack, which is the center of the tool
and the connection with the default front-end. The tool has open
APIs and can be connected to other tools easily provided one has the
access rights.
"""

# Standard libraries
from typing import cast
import json

# Public libraries
import jsonref

from aws_cdk import (
    # Duration,
    Stack,
    AssetStaging, GetContextKeyResult,
    aws_lambda as lambda_,
    aws_rolesanywhere as RolesAnywhere,
    aws_events as Events,
    aws_iam as Iam,
)

from aws_cdk.aws_lambda import IFunction
from aws_cdk.aws_apigateway import ApiKeySourceType

from aws_prototyping_sdk.type_safe_api import (
    TypeSafeRestApi,
    TypeSafeApiIntegration, TypeSafeApiIntegrationOptions, LambdaIntegration,
    OperationDetails, IamAuthorizer,
    ApiKeyOptions
)

from constructs import Construct

# Project modules
from core.utils import dereference


class CoreStack(Stack):
    """
    Core stack contents:

    #. Security Architecture based on AWS RolesAnywhere

       <link to doc>
    #. AWS EventBridge (default bus)

       <link to doc>
    #. Database AWS RDS (PostgreSQL)

        <link to doc>
    #. Front-end business logic using AWS Lambda

        <link to doc>

        - API front-end calls processing
        - Handle S3:ObjectCreated and S3:ObjectRemoved for quotas monitoring
        - Handle S3:ObjectCreated to detect ABC BEGES data collection files (core file input)
        - Process ABC BEGES data collection files
        - Process weekly inventories of client files (P2)
    #. Front-end API with AWS API Gateway v2

        <link to doc>
    #. S3 Buckets to store uploaded files, inventories,

        <link to doc>
    #. Audit with AWS Cloudtrail

        <link to doc>
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bootstrap_tags = [{"key": "bootstrap", "value": "core"}]

        # 1 - Security architecture for M2M access is built around X509 certificate.
        # Intermediate CA certificate are stored as TrustAnchors in AWS RolesAnywhere.
        # They act as Groups. All the final certificates signed by an Intermediate CA have the
        # same permissions, but the audit trail is distinct.
        #
        # 1.1 - AWS RolesAnywhere resources: The Trust Anchor and the Omni Profile.

        # A single profile is used with all the credentials requests. The profile holds the
        # roles required by all the clients.
        self.clients_profile_omni = RolesAnywhere.CfnProfile(
            self, "ClientProfileOmni",
            name="ProfileNatixarOmni",
            role_arns=[],  # Created empty - tools stacks will populate it
            # Optional properties
            duration_seconds=7200,
            enabled=True,
            tags=bootstrap_tags
        )

        # Clients : each client has an X509 certificate that is used by enterprise tools to push
        #           data into the Natixar SaaS. Note that in addition to having the secret key associated with
        #           the certificate, the connector requests an IAM Role tailored for the API access it needs.
        self.clients_trust_anchor = RolesAnywhere.CfnTrustAnchor(
            self, "ClientTrustAnchor",
            name="Natixar AWS Clients Trust Anchor",
            source=RolesAnywhere.CfnTrustAnchor.SourceProperty(
                source_data=RolesAnywhere.CfnTrustAnchor.SourceDataProperty(
                    x509_certificate_data="""
-----BEGIN CERTIFICATE-----
MIIG9DCCBNygAwIBAgIIWkdzt0U7wc4wDQYJKoZIhvcNAQELBQAwazELMAkGA1UE
BhMCRlIxFDASBgNVBAoTC05hdGl4YXIgU0FTMSEwHwYDVQQDExhOYXRpeGFyIEFX
UyBUcnVzdCBBbmNob3IxIzAhBgkqhkiG9w0BCQEWFGlkZW50aXR5QG5hdGl4YXIu
cHJvMCAXDTI0MDQxODAwMDAwMFoYDzk5OTkxMjMxMjM1OTU5WjBOMQswCQYDVQQG
EwJGUjEUMBIGA1UEChMLTmF0aXhhciBTQVMxDDAKBgNVBAsTA0NSTTEbMBkGA1UE
AxMSTmF0aXhhciBDbGllbnRzIENBMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIIC
CgKCAgEAwyQ1aYnu736tJ689N5jVc26rmXggt8t/5oyxtxtyG2tUtVSIBT3REofi
4HS08joYO1iy/VB88FCkCD3v322wPZx43Ra3azdoZIkNKXOGj8NZlbXmVLaOxfXi
lD6bTT2+vJj3dlteoXxJTWbMMS8vV/ebNjec/UHfW6OUFpho+EQpxsAbfhN3q3+n
EeGh0oy/VQv9Zg1PtKGXQZRylxzyrRe4GA+FQdodA9C57Dk3n/nH2H2Nzs8agrFL
rXHHKejbjPCl4hQc1xB+Ol9A5U/qLpmb9r628PD6yRp6NEvT1FzvULs6cKiU9w1K
mk5gGH1KAmLa5R5QQJdxX3revo/0cXzXBUB+yP8Oka0rCYWcAkesdRfUrPkGmOwv
/UuVFLxTH2jhg1z6V0SobpsfbBKPaR3WjfvMlV6oeA2k2TJSWqr3wLAix2s3PAO3
lznLzgtgN54QO9lF+wiz4hLaPh1a7eNfiutmSbADqzFoyOcFx2xeE3UZV64GOmzq
+L/6k1fTCrq5ScuvnfJbB2eVt7+3a4ZjV9aeZyPB+10Hucph/Lm3po/iwbIMPidz
vBazoSax1sMnPqvm3L9uQW1A+LoY+6Pjsv963m3MqHY+j8Fxd9KLjgPgjZe4/XRU
iXTOycI4H3PjQ8wLswuK7XIHMg/nDZIMo95Eq0Sc2rH98KM6IuMCAwEAAaOCAbUw
ggGxMBIGA1UdEwEB/wQIMAYBAf8CAQAwHQYDVR0OBBYEFCUlMgfpR4lR3gfsYKgL
dxwIFPO2MAsGA1UdDwQEAwIBhjA8BgNVHR8ENTAzMDGgL6AthitodHRwczovL2F1
dGgubmF0aXhhci5wcm8vY3JsL05hdGl4YXJBV1MuY3JsMBEGCWCGSAGG+EIBAQQE
AwIABzA+BglghkgBhvhCAQMEMRYvVVJJOmh0dHBzOi8vYXV0aC5uYXRpeGFyLnBy
by9jcmwvTmF0aXhhckFXUy5jcmwwQgYJYIZIAYb4QgEEBDUWM1VSSTpodHRwczov
L2F1dGgubmF0aXhhci5wcm8vY3JsL05hdGl4YXJDbGllbnRzLmNybDA3BglghkgB
hvhCAQcEKhYoVVJJOmh0dHBzOi8vYXBwLm5hdGl4YXIucHJvL2NsaWVudF9yZW5l
dzBBBglghkgBhvhCAQgENBYyVVJJOmh0dHBzOi8vYXBwLm5hdGl4YXIucHJvL05h
dGl4YXJDbGllbnRzQ0FQb2xpY3kwHgYJYIZIAYb4QgENBBEWD3hjYSBjZXJ0aWZp
Y2F0ZTANBgkqhkiG9w0BAQsFAAOCAgEAXw20MRtnDPDqSsQqVfbnsiqj+MYY2/p0
8SLmAc9d2X7+udt5YrDyererLtynnFMNGUIN3DvVNQTD4YhxlhBA4XG3p4xtJrGC
wG1cXszI2DCN6j8kIu1yoAC7fgpzNhs/0L2XY+qWoVxYj4bg9f3BYExKnBtVSHEc
oQphQkVebi7lDumhcTqeUP/jzaV/haSz/V7V+IN0K7zPHL6geXHtxr6qU7SzbG1s
UdTEsv2gzHErP6sY00Fr4CCQAwoErDcHrpgRTSb8xWUY2pPdRbjPltL6lIsx2f2w
iVVRNYdJHDpS6pjcfDXIzKa1pyQzR7JGc7ZXIsEdJZGNGqF+ct/JP7AE40gv8XPf
nicoRGuWBvZ9f8t48BxdbKMC6GKRaB3IRn9qKguSfVAsJV9Ok0ueiFcii8HNxet0
lxfv3L7rlcU+pVVjwRxHIg8Gzt8XN6OZ8o2Ss2SP0Y8WuBDuOI3VFzg7BrUqJujL
40wp68OKXCAGV73qijlqHS6mBJhyk8zBQIn6v+8po5kwd1AXp6xqgd1OOu2BksDQ
vXViuvaat9P/ICXXBDSzdQqzAi3ci9M8x028FMYr8zFthZkx8RR/nlBkNjvB41am
IlmXLtpC2fVSLgIF5gS1QmaCotnX97ZS8M48eGJjAQHs6tHlxKEKeh1s6sI60z7J
Q69sRTEardk=
-----END CERTIFICATE-----
"""
                ),
                source_type="CERTIFICATE_BUNDLE"
            ),
            # Optional properties
            enabled=True,
            tags=bootstrap_tags
        )

        # 1.2 - OIDC federation resources: the OIDC identity provider
        self.oidc_provider = Iam.OpenIdConnectProvider(
            self, "OpenIdConnect_auth.natixar.pro",
            url="https://auth.natixar.pro",
            client_ids=["5e9cba0b-4978-4a24-88c0-0a45b0ed067f"],
            thumbprints=["cabd2a79a1076a31f:21d253635cb039d43:29:a5:e8"],
        )

        # 1.3 - The authorization lambda
        # noinspection PyTypeChecker
        self.auth_lambda = lambda_.Function(
            self, "UnifiedAuthorizer",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="authorizer.handler",
            code=lambda_.Code.from_asset("core/auth_lambda")
        )
        
        # 2 - Events and event bus.
        # The default event bus exists as soon as an account is created.
        # In our case it's arn:aws:events:eu-west-3:975050054945:event-bus/default
        # Other stacks will use the event bus to schedule periodic events (polled sources)
        # or simply to process data.
        self.event_bus = Events.EventBus.from_event_bus_name(self, "DefaultEventBus",
                                                             event_bus_name="default")

        # 3 - Database

        # 4 - Front-end business logic using AWS Lambda
        
        # runtime requires in fact a runtime factory function
        # noinspection PyTypeChecker
        lambda_integration = LambdaIntegration(
            cast(IFunction, lambda_.Function(
                self, "NatixarKlioLambda",
                runtime=lambda_.Runtime.PYTHON_3_11,
                code=lambda_.Code.from_asset("core/api_lambda"),
                handler="core_api.handler",
                environment={
                        "EVENT_BUS_NAME": self.event_bus.event_bus_name
                }
            ))
        )

        # 5 - Front-end API with AWS API Gateway v2

        # ------------------------------------------------------------
        # IAM Authorizer (based on Access Key / Secret)
        iam_authorizer = IamAuthorizer()
        integration = TypeSafeApiIntegration(
            integration=lambda_integration,
            options=TypeSafeApiIntegrationOptions(api_key_required=True)
        )
        
        type_safe_api = TypeSafeRestApi(
            self, "NatixarCoreAPI",
            spec_path=dereference("core/openapi.json"),
            operation_lookup={  # Defines IDs for operations defined in the JSON file
                "CreateClient": OperationDetails(method="POST", path="/clients"),
                "ListClients": OperationDetails(method="GET", path="/clients"),
                "GetClient": OperationDetails(method="GET", path="/clients/{clientId}"),
                "UpdateClient": OperationDetails(method="PUT", path="/clients/{clientId}"),
                "DeleteClient": OperationDetails(method="DELETE", path="/clients/{clientId}"),
                "ListScenarios": OperationDetails(method="GET", path="/scenarios"),
                "CreateScenario": OperationDetails(method="POST", path="/scenarios"),
                "GetScenario": OperationDetails(method="GET", path="/scenarios/{scenarioId}"),
                "UpdateScenario": OperationDetails(method="PUT", path="/scenarios/{scenarioId}"),
                "DeleteScenario": OperationDetails(method="DELETE", path="/scenarios/{scenarioId}"),
                "GetScenarioRanges": OperationDetail(method="GET", path="/scenarios/{scenarioId}/ranges"),
            },
            integrations={
                "CreateClient"  : integration,
                "ListClients"   : integration,
                "GetClient"     : integration,
                "UpdateClient"  : integration,
                "DeleteClient"  : integration,
                "ListScenarios" : integration,
                "CreateScenario": integration,
                "GetScenario"   : integration,
                "UpdateScenario": integration,
                "DeleteScenario": integration,
                "GetScenarioRanges": integeration
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
            rest_api_name="CoreCO2TrackAPI",
            # retain_deployments: bool, default false
            # cors_options: CorsOptions,  <===
            # min_compression_size: Size,
            # web_acl_options: TypeSafeApiWebAclOptions
        )

        # 6 - S3 Buckets
        # - One for uploaded files from the "Upload" menu entry. Events are emitted by S3
        #   trigger an analysis of the type of file, and dedicated file stacks must listen for
        #   specific events and process the files.
        # - One for automatic inventories generated weekly by AWS S3 Inventory and where file
        #   type predicates are stored by file stacks.
