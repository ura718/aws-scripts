#!/usr/bin/env python


import boto3
import sys
import json
import os




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
    print ("[Error:] Profile \"{0}\" not found, check settings:".format(profile))
    print (" ~/.aws/config")
    print (" ~/.aws/credentials")
    sys.exit()



  # Use low level service class "client"
  # Setup session to ec2 service
  client   = boto3.client('ec2')

  
  response = client.describe_instances()


  # Print full json dump of all ec2 resources 
  #print json.dumps(response, indent=4, sort_keys=True, default=str)


  print
  print



  ''' Header '''
  print ("{0:<13} {1:<11} {2:<16} {3:<20} {4:<10} {5:<11} {6:<16} {7:<16} {8:<27} {9}".format(
    "VpcId",
    "AZ",
    "SubnetId",
    "Id",
    "Type",
    "State",
    "PublicIp",
    "PrivateIp",
    "LaunchTime",
    "Name"
  ))



  for r in response["Reservations"]:
    for i in r["Instances"]:


      ''' VpcId: check if it does exists otherwise empty out variable '''
      try:
        if i["VpcId"]:
          VpcId = i["VpcId"]
      except KeyError:
        VpcId = '' 
        pass



      ''' AvailabilityZone: check if it does exists otherwise empty out variable '''
      try:
        if i["Placement"]["AvailabilityZone"]:
          AZ = i["Placement"]["AvailabilityZone"]
      except KeyError:
        AZ = '' 
        pass



      ''' SubnetId: check if it does exists otherwise empty out variable '''
      try:
        if i["SubnetId"]:
          SubnetId = i["SubnetId"]
      except KeyError:
        SubnetId = '' 
        pass



      ''' InstanceId: check if it does exists otherwise empty out variable '''
      try:
        if i["InstanceId"]:
          InstanceId = i["InstanceId"]
      except KeyError:
        InstanceId = '' 
        pass



      ''' Type: check if it does exists otherwise empty out variable '''
      try:
        if i["InstanceType"]:
          InstanceType = i["InstanceType"]
      except KeyError:
        InstanceType = '' 
        pass


     
      ''' State: check if it does exists otherwise empty out variable '''
      try:
        if i["State"]["Name"]:
          state = i["State"]["Name"]
      except KeyError:
        state = '' 
        pass



      ''' PublicIP: check if it does exists otherwise empty out variable '''
      try:
        if i["NetworkInterfaces"][0]["Association"]["PublicIp"]:
          publicip = i["NetworkInterfaces"][0]["Association"]["PublicIp"]
      except KeyError:
        publicip = '' 
        pass
      except IndexError:
        publicip = ''
        pass



      ''' PrivateIP: check if it does exists otherwise empty out variable '''
      try:
        if i["NetworkInterfaces"][0]["PrivateIpAddress"]:
          privateip = i["NetworkInterfaces"][0]["PrivateIpAddress"]
      except KeyError:
        privateip = '' 
        pass
      except IndexError:
        privateip = ''
        pass



      ''' LaunchTime: check if it does exists otherwise empty out variable '''
      try:
        if i["LaunchTime"]:
          LaunchTime = i["LaunchTime"]
      except KeyError:
        LaunchTime = '' 
        pass



      ''' Tags: grab Value where Key == Name '''
      try:
        if i['Tags']:
          for t in range(0, len(i['Tags'])):
            if i['Tags'][t]['Key'] == 'Name':
              tag_name = i['Tags'][t]['Value']

      except KeyError:
        tag_name = ''
        pass





      print ("{0:<13} {1:<11} {2:<16} {3:<20} {4:<10} {5:<11} {6:<16} {7:<16} {8}   {9}".format(
        VpcId,
        AZ,
        SubnetId,
        InstanceId,
        InstanceType,
        state,
        publicip,
        privateip,
        LaunchTime,
        tag_name
      ))







# The if statement checks if code is being imported by another program.
# The code only runs if its not imported and instead run directly.
if __name__ == "__main__":
  main()

