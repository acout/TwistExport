# This file will run the sequence of code that will pull all workspaces, channels, groups and threads from your user scope.
# Please go through the README for instructions on how to configure and run.

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
"workspaces" : "Getting workspaces.",
"groups" : "Getting groups.",
"users" : "Getting users.",
"channels" : "Getting channels.",
"threads" : "Getting threads.",
"comments" : "Getting comments.",
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
def show_progress(progress_type,item_name):
    global step
    print("---")
    step += 1
    print("Step " + str(step))
    if item_name:
        print("For " + progress_message_item[progress_type] +" "+ str(item_name) +":")
    print(progress_messages[progress_type])

# Execution
# Check if auth_key is set (need to update this to check with a ping to Twist)
if not auth_key:
    show_error("auth_key")

# Go to the base directory
files.go_to_base_dir()

# Retrieve and store workspace data
workspaces_data = connect.get_data("workspaces",0,auth_key)
print(workspaces_data)
show_progress("workspaces",0)
for workspace in workspaces_data:
    files.make_and_enter_item_dir(files.item_name("workspace",workspace["id"],workspace["name"]))
    files.make_file(files.item_name("workspace",workspace["id"],workspace["name"]),workspace)

    # Retrieve and store user data
    users_data = connect.get_data("users",workspace["id"],auth_key)
    show_progress("users",workspace["name"])
    files.make_and_enter_item_dir("Users")
    for user in users_data:
        files.make_file(files.item_name("user",user["id"],user["name"]),user)
    files.go_to_parent_dir()

    # Retrieve and store channel data
    channels_data = connect.get_data("channels",workspace["id"],auth_key)
    show_progress("channels",workspace["name"])
    for channel in channels_data:
        files.make_and_enter_item_dir(files.item_name("channel",channel["id"],channel["name"]))
        files.make_file(files.item_name("channel",channel["id"],channel["name"]),channel)
        # Retrieve and store threads data
        threads_data = connect.get_data("threads",channel["id"],auth_key)
        show_progress("threads",channel["name"])
        for thread in threads_data:
            print(files.item_name("thread",thread["id"],thread["title"]))
            files.make_and_enter_item_dir(files.item_name("thread",thread["id"],thread["title"]))
            files.make_file(files.item_name("thread",thread["id"],thread["title"]),thread)
            # Retrieve and store comments
            comments_data = connect.get_data("comments",thread["id"],auth_key)
            show_progress("comments",thread["title"])
            for comment in comments_data:
                files.make_file(files.item_name("comment",comment["id"],""),comment)
            files.go_to_parent_dir()
        files.go_to_parent_dir()
    
    ##Retrieve and share conversations
    conversations_data = connect.get_data("conversations",workspace["id"],auth_key)
    for conversation in conversations_data:
        print(conversation)
        files.make_and_enter_item_dir(files.item_name("conversation",conversation["id"],str(conversation["id"])))
        files.make_file(files.item_name("conversation",conversation["id"],str(conversation["id"])),conversation)
        messages_data = connect.get_data("messages",conversation["id"],auth_key,500,0,"ASC")
        from_obj_index = 500
        while len(messages_data) > 0:
            messages_txt = ""
            first_id = messages_data[0]["id"]
            first_ts = messages_data[0]["posted_ts"]
            for message in messages_data:
                print(message)
                #messages_txt += str(message) + "\n"
                files.append_write_file(files.item_name("message",first_ts,str(first_id)),message)
                #files.append_write_file(files.item_name("message",messages_data[0]["posted_ts"],str(messages_data[0]["id"])),messages_txt)
            messages_data = connect.get_data("messages",conversation["id"],auth_key,500,from_obj_index + 1,"ASC")
            from_obj_index += 500
        files.go_to_parent_dir()
    

# Go to the base directory
files.go_to_base_dir()

show_progress("good_bye",0)
