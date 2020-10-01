#This program will print IPV4 Public/Internet IP address of your machine
#https://ipecho.net/plain
#I have made use of requests module
#https://checkip.amazonaws.com
#both of them are working , can use any one
#set this program in your environment variable so that you can use it easily through cmd :)

import requests

def FindMyPublicIp():
    ip = requests.get('https://checkip.amazonaws.com').text.strip()
    print("Wow! here it's your provided Id " + ip)
  
FindMyPublicIp()
