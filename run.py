# This file will run the sequence of code that will pull all workspaces, channels, groups and threads from your user scope.
# Please go through the README for instructions on how to configure the settings file.

import settings
import files
import connect

# Counting progress steps
step = 0

# List of error types and error messages
error_messages = {
"auth_key" : "You have not set your Authentication Key correctly.\nPlease go through the README to see how to fix this."
}

# Function to print the the correct error message
def show_error(error_type):
    print("ERROR: See below for details")
    print(error_messages[error_type])

# List of progress steps and progress messages
progress_messages = {
"workspaces" : "Retrieving workspaces.",
"groups" : "Retrieving groups.",
"channels" : "Retrieving channels.",
"good_bye" : "All is well.\nAstalavista baby!"
}
progress_message_item = {
"groups" : "Workspace",
"channels" : "Workspace",
}

# Function to print a progress message, for a particular item
# The item is identified by the item ID
def show_progress(progress_type,item_id):
    global step
    print("---")
    step+=1
    print("Step " + str(step))
    if item_id:
        print("For " + progress_message_item[progress_type] +" "+ str(item_id) +":")
    print(progress_messages[progress_type])

# Execution
# Check if auth_key is set (need to update this to check with a ping to Twist)
if settings.auth_key == "NotSet":
    show_error("auth_key")

workspaces_data = connect.get_data("workspaces",0,settings.auth_key)
show_progress("workspaces",0)
for workspace in workspaces_data:
    print(workspace["id"])

for workspace in workspaces_data:
    channels_data = connect.get_data("channels",workspace["id"],settings.auth_key)
    show_progress("channels",workspace["id"])
    for channel in channels_data:
        print(channel["id"])

show_progress("good_bye",0)
