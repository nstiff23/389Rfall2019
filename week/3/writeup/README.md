# Homework 3 #
Nathan Stiff

Sept 9 2019

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Nathan Stiff

## Part 1 ##
I call Eric, posing as a company IT tech, and tell him we've noticed odd activity on the network coming from his machine; it's probably just a bug, but we want to check it out to make sure. I will put on a morose tone of voice.

I tell him that certain browser plugins have security vulnerabilities that I need to check for, and ask him what browser he is using, then give him instructions to open his extensions folder. I'll ask a few more questions, like what version his operating system is and whether his firewall is enabled, to build credibility. At some point I apologize for my bad attitude and tell him that it is because my cat, Socks, died last weekend. I'll mention that I never had a pet as a kid, so she was my first, and take the opportunity to ask how he dealt with the loss of his first pet. Once I've poked enough to get his first pet's name, I apologize and ask a few technical questions.

At this point in the call, I need to open up a diagnostic tool, but it'll take a minute or two. While we wait, after a moment or two of awkward silence, I ask him if there's a good bank in town; I moved here just a few months ago and I am trying to get a mortgage so I can stop renting. This should give me the pretext to ask both what bank he uses and how long he's been living in this area. Unless he tells me he grew up here, I'll follow that up by asking if he's lived anywhere interesting before Texas, which hopefully leads me to the town he grew up in. Once I know what I need to know, I'll say the diagnostic is almost finished, wait a few more seconds, and then tell him that everything checks out so it must be something on our end.

Now that I know what bank he uses, I wait a day or two and call him as an employee of the bank. Someone posing as his grandfather contacted the bank and started asking for his contact info, so I had to call him up to notify him. This is where I ask for his actual grandfather's name, which will give me his mother's maiden name. If he asks the suspicious stranger gave his name as William Jacobs and left when they started asking more questions.

I then apologize profusely for the hassle, but since there's been a threat to his account's security he'll have to change his ATM pin number. To save him a trip to the bank, of course he can do it now, over the phone; but especially with some scammer trying to get his money, I'll need to verify his identity by asking him for his old bank PIN in order to confirm the change. After I hassle him into giving me his PIN by making it sound like it would be immensely inconvenient to do it any other way, I apologize some more for the inconvenience until he is ready to hang up.

## Part 2 ##
The Wattsamp server has a number of vulnerabilities that open it to attack by brute-force and possibly more sophisticated methods. The first is the open port on the backend. This port presents a clear target to hackers, whereas if you used a more secure, regular service like ssh for remote access it would be less obvious and less vulnerable. You should also remove references to the backend login portal from your website's source code. The fewer clues, the better.

The server also allows practically infinite connections from a single source. I was able to make thousands of automated, rapid-fire attempts to login until I was able to find the correct password. This could be prevented by restricting the number of login attempts from a single IP, by adding a cooldown to the login script, or through a more sophisticated solution like an IDS (Intrusion Detection System) or IDP (Intrusion Prevention System). These systems monitor your server's web traffic for suspicious connections and either notify the administrator or prevent further attempts, and may also help detect port scanners like nmap that can be used to expose vulnerable ports.

Finally, the most important step you can take is to find a stronger password. Your password was very weak, and was contained in an old list of compromised passwords. No amount of security software will make up for a weak password. If you have trouble keeping track of good passwords for your accounts and devices, it may be worthwhile to invest in a password manager to ensure you have strong passwords.
