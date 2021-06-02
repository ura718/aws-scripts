#!/usr/bin/env python


import boto3
import sys
import json
import os



def main():

  # AWS Profile to use

  if "AWS_PROFILE" in os.environ:
    print ( "AWS_PROFILE={0} \n".format(os.environ['AWS_PROFILE']) )
    profile = os.environ['AWS_PROFILE']
  else:
    print ("AWS_PROFILE env variable not defined")
    sys.exit(1)


  try:
    # Session initiates a connection to AWS using profile from  ~/.aws/credentials
    # In this case your input must match profile credentials
    boto3.setup_default_session(profile_name=profile)
  except:
    print
    print ("[Error:] Profile \"%s\" not found, check settings:" % profile)
    print (" ~/.aws/config")
    print (" ~/.aws/credentials")
    sys.exit()



  # Use low level service class "client"
  # Setup session to elb service
  client   = boto3.client('elb')


  response = client.describe_load_balancers()


  # Print full json dump of elb resources
  #print json.dumps(response, indent=4, sort_keys=True, default=str)


  print
  print




  ''' Header '''
  print ("{0:<13} {1:<16} {2:<21} {3:<72} {4:<21} {5:<20}".format(
    "VpcId",
    "Scheme",
    "LoadBalancerPort",
    "DNSName",
    "InstancePort",
    "InstanceId"
  ))



  for r in response["LoadBalancerDescriptions"]:

    ''' VpcId: check if it does exists otherwise empty out variable '''
    try:
      if r["VPCId"]:
        VpcId = r["VPCId"]
    except KeyError:
      VpcId = ''
      pass

    
   
    ''' Scheme: check if it does exists otherwise empty out variable '''
    try:
      if r["Scheme"]:
        Scheme = r["Scheme"]
    except KeyError:
      Scheme = ''
      pass





    ''' Protocol: check if it does exists otherwise empty out variable '''
    try:
      if r["ListenerDescriptions"][0]["Listener"]["Protocol"]:
        Protocol = r["ListenerDescriptions"][0]["Listener"]["Protocol"]
    except KeyError:
      Protocol = ''
      pass
    except IndexError:
      Protocol = ''
      pass
      


    ''' LoadBalancerPort: check if it does exists otherwise empty out variable '''
    try:
      if r["ListenerDescriptions"][0]["Listener"]["LoadBalancerPort"]:
        LoadBalancerPort = []
        for i in r["ListenerDescriptions"]:
          ''' Append All listener ports to variable '''
          LoadBalancerPort.append(i["Listener"]["LoadBalancerPort"])

        ''' Append Protocol to Port '''
        LoadBalancerPort.append(Protocol)

    except KeyError:
      LoadBalancerPort = ''
      pass
    except IndexError:
      LoadBalancerPort = ''
      pass





    ''' DNSName: check if it does exists otherwise empty out variable '''
    try:
      if r["DNSName"]:
        DNSName = r["DNSName"]
    except KeyError:
      DNSName = ''
      pass





    ''' InstanceProtocol: check if it does exists otherwise empty out variable '''
    try:
      if r["ListenerDescriptions"][0]["Listener"]["InstanceProtocol"]:
        InstanceProtocol = r["ListenerDescriptions"][0]["Listener"]["InstanceProtocol"]
    except KeyError:
      InstanceProtocol = ''
      pass
    except IndexError:
      InstanceProtocol = ''
      pass

    ''' InstancePort: check if it does exists otherwise empty out variable '''
    try:
      if r["ListenerDescriptions"][0]["Listener"]["InstancePort"]:
        InstancePort = []
        for i in r["ListenerDescriptions"]:
          ''' Append All listener ports to variable '''
          InstancePort.append(i["Listener"]["InstancePort"])

        ''' Append Instance Protocol to Instance Port '''
        InstancePort.append(InstanceProtocol)

    except KeyError:
      InstancePort = ''
      pass
    except IndexError:
      InstancePort = ''
      pass



    ''' InstanceId: check if it does exists otherwise empty out variable '''
    try:
      if r["Instances"][0]["InstanceId"]:

        InstanceId = []

        for i in r["Instances"]:
          ''' Gets the value from hashed index i = [e.g: i.values() ]
              Convert list value to string       = [e.g: ''.join() ]
          '''
          InstanceId.append(''.join(i.values()))
        # If you want to put newline after every InstanceId. Just formatting preference...
        #InstanceId = '\n'.join(InstanceId)   


    except KeyError:
      InstanceId = ''
      pass
    except IndexError:
      InstanceId = 'No Instances Registered'
      pass




    print ("{0:<13} {1:<16} {2:<21} {3:<72} {4:<21} {5:<20}".format(
      str(VpcId),
      str(Scheme),
      str(LoadBalancerPort),
      str(DNSName),
      str(InstancePort),
      str(InstanceId)
    ))
    



# The if statement checks if code is being imported by another program.
# The code only runs if its not imported and instead run directly.
if __name__ == "__main__":
  main()
