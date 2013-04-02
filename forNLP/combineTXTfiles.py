
from __future__ import division
import nltk, re, pprint
from xml.etree.ElementTree import ElementTree
import os


def combineTxtFilesIntoOne(folder):
	filenames = os.listdir(os.getcwd() + "/TextsOutput/" + folder)
	try:
		out_file = open("full_" + folder + ".txt", "w")
		### out_file.write()

		for filename in filenames:
			print filename
			
			try:
				text = open('TextsOutput/' + folder + '/' + filename, 'r')
				out_file.write(text.read() + " ")
				print 'Put some text'
				text.close()
			except IOError as e:
				print "Can not open a file %r" %filename
		
		out_file.close()
		
	except IOError as e:
		print "Can not create a file %r" %out_file
		
	

	

combineTxtFilesIntoOne("aca")
raw_input('Done aca')
combineTxtFilesIntoOne("dem")
raw_input('Done dem')
combineTxtFilesIntoOne("fic")
raw_input('Done fic')
combineTxtFilesIntoOne("news")
raw_input('Done news')

	


	

