#!/usr/bin/python2
# coding: utf-8
# transfer.sh cleartext client
# Version: 20150413.1
# Author: Darren Martyn
import requests
import sys
import os

def upload(file_path):
    try:
        filepath, filename = os.path.split(file_path)
    except Exception, e:
        print "{-} Something has gone horribly wrong! Please report on the github issue tracker with the following backtrace: \n%s" %(e)
    upload_url = "https://transfer.sh/%s" %(filename)
    try:
        r = requests.put(url=upload_url, files={filename: open(file_path, "rb")})
    except Exception, e:
        print "{-} Something has gone horribly wrong! Please report on the github issue tracker with the following backtrace: \n%s" %(e)
    try:
        return r.text.strip()
    except Exception, e:
        print "{-} Something has gone horribly wrong! Please report on the github issue tracker with the following backtrace: \n%s" %(e)

def main(args):
    if len(args) != 2:
       sys.exit("use: %s <path/to/file>" %(args[0]))
    try:
        print "uploading %s" %(args[1])
        file_url = upload(file_path=args[1]) 
    except Exception, e:
        print "{-} Something has gone horribly wrong! Please report on the github issue tracker with the following backtrace: \n%s" %(e)
    if file_url != None:
        print file_url
    else:
        sys.exit("Something fucked up... Like, seriously. Possibly an issue at the remote end?")
        
if __name__ == "__main__":
    main(args=sys.argv)
