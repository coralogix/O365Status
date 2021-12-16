# O365Status
Name: o365 Health Status Lambda 
Author: Juan "Trindium" Gimenez (juan@coralogix.com)
License: Apache 2.0



1. This Function sends Office 365 health status for a particular tenant into Coralogix.

2. We will create a Registerd Application in Azure AD, that will grant permission to the lambda to pull Health infromation from Microsoft Graph API. Same information that can be viewed in https://portal.office.com/adminportal/home?#/servicehealth

3. Requirements:
    a. Admin Access to Office 365 and Azure AD 
    b. Coralogix Account
    c. AWS Access with the ability to deploy new Lambdas thru SAM

4. Instructions:
    a. Modify the template.yaml file to fit your enviromental variables such as PRIVATE_KEY, CLIENT_ID, CLIENT_SECRET, TENANT
    b. If your Coralogix Account does not ends in .com, you need to add the following variable:
        Us Cluster
        CORALOGIX_LOG_URL: "https://api.coralogix.us/api/v1/logs"

        IN Cluster
        CORALOGIX_LOG_URL: "https://api.app.coralogix.in/api/v1/logs"
    c. Run sam build
    d. Run sam deploy --guided
    e. You will be able to see the new Lambda Function in AWS.

5. Comments and Collaboration:
    If you have any Comment or Collaboration, please use github issue, create a pull request or just comment us in our Support Chat inside your Coralogix Account
    Any suggestion will be much appriciated 


