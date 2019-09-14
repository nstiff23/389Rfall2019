# Writeup 2 - OSINT

Name: Nathan Stiff
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Nathan Stiff

## Assignment Writeup

### Part 1 (45 pts)

ejnorman84's real name is Eric J. Norman. He works at Watt's Amp Energy, wattsamp.net. I started on namechk.com, found in the OSINT framework, through which I discovered his Instagram, @ejnorman84; Twitter, @EricNorman84; and Reddit, /u/ejnorman84. He tweeted two email addresses, ejnorman84@gmail.com and ejnorman@protonmail.com. His Gmail account is also listed in the whois DNS records for wattsamp.net, along with what is presumably his work address, 1300 Adabel Drive in El Paso, TX, and his phone number, 202.656.2837.

wattsamp.net lives at IP 157.230.179.99, which whois puts in New York City. securitytrails.com lists not DNS history. On the website, I was able to find only the robots.txt file. An nmap scan of this IP reveals http running on port 80, ssh running on port 22 and a service called "waste?" on port 1337. nmap and the website's directory browser both say it is an Ubuntu system.

BONUS FLAGS: html_h@xor_lulz; Do_you-N0T_See_this; n0_indexing_pls

### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*

I started by creating a function to beat the captcha, because that was what I knew how to do. I've never really worked with Python or done much network coding before this assignment, but parsing was more familiar. Then I worked on getting a connection and after a few tries wrote code that could pass the captcha and submit a username and password about half of the time. From there I refined the code to make it more reliable, and split the task into four processes.

My code is still in stub.py. It takes about an hour to find the correct password and, due to a networking bug I never got around to fixing, will give dozens of false positives first because it sometimes accepts the password prompt as a success (I did not know what the shell prompt would look like so I just had it alert me for anything that wasn't "Fail").

Final flag: CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}
