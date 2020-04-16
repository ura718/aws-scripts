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


  # Use client.describe_<something> to get back resource description
  response = client.describe_subnets()
  


  # Print full json dump of all ec2 resources
  #print json.dumps(response, indent=4, sort_keys=True, default=str)


  print
  print



  ''' Header '''
  print "{0:<11} {1:<19} {2:<30} {3:<11} {4:<16} {5:<13}".format(
    "AZ",
    "Cidr",
    "Name",
    "State",
    "Subnet",
    "VpcID"
  )





  for r in response["Subnets"]:
    ''' AvailabilitiZone: check if it does exists otherwise empty out variable '''
    try:
      if r["AvailabilityZone"]:
        AZ = r["AvailabilityZone"]
    except KeyError:
      AZ = ''
      pass



    ''' CidrBlock: check if it does exists otherwise empty out variable '''
    try:
      if r["CidrBlock"]:
        CidrBlock = r["CidrBlock"]
    except KeyError:
      CidrBlock = ''
      pass



    ''' Tags: grab Value where Key == Name '''
    try:
      if r['Tags']:
        for t in range(0, len(r['Tags'])):
          if r['Tags'][t]['Key'] == 'Name':
            tag_name = r['Tags'][t]['Value']

    except KeyError:
      tag_name = ''
      pass



    ''' State: check if it does exists otherwise empty out variable '''
    try:
      if r["State"]:
        State = r["State"]
    except KeyError:
      State = ''
      pass



    ''' SubnetId: check if it does exists otherwise empty out variable '''
    try:
      if r["SubnetId"]:
        SubnetId = r["SubnetId"]
    except KeyError:
      SubnetId = ''
      pass



    ''' VpcId: check if it does exists otherwise empty out variable '''
    try:
      if r["VpcId"]:
        VpcId = r["VpcId"]
    except KeyError:
      VpcId = ''
      pass


 
    #print AZ, CidrBlock, tag_name, State, SubnetId, VpcId
    print "{0:<11} {1:<19} {2:<30} {3:<11} {4:<16} {5:<13}".format(
    AZ,
    CidrBlock,
    tag_name,
    State,
    SubnetId,
    VpcId
  )



# The if statement checks if code is being imported by another program.
# The code only runs if its not imported and instead run directly.
if __name__ == "__main__":
  main()
