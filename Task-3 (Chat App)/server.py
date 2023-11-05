'''
  Task-3 of Oasis InfoByte Internship:
                           "CHAT APPLICATION"
                                             '''

from socket import *
import os
import random as ra
import smtplib
import time

# Server

def ser():
    s = socket()
    s.bind(('localhost',1200))
    # we binded this socket with port no: 1200

    print('socket is created')

    s.listen(4) # looking for any clients to connect
    print('waiting for connection...')

    c,address = s.accept()
    print("")
    c.send(bytes('wecolme','utf-8'))
    print("address is:",address)

    while True:
        na = c.recv(1024).decode()
        # looking for any msg sent by client

        print("client:",na)
        ms = input("you: ")
        c.send(bytes(ms,'utf-8'))

        if ms=='end chat':
            break

    c.close()

def log():
    os.system('cls')
    print("\n",format('', '<5'), "Login credentials")
    us_n = input("user_name: ")
    p = input("password:")

    if us_n in us and p in pas and us.index(us_n)==pas.index(p):
        os.system('cls')

        ser()
    else:
        print("Invalid credentials\nTry again!")


# credentials
us = ['abc']
pas = ['abcd']
s2 = ra.randint(0000, 10000)

def main():
    print("")
    print(format('','<8'),'CHAT APP')
    print(format('','<9'),'welcome')
    a = input("Do you have account?(y/n):")

    if a=='y' or a=='Y':
        log()

    else:
        s = input("provide user_name:")
        s1 = input("provide password:")
        s3 = input("enter your gmail id:")
        print("")
        print("please wait for otp verification..")
        otp(s3)
        time.sleep(3)
        print("OTP is sent, check inbox/spam")
        s4 = int(input("enter otp:"))

        if s4==s2:
            us.append(s)
            pas.append(s1)
            print('account created successfully')
            log()
        else:
            print("Invalid otp!")

# otp verfication using mail id

def otp(s3):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('bossbasket638@gmail.com',"fzephektzflufaps")
    msg = "Welcome to CHAT APP\nyour otp is:"+str(s2)
    server.sendmail('bossbasket638@gmail.com', s3, msg)
    server.quit()

if __name__ == "__main__":
    main()
