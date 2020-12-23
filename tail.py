#-*- coding:utf-8 

import time
import re
import requests
import datetime
import logging

lines = []
context = []
f_user_pass = open('UserPass.log', 'a')
f_path = open('Path.log', 'a')


def tail(f):
    f.seek(0.2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(10)
            continue
        yield line

def callback(lines_):
    for line in lines_:
        if line not in lines:
            rule = r'Username:.*'
            rule1 = r'Not Found: (.*)'
            lines.append(line)
            honey = re.findall(rule, line)
            honey1 = re.findall(rule1, line)
            if honey:
                f_user_pass.write(honey[0]+'\n')
                content = """
                type : {type}
                ip : {ip}
                info : {info}
                time : {time}
                """.format(type="port:80", ip="x.x.x.x", info=honey[0], time=str(datetime.datetime.now())[11:19])
                resp = requests.post("http://dk.ttupp.com/weixin/weixin.php",
                  data={"key": "xxx.xxx.xxx", "msg": content})

            elif honey1:
                f_path.write(honey1[0]+'\n')
                content = """
                    type : {type}
                    ip : {ip}
                    info : {info}
                    time : {time}
                    """.format(type="port:80", ip="x.x.x.x", info=honey1[0], time=str(datetime.datetime.now())[11:19])
                resp = requests.post("http://dk.ttupp.com/weixin/weixin.php",
                  data={"key": "xxx.xxx.xxx", "msg": content})
        time.sleep(10)



def main():
    flog = tail(open('Dionaea.log'))
    callback(flog)

if __name__ == "__main__":
    main()