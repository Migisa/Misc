import string


def createAFinalMatch(string_in):
	string_in_list = list(string_in)
	string_in_list_combo = [string_in[x + 13 - 26] for x in range(len(string_in))]
	string_in_final = zip(string_in_list, string_in_list_combo)
	return string_in_final

str1 = string.lowercase
str2 = string.uppercase

str_match = createAFinalMatch(str1) + createAFinalMatch(str2)
print str_match


for (i,z) in str_match:
	print i + " --> " + z

