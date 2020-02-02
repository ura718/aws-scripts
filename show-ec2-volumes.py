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


  response = client.describe_volumes()


  # Print full json dump of all ec2 resources
  #print json.dumps(response, indent=4, sort_keys=True, default=str)


  print
  print


  ''' Header '''
  print "{0:<11} {1:<20} {2:<22} {3:<11} {4:<9} {5:<5} {6:<23} {7:<7} {8:<10} {9}".format(
    "AZ",
    "InstanceId",
    "VolumeId",
    "VolumeType",
    "Size",
    "IOPS",
    "SnapshotId",
    "State",
    "Device",
    "Name"
  )




  for v in response["Volumes"]:
    ''' AvailabilityZone: check if it does exists otherwise empty out variable '''
    try:
      if v["AvailabilityZone"]:
        AZ = v["AvailabilityZone"]
    except KeyError:
      AZ = ''
      pass




    ''' InstanceId: check if it does exists otherwise empty out variable '''
    try:
      if v["Attachments"][0]["InstanceId"]:
        InstanceId = v["Attachments"][0]["InstanceId"]
    except KeyError:
      InstanceId = ''
      pass
    except IndexError:
      InstanceId = ''
      pass




    ''' VolumeId: check if it does exists otherwise empty out variable '''
    try:
      if v["Attachments"][0]["VolumeId"]:
        VolumeId = v["Attachments"][0]["VolumeId"]
    except KeyError:
      VolumeId = ''
      pass
    except IndexError:
      VolumeId = ''
      pass




    ''' VolumeType: check if it does exists otherwise empty out variable '''
    try:
      if v["VolumeType"]:
        VolumeType = v["VolumeType"]
    except KeyError:
      VolumeType = ''
      pass




    ''' Size: check if it does exists otherwise empty out variable '''
    try:
      if v["Size"]:
        Size = str(v["Size"]) + str(" GiB")
    except KeyError:
      Size = ''
      pass




    ''' IOPS: check if it does exists otherwise empty out variable '''
    try:
      if v["Iops"]:
        IOPS = v["Iops"]
    except KeyError:
      IOPS = ''
      pass




    ''' SnapshotId: check if it does exists otherwise empty out variable '''
    try:
      if v["SnapshotId"]:
        SnapshotId = v["SnapshotId"]
      else:
        SnapshotId = ''
    except KeyError:
      SnapshotId = ''
      pass      



    ''' State: check if it does exists otherwise empty out variable '''
    try:
      if v["State"]:
        State = v["State"]
    except KeyError:
      State = ''
      pass



    ''' Device: check if it does exists otherwise empty out variable '''
    try:
      if v["Attachments"][0]["Device"]:
        Device = v["Attachments"][0]["Device"]
    except KeyError:
      Device = ''
      pass
    except IndexError:
      Device = ''
      pass


    ''' Tags: grab Value where Key == Name '''
    try:
      if v['Tags']:
        for t in range(0, len(v['Tags'])):
          if v['Tags'][t]['Key'] == 'Name':
            tag_name = v['Tags'][t]['Value']

    except KeyError:
      tag_name = ''
      pass


    print "{0:<11} {1:<20} {2:<22} {3:<11} {4:<9} {5:<5} {6:<23} {7:<10} {8:<10} {9}".format(
      AZ,
      InstanceId,
      VolumeId,
      VolumeType,
      Size,
      IOPS,
      SnapshotId,
      State,
      Device,
      tag_name
    )

     





# The if statement checks if code is being imported by another program.
# The code only runs if its not imported and instead run directly.
if __name__ == "__main__":
  main()

