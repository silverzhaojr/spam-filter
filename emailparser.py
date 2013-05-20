#!/usr/bin/python2
# -*- coding: utf-8 -*-

import email
from htmltotext import HTMLToText

class EmailParser():

	"""
	analyze an email file .eml
	"""

	def __init__(self, mail):
		self.mail = mail

	def get_mail_content(self):
		msg = email.message_from_file(self.mail)
		plain_text = ''
		for part in msg.walk():
			if part.get_content_maintype() == 'text':
				content_text = part.get_payload(decode=True).decode(part.get_content_charset())
				if part.get_content_subtype() == 'html':
					plain_text += HTMLToText(content_text).get_text().encode('utf-8')
				else:
					plain_text += content_text.encode('utf-8')
				plain_text += '\n' + '*' * 30 + '\n'
		return plain_text

