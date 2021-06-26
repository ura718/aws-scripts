#!/bin/bash

aws iam list-policies | jq -r '.Policies[] | .PolicyName' | sort
