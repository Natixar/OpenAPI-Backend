# Repository Organization

The repository contains AWS Cloudformation stack templates. Some templates are
normally instantiated only once as a stack. Others can be instantiated repeatedly
to create new cloud resources following a pattern.

It is not advisable to create everything at once, because we need the ability to 
update the SaaS bit by bit. Therefore this repository contains several top-level
stack templates. 

The description of the cloud backend is written in Python using **CDK constructs**,
rather than directly in the Cloud Assembly format supported by AWS Cloudformation.

## Target AWS account

Assumes a freshly created AWS account with a root user only.  
The root user is s.cranga@natixar.com  
The account# is 975050054945.

# Initialisation

Manually created elements shall be tagged "infrastructure".  
Elements created by scripts or commands like "cdk bootstrap" shall be tagged "bootstrap".
These elements do not belong to any stack.

All the other elements belong to a stack and most should be taken down with the stacks.  
**The only exceptions are databases.**

## Secure the AWS root user and create an Administrator

https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html

- Add 2FA to the root user "DevOps Natixar"
- Enable access to Billing for IAM Users in the root account (scroll down)
- In the AWS console go to IAM / IAM Identity Center and create "Admin1"
  - Username: Admin1 sur eu-west-3.signin.aws
  - Password: z**********H
- Create an access shortcut for the Admin1 account:  
  https://d-80671fe436.awsapps.com/start/#/console?account_id=975050054945&role_name=AdministratorAccess

AWS access portal URL: https://d-80671fe436.awsapps.com/start 

> [!WARNING]  
>    It's not possible to log-in as an IAM user with an IAM Identity Center identity.
>    IAM Identity Center works as an OIDC OpenID Provider and the principal assumes the
>    role with short duration credentials.

## Install tools and setup single sign-on

The file ~/.aws/config should contain something like:

> [default]
> sso_session = my-sso
> sso_account_id = 975050054945
> sso_role_name = PowerUserAccess
> region = eu-west-3
> output = json
> 
> [sso-session my-sso]
> sso_region = eu-west-3
> sso_start_url = https://d-80671fe436.awsapps.com/start
> sso_registration_scopes = sso:account:access

where the various elements are sent by email when the Administrator is created
in IAM Identity Center. 

Install AWS CLI v2 (min 2.138.0) using the install script in /data/Logiciels/Linux/Frameworks/aws.
Install AWS CDK CLI using ``npm install -g aws-cdk``
Install the JetBrains AWS plugin (optional).

## Prepare the cloud resources

All the identity and other cloud resources until now had to be created manually
by administrators, and they must be tagged "infrastructure"./

The resources created by the following commands are not tagged. They are created
as a group by specific tools, but they are not a stack.

### Boostrap the cloud environment

``cdk bootstrap aws://975050054945/eu-west-3``



# Notes:
1. Investigate fastapi-codegen to automate the generation of FastAPI Python code 
based on OpenAPI specifications deployed in AWS Cloudformation API Gateway.

