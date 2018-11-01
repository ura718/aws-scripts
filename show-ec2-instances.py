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
  
  #print json.dumps(response, indent=4, sort_keys=True, default=str)   // print full json dump


  print "{0:<20} {1:<10} {2}".format(
    "Id",
    "Type",
    "Name"
  )


  for r in response["Reservations"]:
    for i in r["Instances"]:


      try:
        # If Tags exist grab Value where Key == Name
        if i['Tags']:
          for t in range(0, len(i['Tags'])):
            if i['Tags'][t]['Key'] == 'Name':
              tag_name = i['Tags'][t]['Value']

      except KeyError:
        pass



      print "{0:<20} {1:<10} {2}".format(
        i["InstanceId"],
        i["InstanceType"],
        tag_name
      )






  '''
  ec2 = boto3.resource('ec2')

  print "{0:<20} {1:<10} {2:<20} {3}".format(
    "Id", 
    "State",
    "Subnet",
    "Launch Time"
  )


  for i in ec2.instances.all():
    print "{0:<20} {1:<10} {2:<20} {3}".format(
      i.id, 
      i.state['Name'],
      i.subnet_id,
      i.launch_time,
    )
  
  '''




# The if statement checks if code is being imported by another program.
# The code only runs if its not imported and instead run directly.
if __name__ == "__main__":
  main()
