import o365health
import json
import os

def lambda_handler(event,context):
    o365 = o365health.O365Health()
    o365.main(event, context)

if __name__ == "__main__":
    event = {}
    context = {}
    o365health.O365Health().main(event, context)