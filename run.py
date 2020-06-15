# This file will run the sequence of code that will pull all workspaces, channels, groups and threads from your user scope.
# Please go through the README for instructions on how to configure the settings file.

import files
import connect

# Read the oauth key.
auth_key_file = open("oauth_key.txt","r")
auth_key = auth_key_file.read(47)
auth_key_file.close()

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

# List progress messages for each progress step
progress_messages = {
"workspaces" : "Listing workspaces.",
"groups" : "Listing groups.",
"users" : "Listing users.",
"channels" : "Listing channels.",
"threads" : "Listing threads.",
"comments" : "Listing comments.",
"good_bye" : "All is well.\nAstalavista baby!"
}
# List of parent items for each progress step
progress_message_item = {
"groups" : "Workspace",
"users" : "Workspace",
"channels" : "Workspace",
"threads" : "Channel",
"comments" : "Thread"
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
if not auth_key:
    show_error("auth_key")

# Go to the base directory
files.go_to_base_dir()

# Retrieve list of workspaces
workspaces_data = connect.get_data("workspaces",0,auth_key)
files.show_progress("workspaces",0)
for workspace in workspaces_data:
    pass
    #files.make_and_enter_item_dir(files.item_name("workspace",workspace["id"]))

# For each workspace, retrieve list of users
for workspace in workspaces_data:
    users_data = connect.get_data("users",workspace["id"],auth_key)
    show_progress("users",workspace["id"])
    for user in users_data:
        print(user["id"])

# For each workspace, retrieve list of channels
for workspace in workspaces_data:
    channels_data = connect.get_data("channels",workspace["id"],auth_key)
    show_progress("channels",workspace["id"])
    for channel in channels_data:
        print(channel["id"])
        threads_data = connect.get_data("threads",channel["id"],auth_key)
        show_progress("threads",channel["id"])
        for thread in threads_data:
            print(thread["id"])

show_progress("good_bye",0)
