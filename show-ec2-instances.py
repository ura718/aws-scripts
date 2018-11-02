#!/usr/bin/python


import boto3
import sys
import json



def main():

  # AWS Profile to use
  profile = raw_input("Choose AWS Profile [e.g: virginia-dev, virginia-prod]? ")

  try:
    # Session initiates a connection to AWS using profile from  ~/.aws/credentials
    # In this case your input must match profile credentials
    boto3.setup_default_session(profile_name=profile)
  except:
    print
    print "[Error:] Profile \"%s\" not found, check settings:" % profile
    print " ~/.aws/config"
    print " ~/.aws/credentials"
    sys.exit()



  # Use low level service class "client"
  # Setup session to ec2 service
  client   = boto3.client('ec2')

  
  response = client.describe_instances()


  ''' Print full json dump of all ec2 resources 
  print json.dumps(response, indent=4, sort_keys=True, default=str)
  '''


  print
  print



  ''' Header '''
  print "{0:<13} {1:<11} {2:<16} {3:<20} {4:<10} {5:<10} {6:<20} {7:<20} {8}".format(
    "VpcId",
    "AZ",
    "SubnetId",
    "Id",
    "Type",
    "State",
    "PublicIp",
    "PrivateIp",
    "Name"
  )



  for r in response["Reservations"]:
    for i in r["Instances"]:

      try:
        ''' If Tags exist grab Value where Key == Name '''
        if i['Tags']:
          for t in range(0, len(i['Tags'])):
            if i['Tags'][t]['Key'] == 'Name':
              tag_name = i['Tags'][t]['Value']

      except KeyError:
        pass

     

 
      try:
        ''' Get Public IP and if it does not exist empty out variable '''
        if i["NetworkInterfaces"][0]["Association"]["PublicIp"]:
          publicip = i["NetworkInterfaces"][0]["Association"]["PublicIp"]
      except KeyError:
        publicip = '' 
        pass




      try:
        ''' Get Private IP and if it does not exist empty out variable '''
        if i["NetworkInterfaces"][0]["PrivateIpAddress"]:
          privateip = i["NetworkInterfaces"][0]["PrivateIpAddress"]
      except KeyError:
        privateip = '' 
        pass
      



      print "{0:<13} {1:<11} {2:<16} {3:<20} {4:<10} {5:<10} {6:<20} {7:<20} {8}".format(
        i["NetworkInterfaces"][0]["VpcId"],
        i["Placement"]["AvailabilityZone"],
        i["SubnetId"],
        i["InstanceId"],
        i["InstanceType"],
        i["State"]["Name"],
        publicip,
        privateip,
        tag_name
      )







# The if statement checks if code is being imported by another program.
# The code only runs if its not imported and instead run directly.
if __name__ == "__main__":
  main()
