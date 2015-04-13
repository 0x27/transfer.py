#!/usr/bin/python2
# coding: utf-8
# transfer.sh cleartext client
# Version: 20150413.1
# Author: Darren Martyn
import requests
from clint.textui import progress
import sys
import os

def upload(file_path):
    try:
        filepath, filename = os.path.split(file_path)
    except Exception, e:
        print "{-} Something has gone horribly wrong! Please report on the github issue tracker with the following backtrace: \n%s" %(e)
    upload_url = "https://transfer.sh/%s" %(filename)
    try:
        r = requests.put(url=upload_url, data=open(file_path, "rb"))
    except Exception, e:
        print "{-} Something has gone horribly wrong! Please report on the github issue tracker with the following backtrace: \n%s" %(e)
    try:
        return r.text.strip()
    except Exception, e:
        print "{-} Something has gone horribly wrong! Please report on the github issue tracker with the following backtrace: \n%s" %(e)

def download(url):
    # kludge for now
    filename = url.replace("https://transfer.sh", "")
    filename = filename.split("/")[2]
    print "{*} Saving file to %s" %(filename)
    try:
        r = requests.get(url=url, stream=True)
        with open(filename, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
                if chunk:
                    f.write(chunk)
                    f.flush()
    except Exception, e:
        print "{-} Something has gone horribly wrong! Please report on the github issue tracker with the following backtrace: \n%s" %(e)

def main(args):
    if len(args) != 2:
       sys.exit("use: %s <path/to/file> OR <transfer.sh url>" %(args[0]))
    if "https://transfer.sh" in args[1]:
        print "{+} Downloading %s" %(args[1])
        try:
            download(url=args[1])
        except Exception, e:
            print "{-} Something has gone horribly wrong! Please report on the github issue tracker with the following backtrace: \n%s" %(e)
    else:
        try:
            print "{+} Uploading %s" %(args[1])
            file_url = upload(file_path=args[1]) 
        except Exception, e:
            print "{-} Something has gone horribly wrong! Please report on the github issue tracker with the following backtrace: \n%s" %(e)
        if file_url != None:
            print file_url
        else:
            sys.exit("Something fucked up... Like, seriously. Possibly an issue at the remote end?")
        
if __name__ == "__main__":
    main(args=sys.argv)
