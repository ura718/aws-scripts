#!/bin/bash


# --------------------------------------------
# Author: Yuri Medvinsky
# Date: June 26, 2021
# Info: Generate MFA token so user can use CLI.
# --------------------------------------------



if [ -z "$1" ]
then
  echo "Usage: "
  echo "To generate mfa token"
  echo " $0 <user_name> <virtual_mfa_token>"
  exit
else
  # Set command variables
  aws=$(/usr/bin/which aws)
  jq=$(/usr/bin/which jq)

  # Get mfa arn from user profile. MFA should already be configured
  mfa_arn=$($aws iam list-mfa-devices --user-name $1 | $jq -r '.MFADevices[] | .SerialNumber')
 
  # Generate token and redirect output assign to variables
  read -r AccessKeyId SecretAccessKey SessionToken Expiration <<<$($aws sts get-session-token --serial-number $mfa_arn --token-code $2 | $jq -r '"\(.Credentials.AccessKeyId) \(.Credentials.SecretAccessKey) \(.Credentials.SessionToken) \(.Credentials.Expiration)"')

  # Testing output 
  #printf "$AccessKeyId \n" 
  #printf "$SecretAccessKey \n"
  #printf "$SessionToken \n"
  #printf "$Expiration \n"

  # Configure mfa profile with generated token
  $aws configure --profile mfa set aws_access_key_id $AccessKeyId
  $aws configure --profile mfa set aws_secret_access_key $SecretAccessKey
  $aws configure --profile mfa set aws_session_token $SessionToken

  printf "Token generated for user [$1] and will expire on: $Expiration \n"
fi

