# This file will run the sequence of code that will pull all workspaces, channels, groups and threads from your user scope.
# Please go through the README for instructions on how to configure the settings file.

import os

# Get the current folder and create the top level folder
current_dir = str(os.getcwd())
top_dir_name = "Twist"
base_dir = current_dir +"/"+ top_dir_name

os.mkdir(base_dir)

def go_to_base_dir():
    global base_dir
    os.chdir(base_dir)

def make_and_enter_item_dir(dir_name):
    os.mkdir(dir_name)
    os.chdir(dir_name)

def move_to_parent_dir():
    os.chdir("../")

def item_name(item_type,item_id):
    name = item_type.title() +"_"+ str(item_ID)
    return name

def make_file(file_name,file_content):
    file_handle = open(file_name,"x")
    file_handle.write(file_content)
    file_handle.close()
