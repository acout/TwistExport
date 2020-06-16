# This file has the functions that will pull data from the API reference.
# Please go through the README for instructions on how to configure the settings file.

import json
import requests
from requests_oauthlib import OAuth2Session

# API References
# Base API URL
base_url = "https://api.twist.com/api/v3/"
# API URL suffix for each type of query
url_suffix ={
"workspaces" : "workspaces/get",
"users" : "workspaces/get_users",
"groups" : "groups/get",
"channels" : "channels/get",
"threads" : "threads/get",
"comments" : "comments/get",
"conversations" : "conversations/get",
"messages" : "conversation_messages/get"
}
# Single parameter to reference scope
url_parameter ={
"workspaces" : 0,
"users" : "id",
"groups" : "workspace_id",
"channels" : "workspace_id",
"threads" : "channel_id",
"comments" : "thread_id",
"conversations" : "workspace_id",
"messages" : "conversation_id"
}

# Retrieve a data object from the server
def get_data(data_class,parameter_id,token_input):
    token = {
    "access_token" : token_input
    }
    client = OAuth2Session(token=token)
    if url_parameter[data_class]:
        url = base_url + url_suffix[data_class] +"?"+ url_parameter[data_class] +"="+ str(parameter_id)
    else:
        url = base_url + url_suffix[data_class]
    response_json = client.get(url).text
    response_data = json.loads(response_json)
    # This output is a list
    # Each element of the list is dict
    # Each dict represents an instance of the data class
    response = response_data
    return response
