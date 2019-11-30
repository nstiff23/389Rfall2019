# Writeup 1 - Web I

Name: Nathan Stiff
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Nathan Stiff


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

I figured out pretty quickly that I was providing input to the site from the item? parameter. I tried a lot of stuff for this, including using URL encoding to mask the OR, putting a null byte %00 between the O and the R, putting a comment /\*\*/ between the O and the R, using UNHEX() and CHAR() to represent the OR, etc. All of these things either were caught by the filter or returned a blank page. Most returned a blank page. This may have been because I was malforming the rest of the input; I could never add an apostrophe to the URL without getting redirected to the index page. I do not know why this is and I am out of time to figure it out.

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

Level 1: Typed in <script>alert("hi");</script> and won.

Level 2: It took me a bit of pondering and looking through the code to realize that a <script> wouldn't be executed because it is inserted after the page loads. Once I got that, I realized that I could put the alert in the onclick attribute of a hyperlink as <a onclick="alert('hi');">, and this worked.
  
Level 3: It took me way too long to realize that the string gets plopped unchanged into an img tag and I can do the exact same thing I did for level 2 by putting `1.jpg' onclick=alert('hi') '` in the URL.

Level 4: At first I was very fixated on putting stuff in the URL because of the previous levels. It took two hints and far too much time for me to figure out that I can just put `',alert(1),'` in the form input.

Level 5: I'm sure I learned about `javascript:` protocol and forgot about it long ago. I would not have solved this one without the hint. I was trying to break out of the href attribute for quite a while.

Level 6: I hosted a file called `alert_inject.js` in this directory and pointed the game to it using a schemeless URI (//raw.githubusercontent.com/nstiff23/389Rfall2019/master/week/11/writeup/alert_inject.js). This gets around the filter that blocks http and https, and looking at the network traffic the site is even requesting the file with the https: protocol, but for some reason it gets back an empty file rather than the script at that location.

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
