#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('heyeyeyeyeyeyeey!')


class TestHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('test!')

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler), webapp2.Route('/test', TestHandler)
], debug=True)
