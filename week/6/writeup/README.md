# Writeup 6 - Binaries I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (50 pts)

CMSC389R-{di5a55-0r-d13}

steps: found "Oh God" input, set env var FOOBAR to " my eyes", created sesame file containing " they burn"

### Part 2 (50 pts)

To start with I didn't have much of an idea what I was looking at in binaryninja, so I went through a few functions looking for intelligible strings. A lot of what got me this flag was guesswork, really. The program first checks for command-line input, "Oh God", in the check1 function. I know this because I saw it in the code, used it a a command-line argument, and got a different output. The strings I could see in the code were useful less as actual hints and more as traces that told me where in the control flow of the main method I had ended up.

The check2 function looks for an environment variable, FOOBAR, which should be set to " my eyes". The string literal this is compared against is stored backwards as "seye ym ". I found it was useful to pay attention to the system calls in check2 and check3, because even though it was very difficult for me to follow what was being stored or accessed in memory, I recognize the system calls and can make educated guesses about what the string literals are for. Finally, check3 looks for a file called "sesame" in the current directory and provides the key if it contains " they burn"; the big switch case at the bottom is apparently a for loop comparing the file's contents to hard-coded character literals that I read off an ascii table to get past the last check.

All of the checks compared some text input against some predetermined string, but they all got the input in different ways, and they all made the comparison in different ways. Each one returned a value, usually either 0x00000000, 0xffffffff, 0xfffffffe or 0xfffffffd, that impacted the flow of the main method. My goal was to get all of them to return 0.

I really don't understand very well how the key is stored, but I see that the update\_flag function is called several times from each check. I don't get what this function does but based on all of the adding and memory accessing functions my best guess is that it's some kind of string manipulation function that generates the correct key only if it is called a certain number of times.
