import webapp2
import string

form = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>ROT13</title>
	</head>
	<body>
		<form method='post'>
			<H1> Enter some text to ROT13:</H1>
			
			<textarea name="text" rows=10 cols=80 >%(entered_text)s</textarea>

			<br><br>
			<input type='submit' value='Submit'>
		</form>
	</body>
</html>
"""

def createAFinalMatch(string_in):
	string_in_list = list(string_in)
	string_in_list_combo = [string_in[x + 13 - 26] for x in range(len(string_in))]
	string_in_final = zip(string_in_list, string_in_list_combo)
	return string_in_final

str_match = createAFinalMatch(string.lowercase) + createAFinalMatch(string.uppercase)

def transformText(text_in):
	text_ret = text_in
	for (letter_in, letter_out) in str_match:
		print letter_in + " --> " + letter_out + "\n"
		text_ret = text_ret.replace(letter_in, letter_out)
	return text_ret



class MainPage(webapp2.RequestHandler):

	def write_form(self, text_out=""):
		self.response.out.write(form % {'entered_text': text_out})				


	def get(self):
		self.write_form()


	def post(self):
		user_text = self.request.get('text')
		self.write_form(transformText(user_text))

#class MainPage(webapp2.RequestHandler):
#	def write_form(self, error="", month="", day="", year=""):
#		self.response.out.write(form % {'error': error,
#																		'month': month,
#																		'day': day,
#																		'year': year})
#	def get(self):
#		self.write_form()
		

#	def post(self):
#		user_month = self.request.get('month')
#		user_day = self.request.get('day')
#		user_year = self.request.get('year')
		
#		month = valid_month(user_month)
#		day = valid_day(user_day)
#		year = valid_year(user_year)

#		if not (month and day and year):
			# run to the form again
#			self.write_form("That doesn't look right to me my friend", user_month, user_day, user_year)
#		else:
#			self.redirect("/thanks")

#class ThanksHandler(webapp2.RequestHandler):
#	def get(self):
#		self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

