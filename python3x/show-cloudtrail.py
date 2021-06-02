#!/usr/bin/env python


#
# Author: Yuri Medvinsky
# Date: April 21, 2020
# Info: Show cloudtrail information


import boto3
import sys
import os





####################################
### Main
###
####################################
def main():

  # AWS Profile to use
  if "AWS_PROFILE" in os.environ:
    print ( "AWS_PROFILE={0} \n".format(os.environ['AWS_PROFILE']) )
    profile = os.environ['AWS_PROFILE']
  else:
    print ("AWS_PROFILE env variable not defined")
    sys.exit(1)

  try:
    # Session initiates a connection to AWS using profile from  ~/.aws/credentials
    # In this case your input must match profile credentials
    boto3.setup_default_session(profile_name=profile)
  except:
    print
    print ("[Error:] Profile \"%s\" not found, check settings:" % profile)
    print (" ~/.aws/config")
    print (" ~/.aws/credentials")
    sys.exit()


  # Use low level service class "client"
  # Setup session to ec2 service
  client = boto3.client('cloudtrail')
  response = client.list_trails()

  #print (response)


  for r in response["Trails"]:

    ''' TrailARN: check if it does exists otherwise empty out variable '''
    try:
      if r["TrailARN"]:
        TrailARN = r["TrailARN"]
    except KeyError:
      TrailARN = ''
      pass


    ''' Name: check if it does exists otherwise empty out variable '''
    try:
      if r["Name"]:
        Name = r["Name"]
    except KeyError:
      Name = ''
      pass


    ''' HomeRegion: check if it does exists otherwise empty out variable '''
    try:
      if r["HomeRegion"]:
        HomeRegion = r["HomeRegion"]
    except KeyError:
      HomeRegion = ''
      pass

  
  print (TrailARN)
  print (Name)
  print (HomeRegion)


# The if statement checks if code is being imported by another program.
# The code only runs if its not imported and instead run directly.
if __name__ == "__main__":
  main()
