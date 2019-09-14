OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Friday, September 13 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `ejnorman84`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `ejnorman84` and answer the following questions:

1. What is `ejnorman84`'s real name? Eric J. Norman

2. Where does `ejnorman84` work? What is the URL to their website? Watts Amp Energy; wattsamp.net

3. List all personal information (including social media accounts, contacts, etc) you can find about `ejnorman84`. For each, briefly detail how you discovered them. 
IG:ejnorman84 from namechk.com, found in the osint framework.
Twitter:@EricNorman84 from his Instagram
Email: ejnorman84@gmail.com and ejnorman@protonmail.com from DNS records and his Twitter
Reddit: ejnorman84
He works at 1300 Adabel Drive in El Paso, TX according to whois. He likely lives in El Paso as well, which is hinted at in his various social media accounts.
Phone number: 202.656.2837 from whois

4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
157.230.179.99; New York City in whois. Apparently no history, according to securitytrails.com.

5. List any hidden files or directories you found on this website.
Only robots.txt

6. What ports are open on the website? What services are running behind these ports? How did you discover this?
nmap reveals port 80 for http, port 22 for ssh, port 1337 for "waste?"

7. Which operating system is running on the server that is hosting the website? How did you discover this?
Ubuntu is the operating system listed when viewing site directories and by nmap.

8. **BONUS:** Did you find any other flags on your OSINT mission? Note: the standard flag format for bonus flags is `*CMSC389R-{}`. (Up to 9 pts!)
html_h@x0r_lulz
Do_you-N0T_See_this
n0_indexing_pls

### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to `ejnorman84`'s server via an open port that you should have found in Part 1.

Once you have gained access to `ejnorman84`'s account with the correct login credentials, you will have access to a system shell.

Use your knowledge of Linux and OSINT techniques to locate the flag file and submit its contents for points.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!

#### Response

I started by creating a function to beat the captcha, because that was what I knew how to do. I've never really worked with Python or done much network coding before this assignment, but parsing was more familiar. Then I worked on getting a connection and after a few tries wrote code that could pass the captcha and submit a username and password about half of the time. From there I refined the code to make it more reliable, and split the task into four processes. 

My code is still in stub.py. It takes about an hour to find the correct password and, due to a networking bug I never got around to fixing, will give dozens of false positives first because it sometimes accepts the password prompt as a success (I did not know what the shell prompt would look like so I just had it alert me for anything that wasn't "Fail").

### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, push it up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
