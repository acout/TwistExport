# This file will run the sequence of code that will pull all workspaces, channels, groups and threads from your user scope.
# Please go through the README for instructions on how to configure the settings file.

import settings
import files
import connect

# List of error types and error messages
error_messages = {
"auth_key" : "You have not set your Authentication Key correctly.\nPlease go through the README to see how to fix this."
}

# Function to print the the correct error message
def show_error(error_type):
    if error_type in error_messages:
        print(error_messages[error_type])
    else:
        print("DEBUG: Wrong error_type")

# List of progress steps and progress messages
progress_messages = {
"good_bye" : "All is well.\nAlta vista baby!"
}

# Function to print a progress message.
def show_error(progress_type):
    if progress_type in progress_messages:
        print(progress_messages[progress_type])
    else:
        print("DEBUG: Wrong progress_type")

# Execution
# Check if auth_key is set (need to update this to check with a ping to Twist)
if settings.auth_key == "NotSet":
    show_error("auth_key")
