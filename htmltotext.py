#!/usr/bin/python2
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

class _MyHTMLParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.text = ''
		self.hide_output = False

	def handle_starttag(self, tag, attrs):
		if tag in ('script','style'):
			self.hide_output = True

	def handle_endtag(self, tag):
		if tag in ('script','style'):
			self.hide_output = False

	def handle_data(self, data):
		if data and not self.hide_output:
			self.text += data

	def get_text(self):
		return self.text

class HTMLToText():

	"""
	extract plain text from a html document
	"""

	def __init__(self, html):
		self.html = html
		self.parser = _MyHTMLParser()

	def get_text(self):
		self.parser.feed(self.html)
		self.parser.close()
		return self.parser.get_text()

