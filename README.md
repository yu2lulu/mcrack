#
简介：
  python3多进程爆破程序，目前支持telnet/ftp/mysql/http401/smb/smtp/ssh


#
目录结构：
    conf: 配置文件
    lib:  函数库
    dict: 爆破字典目录
    mcrack.py  入口程序

#
使用简介：
  Usage: crack.py [options]

  Options:
    -h, --help            show this help message and exit
    -H HOST, --host=HOST  dest host
    -T TYPE, --type=TYPE  such:ssh,file,ftp,telnet
    --process=PROCESS     set num of process to run,default 4
    -P PASSWD, --passwd=PASSWD
                          set login passwd dictory
    -U USERNAME, --username=USERNAME
                          set login user
    -F FILE, --file=FILE  set zip/rar file
    -p PORT, --port=PORT  set service port
    -v, --verbose
    -u URL, --url=URL     set url to crack

  Example:
      python crack.py -H 127.0.0.1 -Uroot -Ppasswd -T ftp
      python crack.py -H 127.0.0.1 -Uroot -Ppasswd -T ssh
      python crack.py =H 127.0.0.1 -U root -Ppasswd -T mysql

