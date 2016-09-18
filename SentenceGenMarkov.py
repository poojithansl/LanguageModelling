#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import random
#import codecs
def mixtheregex(*items):
	return '(?:' + '|'.join(items) + ')'
#word_re=(r'(?:[a-zA-Z0-9]+[\'-]?[a-zA-Z]+[a-zA-Z0-9]*)|(?:[a-zA-Z0-9\]*[a-zA-Z]+[\'-]?[a-zA-Z0-9]+)')
#word_re=r'(?:[\w\‘\’\'\-\:]*)'     #wordswith'_-
word_re=r'(?:[\w_\‘\’\'\-\:\\)\(]+)'
#word_re=r"""(?:[\w]*[\w\'\-_]*[\w]*)"""
number_re=(r'(?:[\+-]?\$?\d+(?:\.\d+)?(?:[eE]-?\d+)?%?)(?![A-Za-z])(?:\\s*/\s*(?:[\+-]?\$?\d+(?:\.\d+)?(?:[eE]-?\d+)?%?)(?![A-Za-z]))?')
k_re=r'(?:([0-9]*[,]*[0-9]*)*)'
Punct_re=r"['\"“”‘’?.!…,:;@/\\]"
hash_re = r'(?:\#+[\w]+[_\'\-]*[\w]+)'
wo_re=r'(?:[a-zA-Z]+[\'][a-zA-Z]*)'
#ment_re=r'(?:@[\w]+[:]?)'
#ell_re=r'(?:\.\.+)'
ment_re=r'(?:@[\w_]+)'
ell_re=r'(?:\.(?:\s*\.){1,})'
urls_re=r'@\w{1,15}|(?:(?:https?://[A-Za-z0-9\.]+)|(?:(?:www\.)?[A-Za-z0-9]+\.(?:[\w]+)'
brac_re=r'(?:[(][\w_\'\-\:\\)\(]+[)])'
sq_re=r'(?:[[][\w_\'\-\:\\)\(]+[]])'
other=r'(?:\S)'
br=r'(?:[{][\w_\'\-\:\\)\(]+[}])'
has=r'(?:[<][\w_\'\-\:\\)\(]+[>])'
time=(r'\d{1,2}:\d{2}(?::\d{2})?\s*(?:AM|PM|am|pm)?')
phone_nu=r"""(?:(?:\+?[01][\-\s.]*)?(?:[\(]?\d{3}[\-\s.\)]*)?\d{3}[\-\s.]*\d{4})"""
h_nu=r"""
	(?:
		  (?:            # (international)
				\+?[01]
						[\-\s.]*
							  )?            
			  (?:            # (area code)
					[\(]?
							\d{3}
									[\-\s.\)]*
										  )?    
				  \d{3}          # exchange
					  [\-\s.]*   
						  \d{4}          # base
							)"""
quotes_re=r'(?:["][\w_\'\-\:\\)\(]+["])'
#urls_re=r'(^|[\s.:;?\-\]<\(])(https?://[-\w;/?:@&=+$\|\_.!~*\|'()\[\]%#,☺]+[\w/#](\(\))?)(?=$|[\s',\|\(\).:;?\-\[\]>\)])'
#ep = r'(?:\"“”‘’«»{}\\(\\)\\[\\]\\*&)'
url_re=r'(?:http[s]?:\//[\w]+.[\w]+(?:[\/])*[\w]+)'
email_re=r'(?:[a-zA-Z(0-9)]+@[a-z]+.[a-z]{3,3})'
t_re=re.compile((mixtheregex(email_re,url_re,word_re,quotes_re,number_re,hash_re,ment_re,ell_re,Punct_re,time,h_nu,brac_re,br,has,other)),re.VERBOSE|re.I|re.UNICODE)
"""
def SentenceT(s):
	if s=='\n':
		return True
"""


n=0
class MarkovChain:

	def __init__(self):
		self.memory = {}

	def _learn_key(self, key, value):
		if key not in self.memory:
			self.memory[key] = []

		self.memory[key].append(value)

	def learn(self, text):
		tokens = Tokenize(text)
		for i in range(len(tokens)):
			ngrams=()
			for j in range(i,i+n):
				if i+n<len(tokens):
					ngrams=ngrams+(tokens[j],)
					print ngrams
			self._learn_key(ngrams, tokens[i+n].encode('utf-8'))

	def _next(self, current_state):
		next_possible = self.memory.get(current_state)

		if not next_possible:
			next_possible = self.memory.keys()

		return random.sample(next_possible, 1)[0]

	def babble(self, amount, state=''):
		if not amount:
			return state

		next_word = self._next(state)
		#print self.babble(amount - 1, next_word)
		return tuple((state,) +tuple(' ')+ tuple(self.babble(amount - 1, next_word)))
mar=MarkovChain()
	
def Tokenize(s):
	"""
	if SentenceT(s):
		print "a"
	"""
	#print s
	#print "-------"
	
	
	#print "============"
	s=str(s).decode('utf-8')
	#print s
	tokens=t_re.findall(s)
	#print tokens
	"""
	for k in tokens:    
		print k.encode('utf-8')
		#print tokens.encode('utf-8')
	"""
	return tokens
	#print tokens
	
if __name__=="__main__":
	#f=codecs.open('test.txt',encoding='utf-8')
	#for j in f:
	lena=input("n")
	simo=input("amount")
	for j in open('k2.txt', mode='r').readlines():
			#with open('test.txt',encoding='utf-8') as f:
			#l=Tokenize(j)
			mar.learn(j)
	l=list(mar.babble(simo,''))
	nmh=[]
	for t in l:	
		if t!=() and t!='':
			nmh.append(t)
	print "".join(nmh)

