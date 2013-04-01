'''
ElementTree test
'''

from __future__ import division
import nltk, re, pprint
from xml.etree.ElementTree import ElementTree
import os



def convertFromXMLtoStr(fileIn, path):
	'''
		Takes a file in XML format, unpacks it and saves raw text as a string.
	'''
	proc = ElementTree().parse(fileIn)
	### grab all the text from the file
	sentence = proc.findall(path)
	full_text = ""
	for i,s in enumerate(sentence):
		print "Looking at sentence " + str(i)
		text = [word.text for word in s]
		text_str = "".join(filter(None, text))
		full_text += " " + text_str
	return full_text



def saveTxtFiles(folder, sent_path_p):
	filenames = os.listdir(os.getcwd() + "/Texts/" + folder)
	for filename in filenames:
		if filename[-3:] == "xml":
			try:	
				raw = open('Texts/' + folder + '/' + filename,'r')
				out_file = 'TextsOutput/' + folder + '/' + filename[:-4] + ".txt"
				### print filename + " puts " + out_file
				try:
					print filename
					output = open(out_file, "w")
					raw_str = convertFromXMLtoStr(raw, path=sent_path_p)
					output.write(raw_str.encode('utf-8'))
					output.close()
				except IOError as e:
					print "Can not create a file %r" %out_file		
				raw.close()	
				print "OK"
			except IOError as e:
				print "Can not find a file %r" %filename
				print "I/O error({0}) : {1}".format(e.errno, e.strerror)


### proc.getchildren()

print "\nGot here"


saveTxtFiles(folder = "aca", sent_path_p='wtext//div//p//s')
saveTxtFiles(folder = "dem" , sent_path_p='stext//div//u//s')
saveTxtFiles(folder = "fic" , sent_path_p='wtext//div//p//s')
saveTxtFiles(folder = "news" , sent_path_p='wtext//div//p//s')

print "\nDone"
