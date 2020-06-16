# This file has the functions for dealing with the file system.
# Please go through the README for instructions on how to configure and run.

import json
import os

# Get the current folder and create the top level folder
starting_dir = str(os.getcwd())
top_dir_name = "Twist"

# Create the base directory to write files into.
# If the directory exists create another one.
dir_create_sequence = 0
while top_dir_name in os.listdir():
    dir_create_sequence += 1

top_dir_name = top_dir_name + str(dir_create_sequence)
base_dir = starting_dir +"/"+ top_dir_name
os.mkdir(base_dir)

def go_to_base_dir():
    global base_dir
    os.chdir(base_dir)

def make_and_enter_item_dir(dir_name):
    current_dir = str(os.getcwd())
    dir_full_name = current_dir +"/"+ dir_name
    os.mkdir(dir_full_name)
    os.chdir(dir_full_name)

def go_to_parent_dir():
    current_dir = str(os.getcwd())
    os.chdir(current_dir + "/../")

def item_name(item_type,item_id,item_name):
    name = item_type.title() +"_"+ str(item_id)
    if item_name:
        name = name +"_"+ item_name.replace("/","-")
    return name

def make_file(file_name,file_content):
    file_handle = open(file_name+".JSON","x")
    file_handle.write(json.dumps(file_content))
    file_handle.close()
