from __future__ import division
import nltk, re, pprint
from xml.etree.ElementTree import ElementTree
import os


folder="dem"
filename = "KB5.xml"
raw = open('Texts/' + folder + '/' + filename,'r')

proc = ElementTree().parse(raw)
sent = proc.findall("wtext//div//p//s")

full_text = ""

for i,s in enumerate(sent):
	print "Looking at sentence " + str(i)
	text = [word.text for word in s]
	text_str = "".join(filter(None, text))
	full_text += text_str

print "Done"
print full_text[:200]
print "-" * 20
print full_text[-200:]


