import webapp2

form = """
		<form method="post" action="/testform">
			<input type="password" name="q">
			<input type="submit"> </br></br>
			<input type="checkbox" name="q">
			<input type="submit">
		</form>

"""


class MainPage(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		#self.response.write('Hello, Udacity!')
		self.response.write(form)

class TestHandler(webapp2.RequestHandler):
	def post(self):
		q = self.request.get('q')
		self.response.write(q)
		#self.response.headers['Content-Type'] = 'text/plain'
		#self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage),
															 ('/testform',TestHandler)], 
															debug = True)
