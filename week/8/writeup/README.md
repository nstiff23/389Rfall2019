# Writeup 8 - Binaries II

Name: Nathan Stiff
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Nathan Stiff

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?

The admin password is generated with a random number generator seeded with the system time, in seconds. The weakness to this method is that anyone can generate the same password by running the same code with the same seed. By copying the section of code that generates the password into another C program and executing it in the same second as the server, I was able to get a working admin password every time.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.

3. What is the flag?

CMSC389R-{expl017-2-w1n}

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

I got the flag in two steps. First I cracked the password, then I used a buffer overflow to change the command whitelist to "cat flag." To get through the password, I wrote a small C program that runs the same code the server uses to generate the password, then I wrote a bash script that runs this C program and then netcats to the server. From there I just retype the password into the "authenticate" option.

Once I was able to run commands as the server, I had to get around the small, hardcoded command whitelist that would let me ls to see the flag file, but not open it. Looking at the code I saw the "gets" call and knew I could use a buffer overflow to overwrite the whitelist. Because the buffer that "gets" sets is 33 bytes long, any input past 33 characters overwrites the list. I still couldn't run "cat flag" though. It took me a while to realize this was because I needed to null-terminate the command. With a bit of googling I learned that I can type a null character with Ctrl+@, and by telling the server to execute 
```"cat flag^@                        cat flag"``` 
I got the flag.
