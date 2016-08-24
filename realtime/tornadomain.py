#!/usr/bin/env python

import json
import os
import tornado.ioloop
import tornado.web

current_time = 0
active_users = {}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        pass
    

class SetTimeHandler(tornado.web.RequestHandler):
    # posting here will set the time to specified value and clear the state
    def post(self):
        data = json.loads(self.request.body)

        if 'time' not in data:
            raise tornado.web.HTTPError(400)

        current_time = data['time']


class EventHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)

        if 'time' not in data or 'user_id' not in data:
            raise tornado.web.HTTPError(400)
        



DIR_NAME = os.path.dirname(__file__)

tornado_settings = {
    'static_path': os.path.join(DIR_NAME, 'static'),
    'template_path': os.path.join(DIR_NAME, 'templates'),
}

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/settime", SetTimeHandler),
        (r"/event", EventHandler),
    ], **tornado_settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()



