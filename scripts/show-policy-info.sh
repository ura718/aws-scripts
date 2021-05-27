#!/bin/bash

# Author: Yuri Medvinsky
# Shows detailed policy information
# Date: May 27, 2021


if [ -z "$1" ]
then
  echo "Usage: "
  echo " $0 <policy_name>"
  exit
else

  printf "[+] policy: [$1] info: \n\n"
  arn=$(~/.local/bin/aws iam list-policies | /usr/bin/jq -r ".Policies[] | select(.PolicyName==\"$1\")" | /usr/bin/jq -r '"\(.Arn)"')

  version=$(~/.local/bin/aws iam list-policies | /usr/bin/jq -r ".Policies[] | select(.PolicyName==\"$1\")" | jq -r '"\(.DefaultVersionId)"')

  ~/.local/bin/aws iam get-policy-version --policy-arn $arn --version-id $version

  printf "\n[+] $arn : $version \n"
fi

