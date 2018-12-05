#!/usr/bin/python

#
# Author: Yuri Medvinsky
# Date: June 22, 2018
# Info: Provide a list of all permissions assigned to user group


import boto3
import json





##################################################
# List Of Group Names
#
##################################################
def ListGroups(iam):

  response = iam.list_groups()

  print "{0:<60} {1:<30}".format('Arn', 'GroupName')
  print "{0:<60} {1:<30}".format('-'*60, '-'*30)

  for i in response['Groups']:
    print "{0:<60} {1:<30}".format(i['Arn'], i['GroupName'])

  print






##################################################
# Show all Managed Policies permissions
#
##################################################
def ManagedPolicy(iam, groupname):
  response = iam.list_attached_group_policies(GroupName=groupname)

  for i in response['AttachedPolicies']:
      Name = i['PolicyName']
      Arn  = i['PolicyArn']

      # Get policy definitions
      description = iam.get_policy(PolicyArn=Arn)
      version     = description['Policy']['DefaultVersionId']

      print Name
    
      print json.dumps(iam.get_policy_version(PolicyArn=Arn, VersionId=version)['PolicyVersion']['Document'], indent=4)
      print '-'*50






##################################################
# Show all Inline Policies permissions
#
##################################################
def InlinePolicy(iam, groupname):
  response = iam.list_group_policies(GroupName=groupname)
  for policy in response['PolicyNames']:
    result = iam.get_group_policy(GroupName=groupname, PolicyName=policy)
     
    Name = result['PolicyName']                 # stand alone name
    PolicyDocument = result['PolicyDocument']   # This has the json information that you can use with json.dump

    print 
    print Name
    print json.dumps(iam.get_group_policy(GroupName=groupname, PolicyName=policy)['PolicyDocument'], indent=4)
    print '-'*50






def main():

  # AWS Profile to use
  profile = raw_input("Choose AWS Profile [e.g: virginia-dev/virginia-prod]? ")
  boto3.setup_default_session(profile_name=profile)


  # Setup client session to iam service
  iam     = boto3.client('iam')
  
  ListGroups(iam)
  groupname = raw_input("Please enter group name: ")
  print
  
  # Get Managed Policy Permissions
  ManagedPolicy(iam, groupname)

  # Get Inline Policy Permissions
  InlinePolicy(iam, groupname)



# The if statement checks if code is being imported by another program. 
# The code only runs if its not imported and instead run directly. 
if __name__ == "__main__":
  main()
