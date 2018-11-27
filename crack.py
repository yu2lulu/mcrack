import sys
import optparse
import os
from multiprocessing import Process,Manager
import telnetlib

sys.path.append('lib')
sys.path.append('conf')

import defaultPort

ROOTPATH=os.path.realpath('.')
DICTPATH=ROOTPATH+'/dict/'


class mcrack:
    cracklist=defaultPort.cracklist
    def __init__(self):
        parse = optparse.OptionParser()
        parse.add_option("-H", '--host', dest='host', help='dest host')
        parse.add_option('-T', '--type', dest='type', help='such:ssh,file,ftp,telnet')
        parse.add_option('--process',dest='process',help='set num of process to run,default 4',default='4')
        parse.add_option('-P','--passwd',dest='passwd',help='set login passwd dictory')
        parse.add_option('-U','--username',dest='username',help='set login user')
        parse.add_option('-F','--file',dest='file',help='set zip/rar file')
        parse.add_option('-p','--port',dest='port',default=None,help='set service port')
        parse.add_option('-v','--verbose',dest='verbose',action='count')
        parse.add_option('-u','--url',dest='url',help='set url to crack')

        example=optparse.OptionGroup(
            parse,
            'Example',
            '''python crack.py -H 127.0.0.1 -Uroot -Ppasswd -T ftp \r\n
            python crack.py -H 127.0.0.1 -Uroot -Ppasswd -T ssh\r\n
            python crack.py -H 127.0.0.1 -Uroot -Ppasswd -T mstsc\r\n
            python crack.py =H 127.0.0.1 -U root -Ppasswd -T mysql\r\n
            ''',
        )
        parse.add_option_group(example)

        self.op, self.args = parse.parse_args()


        if self.op.type == None or self.op.host == None or self.op.passwd==None or self.op.username==None:
            print("Usage: python crack.py -U root  -H 127.0.0.1 -T smb  -P passwd")
        elif self.op.type not in self.cracklist:
            print("Usage: python crack.py -H 127.0.0.1 -T [%s] ......." %"|".join(self.cracklist))
        else:
            self.checkservice()

    def load(self):
        #1.判断对应的文件是否存在,存在就设置字典队列
        print("[-]Dictory Loading.......")
        try:
            self.inputQ=Manager().Queue()
            with open(DICTPATH+self.op.passwd,encoding='utf-8') as f:
                while True:
                    line=f.readline().strip()
                    if line!="":
                        self.inputQ.put(line)
                    else:
                        break
            print("[+] %s -- the dictory is load ok!" %self.op.passwd)

        except Exception as e:
            print("[-] The Passwd File Is Not Exsit!")

        self.run()



    def checkPort(self,port):
        if self.op.type=='http401':
            #判断url是否有传递，没有传递就结束
            if self.op.url!=None:
                return (True,'http401')
            else:
                return (False,'401爆破:请输入URL地址')
        else:
            try:
                telnetlib.Telnet(self.op.host, port=port, timeout=1)
                return (True,'%s:%s is closed!" % (self.op.host, self.op.port)')
            except:
                return (False,"%s:%s is closed!" %(self.op.host,self.op.port))


    def checkservice(self):
        '''对服务的端口检查，不通就直接结束'''

        if self.op.port==None:
            self.op.port=self.cracklist[self.op.type]


        if isinstance(self.op.port,list):
            for port in self.op.port:
                status,msg=self.checkPort(port)
                if not status:
                    print(msg)
                    exit(1)

        else:
            status,msg = self.checkPort(self.op.port)
            if not status:
                print(msg)
                exit(1)

        self.load()

    def run(self):

        #1.设置outputq
        self.outputQ = Manager().Queue()

        #1.调用爆破模块,直接设置进程数

        crackName=self.op.type+'crack'
        moduleName=__import__(crackName)
        t=getattr(moduleName,crackName)(self.op,self.args)


        plist=[]
        for i in range(0,int(self.op.process)):
            p=Process(target=t.run,args=(self.inputQ,self.outputQ,self.op.username))
            plist.append(p)
            p.start()

        print("The CPU Concurrent Number  is %s......" %self.op.process)

        flag=0
        while True:
            if flag==4:
                print("\n[-]not Found Passwd!")
                break
            data=self.outputQ.get()
            if data==1:
                flag+=1
            else:
                print("\n[+]Found Passwd: %s/%s" %(data[0],data[1]))
                break


        print()

        for p in plist:
            p.terminate()




if __name__=="__main__":
    crack=mcrack()
