# This script reads the file and does some manipulations to the text.
#Initiated 20121222 2051
#1. Program reads a file, breaks each line into words, stripes whitespaces and punctuation from words and converts them #to lowercase.
#-> Use whitespace attribute from string module.

from sys import argv
from string import (lowercase,digits)

script, filename = argv

def keepOnlyValidChars(string, valid_string):
	""" Keeps only characters  that are included in the validation string."""
	final_string = ''
	for i in string:
		if i in valid_string:
					final_string += i
		else:
			pass
	return final_string

def deleteEmpyElements(array_of_words):
	final_array = []
	for item in array_of_words:
		if item in (""," "):
			pass
		else:
			final_array.append(item)
	return final_array
# 1. Read in the text

try:
	file = open(filename)
	lines = file.readlines()
	print "Number of lines: %s" %str(len(lines))
	file.close()
	# new_lines - dictionary that will contain clean text by line
	new_lines = {}
	condition =  lowercase + digits + " "
	key = 0
	for line in lines:
		clean_line = keepOnlyValidChars(line.lower(), condition)
		new_lines[key] = deleteEmpyElements(clean_line.split(' '))
		key += 1
	print new_lines
except IOError as e:
	print "Can not find a file %r " %filename
	print "I/O error({0}): {1}".format(e.errno, e.strerror)

