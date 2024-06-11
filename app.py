#!/usr/bin/env python3

import aws_cdk as cdk

from core.core_stack import CoreStack
from connector.erp_klio_cdk import KlioStack

app = cdk.App()

# In a stack, if you don't specify 'env', this stack will be environment-agnostic.
# Account/Region-dependent features and context lookups will not work,
# but a single synthesized template can be deployed anywhere.
ENV = cdk.Environment(account='975050054945', region='eu-west-3')


core = CoreStack(app, "NatixarCoreStack",
    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=ENV,

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
)

KlioStack(app, "NatixarKlioAPI", env=ENV).add_dependency(core)

app.synth()
