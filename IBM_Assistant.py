from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
import json

authenticator = IAMAuthenticator('<YOUR_API_KEY>')
assistant = AssistantV2(
    version='2020-02-05',
    authenticator=authenticator)

assistant.set_service_url('https://gateway.watsonplatform.net/assistant/api')

try:
    # Invoke a Watson Assistant method
    response_create = assistant.create_session(
        assistant_id='<YOUR_ASSISTANT_ID_HERE>').get_result()
    print(json.dumps(response_create, indent=2))

    while True:
        msg = str(input(">>> "))
        assistant_response = assistant.message(
            assistant_id='<YOUR_ASSISTANT_ID_HERE>',
            session_id=response_create['session_id'],
            input={
                'message_type': 'text',
                'text': msg
                }
            ).get_result()
        print(json.dumps(assistant_response, indent=2))

    response_delete = assistant.delete_session(
        assistant_id='<YOUR_ASSISTANT_ID_HERE>',
        session_id=response_create['session_id']).get_result()
    print(json.dumps(response_delete, indent=2))
    
except ApiException as ex:
    print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
