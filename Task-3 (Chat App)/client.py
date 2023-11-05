from socket import *
import smtplib
import os
import random as ra
import time

# Client

def cli():
    c = socket()
    # socket creation

    c.connect(('localhost',1200))
    # connecting sever of port no. 1200
    print("")
    while True:
        ms = c.recv(1024).decode()
        # receives any messages sent by server

        print("server:",ms)
        name = input("you: ")
        c.send(bytes(name,'utf-8')) # message sending in form of bytes

        if name=='end chat':
            # you can stop chat by typing 'end chat'
            break

    c.close()

# credentials
us = ['client']
pas = ['pas']
s2 = ra.randint(0000,10000)

def log():
    os.system('cls')
    print("\n",format('', '<5'), "Login credentials")
    us_n = input("user_name: ")
    p = input("password:")

    if us_n in us and p in pas and us.index(us_n) == pas.index(p):
        os.system('cls')
        cli()
    else:
        print("Invalid credentials\nTry again!")

def main():
    print("")
    print(format('','<8'),"CHAT APP")
    a = input("Do you have account?(y/n):")
    if a=='Y' or a=='y':
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

def otp(s3):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('bossbasket638@gmail.com', "fzephektzflufaps")
    msg = "Welcome to CHAT APP\nyour otp is:" + str(s2)
    server.sendmail('bossbasket638@gmail.com',s3, msg)
    server.quit()

if __name__ == '__main__':
    main()

'''
   code by: U. Nandan Varma 
                              '''
