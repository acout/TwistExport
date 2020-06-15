# TwistExport
 Simple script to export Twist Data
This README is true and correct as of 14th June 2020.
All future incompatibilities should be blamed on the passage of time.

SOME BACKGROUND:
This set of scripts helps you to export your Twist Data by connecting to the the Twist API and retrieving a set of JSON files that contain your workspaces, channels, groups, threads and messages.

This script was written by a rank amateur, who learnt to code in python less than 24 hours before these words were written. Although the despicable skills are mutable, they do not bode well for you. Hence the disclaimer:
USE WITH CAUTION.

These scripts have been written and tested with a Python 3.8.3, however I don't foresee that the developer has used things that will break in other versions. If you do find bugs with other versions, they are not bugs.

HOW TO USE:
In order to use these scripts follow these steps in precisely this order:

1. Create an integration in the Twist. When creating this, ensure that you have selected "General Integration". (Please go through the Twist Help for how to do this, this README has limited real estate.)

2. Now in the integration settings on the Twist site, go to the OAuth section and find the token marked as "OAuth2 test token".

If you are unable to execute steps 1 & 2, don't email me, just work harder.

3. Copy that token and paste it into the auth_key string in the settings.py file.
DISCLAIMER: This is a workaround for using the Twist testing framework for their integrations. This will use your user scope in Twist (you is the person who is reading and enduring this arduous instruction set).
From the Twist blurb:
"To get started quickly with your app development, you can use the test token to your own account without going through the authorization process. The test token will have the full scope access."
BE CAREFUL, DO NOT EXPOSE THIS TOKEN TO THE PUBLIC.

4. Then run this command in the scripts folder: "python3 run.py"

Enjoy!
