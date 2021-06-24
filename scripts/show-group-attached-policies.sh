#!/bin/bash

# Author: Yuri Medvinsky
# Shows group attached policies
# Date: June 14, 2021


if [ -z "$1" ]
then
  echo "Usage: "
  echo " $0 <group_name>"
  exit
else

  printf "[+] Group attached Policies: [$1] \n\n"
  group_attached_managed_policies=$(~/.local/bin/aws iam list-attached-group-policies --group-name $1 | /usr/bin/jq -r '.AttachedPolicies[] | .PolicyName' | sort  2>/dev/null) 

  group_attached_inline_policies=$(~/.local/bin/aws iam list-group-policies --group-name $1 | /usr/bin/jq -r '.PolicyNames[]' | sort 2>/dev/null) 


  printf "\n[+] Managed Policies  \n"
  printf "\n$group_attached_managed_policies \n"

  printf "\n[+] Inline Policies  \n"
  printf "\n$group_attached_inline_policies \n"
fi

