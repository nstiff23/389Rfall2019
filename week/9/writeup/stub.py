#!/usr/bin/env python2

import sys
import struct
import time


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

datactr = 8
timestamp, author, sectionc = struct.unpack("<l8sL", data[datactr:datactr+16])
datactr += 16
if sectionc == 0:
    bork("Not enough sections!")
print("TIME: %s" % time.strftime("%m/%d/%y %H:%M:%S", time.localtime(timestamp)))
print("AUTHOR: %s" % author)
print("SECTIONS: %d" % sectionc)

print("-------  BODY  -------")
filectr = 0

def parse_ascii(slen):
    global datactr
    global filectr
    if slen == 0:
        print("No text to save")
        return
    text = struct.unpack("%ds" % slen, data[datactr:datactr+slen])[0]
    datactr += slen
    with open("carve/%d.txt" % filectr, "w+") as f:
        f.write(text)
    print("Wrote %d bytes ascii to %d.txt" % (slen,filectr))
    filectr += 1

def parse_utf8(slen):
    global datactr
    global filectr
    if slen == 0:
        print("No text to save")
        return
    text = struct.unpack("%ds" % slen, data[datactr:datactr+slen])[0]
    datactr+= slen
    with open("carve/%d.txt" % filectr, "w+") as f:
        f.write(text)
    print("Wrote %d bytes utf-8 to %d.txt" % (slen, filectr))
    filectr += 1

def parse_words(slen):
    global datactr
    global filectr
    if slen == 0:
        print("No words to print")
        return
    words = struct.unpack("=%dL" % slen / 4, data[datactr:datactr+slen])
    datactr += slen
    with open("carve/%d" % filectr, "wb+") as f:
        for word in words:
            f.write(word)
    print("Wrote %d words to %d" % (slen / 4, filectr))
    filectr += 1

def parse_dwords(slen):
    global datactr
    global filectr
    if slen == 0:
        print("No dwords to print")
        return
    dwords = struct.unpack("=%dQ" % slen / 8, data[datactr:datactr+slen])
    datactr += slen
    with open("carve/%d" % filectr, "wb+") as f:
        for word in dwords:
            f.write(word)
    print("Wrote %d dwords to %d" % (slen / 8, filectr))
    filectr += 1

def parse_doubles(slen):
    global datactr
    if slen == 0:
        print("No doubles to print")
        return
    doubles = struct.unpack("=%dd" % slen / 8, data[datactr:datactr+slen])
    datactr += slen
    for double in doubles:
        print(double)

def parse_coord(slen):
    global datactr
    if slen != 16:
        bork("Expected doubles section of length 16, got %d" % slen)
    x, y = struct.unpack("=2d", data[datactr:datactr+16])
    datactr += 16
    print("(%f, %f)" % (x,y))

def parse_ref(slen):
    global datactr
    if slen != 4:
        bork("Expected reference section of length 4, got %d" % slen)
    ref = struct.unpack("%<L", data[datactr:datactr+4])
    if ref[0] > sectionc - 1:
        bork("Reference outside of acceptable range 0-%d: %d" % (sectionc,ref[0]))
    datactr += 4
    print("REF: %d" % ref[0])

def parse_png(slen):
    global datactr
    global filectr
    if slen == 0:
        bork("Empty PNG?")
    header = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
    with open("carve/%d.png" % filectr, "wb+") as f:
        f.write(header)
        for byte in data[datactr:datactr+slen]:
            f.write(byte)
    print("Wrote %d bytes to %d.png" % (slen, filectr))
    filectr += 1
    datactr += slen

def parse_gif87(slen):
    global datactr
    global filectr
    if slen == 0:
        bork("Empty GIF?")
    header = "GIF87a"
    with open("carve/%d.gif" % filectr, "wb+") as f:
        f.write(header)
        for byte in data[datactr:datactr+slen]:
            f.write(byte)
    print("Wrote %d bytes to %d.gif" % (slen, filectr))
    filectr += 1
    datactr += slen

def parse_gif89(slen):
    global datactr
    global filectr
    if slen == 0:
        bork("Empty GIF?")
    header = "GIF89a"
    with open("carve/%d.gif" % filectr, "wb+") as f:
        f.write(header)
        for byte in data[datactr:datactr+slen]:
            f.write(byte)
    print("Wrote %d bytes to %d.gif" % (slen, filectr))
    filectr += 1
    datactr += slen

for i in range(0,sectionc):
    stype, slen = struct.unpack("<LL", data[datactr:datactr+8])
    datactr += 8
    stypes = ""
    if stype < 1 or stype > 10:
        bork("Section %d: bad section type!" % i + 1)
    if stype == 1:
        parse_ascii(slen)
        stypes = "ASCII"
    if stype == 2:
        parse_utf8(slen)
        stypes = "UTF8"
    if stype == 3:
        parse_words(slen)
        stypes = "WORDS"
    if stype == 4:
        parse_dwords(slen)
        stypes = "DWORDS"
    if stype == 5:
        parse_doubles(slen)
        stypes = "DOUBLES"
    if stype == 6:
        parse_coord(slen)
        stypes = "COORDINATES"
    if stype == 7:
        parse_ref(slen)
        stypes = "REFERENCE"
    if stype == 8:
        parse_png(slen)
        stypes = "PNG"
    if stype == 9:
        parse_gif87(slen)
        stypes = "GIF87"
    if stype == 10:
        parse_gif89(slen)
        stypes = "GIF89"
    print("SECTION %d: %s" % (i, stypes))


