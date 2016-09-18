#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from random import randint
#import codecs
jer={}
def mixtheregex(*items):
	return '(?:' + '|'.join(items) + ')'

word=r'(?:[\w_\‘\’\'\-\:\\)\(]+)'		#Regex to match words

number=(r'(?:[\+-]?\$?\d+(?:\.\d+)?(?:[eE]-?\d+)?%?)(?![A-Za-z])(?:\\s*/\s*(?:[\+-]?\$?\d+(?:\.\d+)?(?:[eE]-?\d+)?%?)(?![A-Za-z]))?')
											#Regex for numbers(decimals,...)
Punct=r"['\"“”‘’?.!…,:;@/\\]"		#Punctuation	
hashi = r'(?:\#+[\w]+[_\'\-]*[\w]+)'		#Hash regex

mention=r'(?:@[\w_]+)'			#Mention regex
ellipsis=r'(?:\.(?:\s*\.){1,})'		#Ellipsis regex
h_nu=r"""(?:(?:\+?[01][\-\s.]*)?(?:[\(]?\d{3}[\-\s.\)]*)?\d{3}[\-\s.]*\d{4})"""		#Phonenumberregex
brack=r'(?:[(][\w_\'\-\:\\)\(]+[)])'		#Brackets regex
time=(r'\d{1,2}:\d{2}(?::\d{2})?\s*(?:AM|PM|am|pm)?')	#Time regex
other=r'(?:\S)'
br=r'(?:[{][\w_\'\-\:\\)\(]+[}])'		#other kindof bracket regex
has=r'(?:[<][\w_\'\-\:\\)\(]+[>])'			#<> regex
sqb=r'(?:[[][\w_\'\-\:\\)\(]+[]])'			#square bracket regex
quotes=r'(?:["][\w_\'\-\:\\)\(]+["])'
url=r'(?:http[s]?:\//[\w]+.[\w]+(?:[\/])*[\w]+)'
email=r'(?:[a-zA-Z(0-9)]+@[a-z]+.[a-z]{3,3})'
t_re=re.compile((mixtheregex(email,url,word,quotes,number,hashi,mention,ellipsis,Punct,time,h_nu,brack,br,has,other,sqb)),re.VERBOSE|re.I|re.UNICODE)


jm=[]
phi=0
def Tokenize(s):

	s=str(s).decode('utf-8')
	
	tokens=t_re.findall(s)
	
	if tokens!=[]:
		
		jm=[]
		for k in range(len(tokens)):
			for j in range(k,k+phi):
				if k+phi<len(tokens):
					jm.append(tokens[j].encode('utf-8'))
			
			m=" ".join(jm)
			if not jer.has_key(m):
				jer[m]=1
			else:
				jer[m]+=1
			jm=[]	
		
	return tokens
	
	
if __name__=="__main__":
	
	phi=1
	mp=[]
	po=input("Enter n as a limit to ngram")
	for j in open('k2.txt', mode='r').readlines():
			
			mp.append(j)
			l=Tokenize(j)
	#print jer
	su=0
	qe=""
	ml=-99
	for k in jer.keys():
			su+=jer[k]
	for k in jer.keys():
		if jer[k]>ml and k!='':
			ml=jer[k]
			qe=k
			
	print qe
	onk=''
	print "***"
	for jmk in range(30):			#30 iterations to produce a paragraph
		
		for phi in range(2,po+1):			#bigrams to n-grams
		
			jer={}
			ml=-99
			t=[]
			for j in mp:
					
					l=Tokenize(j)
					
			flag=0
			for k in jer.keys():
				#t=k.split()
					
				#print " ".join(t[0:phi-1])
				if list(k.split())[0:phi-1]==list(qe.split()):
					#print k,"sjf",qe
					if jer[k]>ml:
						ml=jer[k]
						qe=k
						#print qe		
						flag=1
			if flag==0:
				onk=onk+' '+ qe
				qe=jer.keys()[randint(0,len(jer.keys())-1)]
				print onk
		"""		
		mko=qe.split()
		#print mko
		onk=onk+qe
		qe="".join(mko[-1])
		"""
		
	print "=====Sentences Generated======"	
	print onk
