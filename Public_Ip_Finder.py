#This program will print IPV4 Public/Internet IP address of your machine
#I have made use of requests module
#https://ipecho.net/plain
#https://checkip.amazonaws.com
#both of them are working , can use any one
#set this program in your environment variable so that you can use it easily through cmd :)

import requests

def FindMyPublicIp():
    ip = requests.get('https://checkip.amazonaws.com').text.strip()
    print("Your Public IP is " + ip)
  
FindMyPublicIp()
