import sys
import os
import string

import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser


def internet_on():
    try:
        print("Reaching out to Google to ensure internet connectivity")
        urllib.request.urlopen('http://216.58.192.142', timeout=1) #google's ip

        return True
    except urllib.error.URLError as err:
        return False


def newegg_on():
    try:
        print ("Reaching out to Newegg.com")
        urllib.request.urlopen('https://newegg.com', timeout=1)
        return True
    except urllib.error.URLError as err:
        return False




if __name__ == "__main__":

    if internet_on() == True:
        print ("Successfully connected to google/internet")
        if newegg_on() == True:
            print ("Successfullly connected to Newegg.com")



        else:
            print ("Failed to establish connection to Newegg.com, exiting...")
            sys.exit(0)
    else:
        print ("Failed to establish connetion to web, exiting...")
        sys.exit(0)