#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import email
from htmltotext import HTMLToText

fp = open(sys.argv[1], "r")
msg = email.message_from_file(fp)
fp.close()

"""
subRaw = msg.get('subject')
h = email.Header.Header(subRaw)

subTupleList = email.Header.decode_header(subRaw)
subStr = subTupleList[0][0]
subCharset = subTupleList[0][1]
print "subject is :", subStr.decode(subCharset)

fromRaw = msg.get('from')
fromStr = email.Utils.parseaddr(fromRaw)[1]
print "from is :", fromStr

toRaw = msg.get('to')
toStr = email.Utils.parseaddr(toRaw)[1]
print "to is :", toStr
print msg.get_content_charset()
#print msg.get_payload(decode=True)
print msg.get_payload()
"""

for par in msg.walk():
	if par.get_content_maintype() == "text":
		print "*" * 30
		content_text = par.get_payload(decode=True).decode(par.get_content_charset()).encode('utf-8')
		if par.get_content_subtype() == "html":
			print HTMLToText(content_text.decode('utf-8')).get_text().encode('utf-8')
		else:
			print content_text

