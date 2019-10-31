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

The code that generates the admin password begins at line 89 in main(). As mentioned above, the trouble with this generator is that anyone who knows how it works can replicate it. There are a number of ways to make this more secure; for a start, it would be better to have a separate executable for generating the password so that even if someone gets the source code for the public-facing server executable they still don't know how the password is generated. But really, the proper thing to do is to use a good static password stored behind a secure hashing algorithm such as SHA-256.

At line 68 in the exec\_command function you use the gets function. This function is highly deprecated and known to be vulnerable to buffer overflow exploits; because it does not check the size of the input buffer when it takes input, the end user can accidentally or intentionally overwrite other data below the buffer on the stack. This can be avoided by getting input using a secure function, like fgets(), which limits the number of bytes of input the program can read.

3. What is the flag?

CMSC389R-{expl017-2-w1n}

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

I got the flag in two steps. First I cracked the password, then I used a buffer overflow to change the command whitelist to "cat flag." To get through the password, I wrote a small C program that runs the same code the server uses to generate the password, then I wrote a bash script that runs this C program and then netcats to the server. From there I just retype the password into the "authenticate" option.

Once I was able to run commands as the server, I had to get around the small, hardcoded command whitelist that would let me ls to see the flag file, but not open it. Looking at the code I saw the "gets" call and knew I could use a buffer overflow to overwrite the whitelist. Because the buffer that "gets" sets is 33 bytes long, any input past 33 characters overwrites the list. I still couldn't run "cat flag" though. It took me a while to realize this was because I needed to null-terminate the command. With a bit of googling I learned that I can type a null character with Ctrl+@, and by telling the server to execute 
```cat flag^@``` followed by 25 spaces, then ```cat flag``` 
I got the flag.
