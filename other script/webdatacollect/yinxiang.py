#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from evernote.api.client import *
import evernote.edam.type.ttypes as Types


def writeNote(title,content):
	dev_token = 'S=s1:U=9396c:E=162fbfbba33:C=15ba44a8d68:P=1cd:A=en-devtoken:V=2:H=ef70187137ae3950b5a4055c72a8ac1e'
	client = EvernoteClient(token=dev_token)
	userStore = client.get_user_store()
	user = userStore.getUser()
	print('登录名:',user.username)

	noteStore = client.get_note_store()
	notebooks = noteStore.listNotebooks()
	i = 0
	for n in notebooks:
		i+=1
		print('notebook[%s]:%s' %(i,n.name))
		#print('notebooks[%s]:%s' %(i,n.name))

	# 创建一个笔记
	# noteStore = client.get_note_store()
	note = Types.Note()
	note.title = title
	note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
	note.content += '<en-note>'+content+'</en-note>'
	note = noteStore.createNote(note)
	
writeNote('向林海','向林海的工作笔记')	