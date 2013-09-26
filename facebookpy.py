#!/usr/bin/python
import string
import os
import requests
import json
import re
from pprint import pprint
rs = requests.session()
name = input("Enter ID? ")
proxies = { 'https': "http://172.30.0.16:3128" }
res = rs.request("get", 
   "https://graph.facebook.com/"+name+"/picture?redirect=false",
    proxies=proxies)
file = open("datafile.txt", "w")
data = res.json()
st=""

for key1 in data:
	for key2 in key1+1:
		print (key2)
#urls = re.search("(?P<url>https?://[^\s]+)", data).group("url")

print (data)
#print (urls)
