# O365Status
Name: o365 Health Status Lambda 
Author: Juan "Trindium" Gimenez (juan@coralogix.com)



1. This Function sends Office 365 health status for a particular tenant into Coralogix.

2. We will create a Registerd Application in Azure AD, to obtain a Client_id and Client_secret  that will grant permission to the lambda to pull Health infromation from Microsoft Graph API. Same information that can be viewed in https://portal.office.com/adminportal/home?#/servicehealth

3. Requirements:
    a. Admin Access to Office 365 and Azure AD 
    b. Coralogix Account
    c. AWS Access with the ability to deploy new Lambdas thru SAM

4. Instructions: 
    a. Run sam build
    b. Run sam deploy --guided
    c. You will be able to see the new Lambda Function in AWS.
    d. Go into the new Lambda Function Configuration and set up the Envirment Variables 
        APPLICATION_NAME
        SUBSYSTEM_NAME
        CLIENT_ID #This is Azure Registered Application ID
        CLIENT_SECRET #This is Azure Registerd Application Secret
        TENANT #This is Azure Tenant ID
        If your Coralogix Account does not ends in .com, you need to add the following variable:
        Us Cluster ( .us )
        CORALOGIX_LOG_URL: "https://api.coralogix.us/api/v1/logs"

        IN Cluster ( .in )
        CORALOGIX_LOG_URL: "https://api.app.coralogix.in/api/v1/logs"

        SG Cluster ( coralogixsg.com )
        CORALOGIX_LOG_URL: "https://api.coralogixsg.com/api/v1/logs"



5. Comments and Collaboration:
    If you have any Comment or Collaboration, please use github issue, create a pull request or just comment us in our Support Chat inside your Coralogix Account
    Any suggestion will be much appriciated 


