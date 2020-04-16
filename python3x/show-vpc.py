#!/usr/bin/env python


#
# Author: Yuri Medvinsky
# Date: October 24, 2018
# Info: Show vpc info


import boto3
import sys
import os



####################################
### VPC Info
###
####################################
def vpc_info(response, vpc_id):

  for x in response["Vpcs"]:
    # Get VPC ID
    VpcId = x['VpcId']

    # Get Cidr Block
    CidrBlock = x['CidrBlock'] 

    # Declare Variable if empty
    tag_name = ''


    try:  
      # If Tags exist grab Value where Key == Name
      if x['Tags']:
                
        for i in range(0, len(x['Tags'])):
          if x['Tags'][i]['Key'] == 'Name':
            tag_name = x['Tags'][i]['Value']

    except KeyError:
      pass


    print ("{0:<15} {1:<15} {2:<15}".format(VpcId, CidrBlock, tag_name))

    vpc_id.append(VpcId)


  return vpc_id





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
  client   = boto3.client('ec2')
  response = client.describe_vpcs()



  # Get VPC Info
  vpc_id = []
  vpc_id = vpc_info(response, vpc_id)






# The if statement checks if code is being imported by another program.
# The code only runs if its not imported and instead run directly.
if __name__ == "__main__":
  main()
