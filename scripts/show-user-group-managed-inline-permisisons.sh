#!/bin/bash


# Author: Yuri Medvinsky
# Date: 05/05/2021
# Info: Shows all groups a user belongs to and then prints out permissions (managed/inline) 
# attached to the groups
#####################################


if [ -z "$1" ]
then
  echo "Usage: "
  echo " $0 <iam_user>"
  exit
else

  printf "[+] User: [$1] belongs to groups with permissions: \n\n" 
  for i in $(aws iam list-groups-for-user --user-name $1 | jq -r '.[] | .[] | .GroupName') 
  do 
    printf "group: $i \n"  
    printf " managed: \n" 
    ~/.local/bin/aws iam list-attached-group-policies --group-name $i | /usr/bin/jq '.AttachedPolicies[].PolicyName' 
    printf " inline: \n"
    ~/.local/bin/aws iam list-group-policies --group-name $i | /usr/bin/jq '.PolicyNames[]'
    echo

  done
fi

  printf "[+] User: [$1] has attached permissions: \n\n" 
  printf " managed: \n"
  echo -n " PolicyName: ";  ~/.local/bin/aws iam list-attached-user-policies --user-name $1 | jq '.AttachedPolicies[].PolicyName'
  echo -n " PolicyArn: ";   ~/.local/bin/aws iam list-attached-user-policies --user-name $1 | jq '.AttachedPolicies[].PolicyArn'
  printf " inline: \n"
  ~/.local/bin/aws iam list-user-policies --user-name $1 | jq '.PolicyNames[]'
