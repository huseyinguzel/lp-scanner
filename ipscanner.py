import subprocess
import shlex
import os
import sys
import time
import pymysql
from tkinter import *


def sqli(ipadres):
        conn = pymysql.connect(
        db='python',
        user='root',
        passwd='1qazXSW2',
        host='localhost')
        c = conn.cursor()
        c.execute("insert into python.ip(ipcol) values(%s)",ipadres)
        conn.commit()
        conn.close()



def msj():
    root=Tk()
    root.geometry('450x450+500+300')
    root.title('ipscanner')
    thelabel=Label(root,text="Yeni ip adresi bulunmuştur")
    mbutton=Button(root,text='ok',fg='red',bg='blue').pack()
    mylebel=Label(root,text='my label').pack()
    thelabel.pack()
    root.mainloop()









def main():
        for ip in range(1,10):
             command_line = "ping -c 3 192.168.43."+str(ip)
             args = shlex.split(command_line)
             ipadres="192.168.43."+str(ip)
             try:
                 subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                 print ("ip canlı:"+"192.168.43."+str(ip))
                 dosya=open("ip.txt","a")
                 dosya.write(ipadres+"\n")
                 time.sleep(1)
                 dosya.close()
                 conn = pymysql.connect(
                 db='python',
                 user='root',
                 passwd='1qazXSW2',
                 host='localhost')
                 c = conn.cursor()
                 sorgu=c.execute("SELECT ipcol  FROM python.ip where ipcol=""%s",ipadres)
                 print(sorgu)
                 if sorgu==0:
                     msj()
                     print("veritabanında yok")
                     cevap=input("eklemek için evet yazın devam etmek için entera basın:")
                     if cevap=="evet":
                         sqli(ipadres)
                     else:
                         print("eklenmedi")
                 else:
                     print("var")
                 conn.close()
             except subprocess.CalledProcessError:
                 print ("ip pinge cevap vermiyor:"+"192.168.43."+str(ip))
        time.sleep(60)
        return  main()


main()
