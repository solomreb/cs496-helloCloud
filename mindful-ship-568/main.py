#!/usr/bin/env python

import webapp2
import cgi
import pywapi
import string

MAIN_PAGE_HTML = """\
<html>
  <body>
    <h3>Enter your zip to get weather</h3>
    <form action="/weather" method="post">
      <div><input type="text" pattern="\d*" name="zip"></div>
      <div><input type="submit" value="Get Weather"></div>
    </form>
  </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Weather(webapp2.RequestHandler):
    def post(self):
#	weather_com_result = pywapi.get_weather_from_weather_com(self.request.get('zip'))	
        self.response.write('<html><body>Weather.com says it is:<pre>')
#	self.response.write(string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "\n\n"
	self.response.write('</pre></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/weather', Weather),
], debug=True)
