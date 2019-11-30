# Writeup 1 - Web I

Name: Nathan Stiff
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

Level 1: Typed in <script>alert("hi");</script> and won.

Level 2: It took me a bit of pondering and looking through the code to realize that a <script> wouldn't be executed because it is inserted after the page loads. Once I got that, I realized that I could put the alert in the onclick parameter of a hyperlink as <a onclick="alert('hi');">, and this worked.
  
Level 3: It took me way too long to realize that the string gets plopped unchanged into an img tag and I can do the exact same thing I did for level 2 by putting `1.jpg' onclick=alert('hi') '` in the URL.

Level 4: At first I was very fixated on putting stuff in the URL because of the previous levels. It took two hints and far too much time for me to figure out that I can just put `',alert(1),'` in the form input.

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
