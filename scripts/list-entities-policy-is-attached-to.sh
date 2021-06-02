#!/bin/bash

# Author: Yuri Medvinsky
# Shows policy arn
# Date: May 28, 2021


if [ -z "$1" ]
then
  echo "Usage: "
  echo " $0 <policy_arn>"
  exit
else

 
  entities=$(aws iam list-entities-for-policy --policy-arn $1 | jq '.[] | .[]')

  printf "\n[+] $1 \n"
  printf "$entities\n\n"
fi


