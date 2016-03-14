import subprocess
import shlex
import pymysql


def main():
        for ip in range(1,20):
             command_line = "ping -c 1 192.168.31."+str(ip)
             args = shlex.split(command_line)
             ipadres="192.168.31."+str(ip)
             try:
                 subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                 print ("ip canlı:"+"192.168.31."+str(ip))
                 conn = pymysql.connect(
                 db='python',
                 user='root',
                 passwd='1qazXSW2',
                 host='localhost')
                 c = conn.cursor()
                 c.execute("SELECT * FROM python.ip")
             except subprocess.CalledProcessError:
                 print ("ip pinge ecevap vermiyor:"+"192.168.31."+str(ip))




main()
  
