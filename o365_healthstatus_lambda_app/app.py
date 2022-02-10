import os
import logging
from coralogix.handlers import CoralogixLogger
import requests
import json


def lambda_handler(event,context):
    if not os.environ.get('PRIVATE_KEY'):
            raise Exception("Missing the PRIVATE_KEY environment variable. CANNOT CONTINUE")
    
    #Take variables from environment    
    PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
    APP_NAME = os.environ.get('APPLICATION_NAME', 'Office365')
    SUB_SYSTEM = os.environ.get('SUBSYSTEM_NAME', 'Health')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    TENANT = os.environ.get('TENANT')

    #Set up logger objects
    logger = logging.getLogger("Python Logger")
    logger.setLevel(logging.DEBUG)  
    if not logger.handlers:        
        coralogix_handler = CoralogixLogger(PRIVATE_KEY, APP_NAME, SUB_SYSTEM)
        logger.addHandler(coralogix_handler)
    
    payload = 'client_id='+CLIENT_ID+'&scope=https%3A%2F%2Fgraph.microsoft.com%2F.default&client_secret='+CLIENT_SECRET+'&grant_type=client_credentials'
    rqst = requests.post('https://login.microsoftonline.com/'+TENANT+'/oauth2/v2.0/token', data = payload)
    token = json.loads(rqst.content)["access_token"]

    status = requests.get('https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/healthOverviews',
                    headers = { 'content-type': 'application/json', 'Authorization': "Bearer " + token}
                    )
    for element in json.loads(status.content)["value"]:
        
        log = {
            "Context" : json.loads(status.content)["@odata.context"],
            "Service" : element["service"],
            "Status" : element["status"],
            "Id" : element["id"]
        }
        str = json.dumps(log)
        logger.info(str)
        CoralogixLogger.flush_messages()
