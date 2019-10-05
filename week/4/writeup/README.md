# Writeup 2 - Pentesting

Name: Nathan Stiff
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Nathan Stiff

## Assignment Writeup

### Part 1 (45 pts)

* CMSC389R-{p1ng\_as\_a\_$erv1c3}
* After nc-ing to wattsamp: -V ; cat /home/flag.txt
* I Googled command injection and read the Wikipedia page. The page reminded me that I can use a semicolon to string bash commands together, so I used the -V option to prevent the ping utility from actually doing anything and followed it up with the commands I needed to find the flag. This was also fairly intuitive to me since I had previously learned to use SQL injection.
* This could very easily be prevented with basic input validation, by ensuring that the input string is actually an IP address or domain name, and nothing else, before passing it to the command line. This is pretty easy with regex. A simpler fix would be to either only accept one word as input, or to delete semicolons and other bash special characters from the input, although these solutions could potentially still allow other unwanted input, so properly validating is always more secure.

### Part 2 (55 pts)

I did this part more or less backwards, because I didn't read the directions very carefully the first time. So, once I figured out how to inject commands, I set up a shell for sending commands to the server by sending whatever command the user entered concatenated to "-V ; ". I also cleaned up the output by removing the version info returned by ping. From there I implemented cd locally; I save the path the user sets locally, and any time I execute a command on the server I cd to the specified directory first. After doing this, I went back and read the assignment again and realized I needed to wrap everything in another shell, so I moved my shell loop to a helper function and built a new shell in main for the top-level commands.
