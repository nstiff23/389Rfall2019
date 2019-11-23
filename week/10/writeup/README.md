# Writeup 10 - Crypto I

Name: Nathan Stiff
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Nathan Stiff


## Assignment details

### Part 1 (45 Pts)

1. The password hash is stored in the first 16 bytes, followed by the message hash in the next 16 bytes, then the initialization vector in the next 16 bytes, then the message.

2. The program uses aes128 encryption on the ledger and verifies passwords and file integrity using md5 hashing. Using md5 poses a risk because it works very quickly, so attackers have a much easier time brute-forcing hashes. It would be better to use a deliberately slow hashing algorithm to mitigate the risk of brute-force attacks.

3. I'm able to read the initialization vector and the hashes of both the key and the message without decrypting.

4. All data in the ledger is encrypted using aes128. The user provides an encryption key which is checked against a hash, and if it is verified then it is used to decrypt the ledger. In theory, this makes it impossible for someone to read the ledger without knowing the key, ensuring confidentiality.

5. The program checks the integrity of the ledger by hashing the ledger message and comparing it against the expected hash. However, the expected hash is stored in the file, so anyone who can tamper with the file can also modify the hash to match, making this feature essentially useless against an observant attacker.

6. The program checks the user's authenticity by taking a password as an argument, hashing it, then hashing the first two bytes of that hash. This has a clear flaw in that by reducing the first hash to two characters then hashing again, this design will accept any password with a hash matching the first two characters of the actual password's hash, thus drastically increasing the likelihood of collisions.

7. The initialization vector is generated randomly for a new file and stored in the file; the same IV is used each time, which weakens the encryption.

### Part 2 (45 Pts)

1. My code is in crack.c. The executable is in the week 10 folder as well as in the writeup folder and it will run the same from either.
I started by looking at ledger.c, and noticed that when the user-submitted password is hashed most of the hash is tossed. From here it became clear that I would be able to brute-force the two characters whose hash match the hash stored in ledger.bin, so I coded that first. Once I had that working, I wrote some more loops to generate random strings and hash them until one of them produced a hash starting with the same two characters as I identified in the previous step. The program outputs this 3-letter string which can then be sent to the ledger as a valid password.

2. CMSC389R-{k3y5p4c3\_2\_sm411}

### Part 3 (10 Pts)

Systems should be designed so that even an attacker with full knowledge of the system cannot break it. The idea behind cryptography is to replace a difficult problem, keeping a message secret, with an easier one, keeping a key secret. If keeping the message secret also requires keeping the encryption scheme secret, this replaces a difficult problem with an equally difficult problem. If the security of the system does not rely on obscurity, then even if the source code is leaked an attacker will not be able to get in.
One could argue that keeping the code secret still adds an extra layer of security through obscurity, but if software is open-source then many people can look at it and find vulnerabilies so they can be fixed before they cause any real damage.
Because we have to operate under the assumption that a determined hacker can discover your implementation, said implementation should be as secure as possible. The fewer people who have legitimately acquired and analyzed a bit of code, the more likely it is that an attacker who illegitimately acquires the source will find a vulnerability that the developers were unaware of. 
Thus, it is generally safer to avoid obscurity as it is likely to become a dependence whether it is intended to or not.
