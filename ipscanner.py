import subprocess
import shlex
import pymysql


def sqli(a):
        conn = pymysql.connect(
        db='python',
        user='root',
        passwd='1qazXSW2',
        host='localhost')
        c = conn.cursor()
        c.execute("insert into python.ip(ipcol) values(%s)",a)
        conn.commit()
        conn.close()


def main():
        for ip in range(1,255):
             ipadres="192.168.31."+str(ip)
             command_line = "ping -c 3 "+str(ipadres)
             args = shlex.split(command_line)
             try:
                 subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                 print ("ip canlı:"+"192.168.31."+str(ip))
                 dosya=open("ip.txt","a")
                 dosya.write(ipadres+"\n")
                 dosya.close()
                 conn = pymysql.connect(
                 db='python',
                 user='root',
                 passwd='1qazXSW2',
                 host='localhost')
                 c = conn.cursor()
                 sorgu=c.execute("SELECT ipcol  FROM python.ip where ipcol=""%s",ipadres)
                 print(sorgu)
             except subprocess.CalledProcessError:
                 print ("ip pinge ecevap vermiyor:"+str(ipadres))

main()


