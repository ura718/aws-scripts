#!/bin/bash

# Author: Yuri Medvinsky
# Shows policy arn
# Date: May 28, 2021


if [ -z "$1" ]
then
  echo "Usage: "
  echo " $0 <policy_name>"
  exit
else

  arn=$(~/.local/bin/aws iam list-policies | /usr/bin/jq -r ".Policies[] | select(.PolicyName==\"$1\")" | /usr/bin/jq -r '"\(.Arn)"')

  printf "\n[+] $1 \n"
  printf "    $arn\n\n"
fi


