#!/usr/bin/python2
# -*- coding: utf-8 -*-

import re
from HTMLParser import HTMLParser

class _MyHTMLParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.buf = []
		self.hide_output = False

	def handle_starttag(self, tag, attrs):
		if tag in ('script','style'):
			self.hide_output = True

	def handle_endtag(self, tag):
		if tag in ('script','style'):
			self.hide_output = False

	def handle_data(self, text):
		if text and not self.hide_output:
			self.buf.append(text)

	def get_text(self):
		return re.sub('\s+', '\n', ''.join(self.buf))

class HTMLToText():

	"""
	extract plain text from a html document
	"""

	def __init__(self, html):
		self.html = html
		self.parser = _MyHTMLParser()

	def get_text(self):
		try:
			self.parser.feed(self.html)
			self.parser.close()
		except HTMLParseError:
			pass
		return self.parser.get_text()

