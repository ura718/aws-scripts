#!/usr/bin/python

#
# Author: Yuri Medvinsky
# Date: October 17, 2018
# Info: Show Route53 Zones, DNS Names, Aliases, A, SOA records


import boto3
import json



##############################
### Display Hosted Zones
###
##############################
def list_hosted_zones(client):

  # Grab json dump of all hosted zones
  response = client.list_hosted_zones()

  # Header for Hosted Zones
  print "{0:<6} {1:<40} {2:<24} {3:<10}".format('Index','Name','ResourceRecordSetCount','Id') 
  print "{0:<6} {1:<40} {2:<24} {3:<10}".format('-'*5,'-'*30,'-'*22,'-'*20) 


  # Define empty array
  HostedZonesId = []

  # Loop through Array of HostedZones 
  for i in range(0, len(response["HostedZones"])):
    print "{0:<6} {1:<40} {2:<24} {3:<10}".format(
          i, \
          json.dumps(response["HostedZones"][i]["Name"], sort_keys=True, indent=4, separators=(',',': ')).strip('\"'), \
          json.dumps(response["HostedZones"][i]["ResourceRecordSetCount"], sort_keys=True, indent=4, separators=(',',': ')).strip('\"'), \
          json.dumps(response["HostedZones"][i]["Id"], sort_keys=True, indent=4, separators=(',',': ')).strip('\"') 
    )
          
    HostedZonesId.append(json.dumps(response["HostedZones"][i]["Id"], sort_keys=True, indent=4, separators=(',',': ')))

  return HostedZonesId






####################################
### Display Hosted Zones Record Set
### Sub-domains DNS Records
####################################
def list_resource_record_sets(client, HostedZonesId):

  '''
   Query Records using HostedZoneId
   Lets say you have 4 Hosted Zones DNS Entries you will loop over each one
   e.g: <name1>.library.nyu.edu, <name2>.library.nyu.edu ...etc
   And print out its sub records Aliases, A, SOA ...etc
  '''


  print
  for id in HostedZonesId:

    # Remove quotes and split by forward slash take last element
    id = id.split('"')[1].split('/')[-1]

    # Query records for each HostedZone using Id
    response = client.list_resource_record_sets(HostedZoneId=id) 


   

    # Loop against each DNS Name Record Resources and print Values
    for r in range(0,len(response["ResourceRecordSets"])):
      try:
        print "{0:<55} {1:<5} {2:<10}".format(
           json.dumps(response["ResourceRecordSets"][r]["Name"], sort_keys=True, indent=4, separators=(',',': ')).strip('\"'),\
           json.dumps(response["ResourceRecordSets"][r]["Type"], sort_keys=True, indent=4, separators=(',',': ')).strip('\"'),\
           json.dumps(response["ResourceRecordSets"][r]["ResourceRecords"][0]["Value"], sort_keys=True, indent=4, separators=(',',': ')).strip('\"')
        )
      except KeyError:
        pass




    # Loop against each DNS Name Record Resources and print AliasTarget
    for r in range(0,len(response["ResourceRecordSets"])):
      try:
        print "{0:<55} {1:<5} {2:<10}".format(
           json.dumps(response["ResourceRecordSets"][r]["Name"], sort_keys=True, indent=4, separators=(',',': ')).strip('\"'),\
           json.dumps(response["ResourceRecordSets"][r]["Type"], sort_keys=True, indent=4, separators=(',',': ')).strip('\"'),\
           json.dumps(response["ResourceRecordSets"][r]["AliasTarget"]["DNSName"], sort_keys=True, indent=4, separators=(',',': ')).strip('\"')
        )
      except KeyError:
        pass

    print






    '''
    # TEST - Print all Json 
    try:
      print json.dumps(response["ResourceRecordSets"], sort_keys=True, indent=4, separators=(',',': '))
    except KeyError:
      pass
    '''



####################################
### Main
###
####################################
def main():

  # AWS Profile to use
  profile = raw_input("Choose AWS Profile [e.g: virginia-dev, virginia-prod]? ")
  boto3.setup_default_session(profile_name=profile)


  # Setup client session to route53 service
  client     = boto3.client('route53')


  # Show HostedZones
  HostedZonesId = list_hosted_zones(client) 
 
 
  # List Resource Record Set
  list_resource_record_sets(client, HostedZonesId)




# The if statement checks if code is being imported by another program. 
# The code only runs if its not imported and instead run directly. 
if __name__ == "__main__":
  main()
