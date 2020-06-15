# This file will run the sequence of code that will pull all workspaces, channels, groups and threads from your user scope.
# Please go through the README for instructions on how to configure the settings file.

import json
import requests
from requests_oauthlib import OAuth2Session

# API References
base_url = "https://api.twist.com/api/v3/"
url_suffix ={
"workspaces" : "workspaces/get",
"channels" : "channels/get"
}
url_parameter ={
"workspaces" : 0,
"channels" : "workspace_id"
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

# Retrieve a set of data objects from the server
def get_data_in_batch(data_class,data_id_batch,token_input):
    pass
