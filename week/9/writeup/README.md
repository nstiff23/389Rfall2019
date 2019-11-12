# Writeup 9 - Forensics II

Name: Nathan Stiff
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Nathan Stiff


## Assignment details

### Part 1 (45 Pts)

The server's IP is 142.93.136.81.
The attacker, 159.203.113.181, begins by running a TCP scan of the 1337bank server, most likely using NMap. Their IP traces to Clifton, New Jersey.
After the scan, they logged in to user v0idcache and downloaded find\_me.jpeg, then uploaded greetz.fpff before logging off.

In order to prevent attacks like this, the server should have a more secure login system. Not only did v0idcache have a very weak password, the attackers sent it over the network in plaintext. This is very likely how they got the password in the first place, by snooping on the network and grabbing the login data. To avoid this vulnerability, the password should be encrypted before it is sent over the network. Either have the ssh client use asymmetric key validation to encrypt the password, or write a separate client app for the server that hashes the password before sending it over the network.

### Part 2 (55 Pts)

Note: my parser (in stub.py) assumes there will be a directory called "carve" in the working directory.

greetz was authored by "fl1nch" on March 27th, 2019 at 12:15 a.m. It has five sections: an ASCII, a coordinate pair, a PNG, and two more ASCII.

CMSC389R-{h0pefully\_y0u\_didnt\_grep\_CMSC389R}

CMSC389R-{w3lc0me\_b@ck\_fr0m\_spr1ng\_br3ak}
