#! /usr/bin/python

import os.path
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import RPi.GPIO as GPIO
import socket

#Initialize Raspberry PI GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(17, True)
GPIO.output(27, True)
GPIO.output(22, True)
      
#RES Folder Paths
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "RES_templates"),
    static_path = os.path.join(os.path.dirname(__file__), "RES_static")
    )

#RES Server port
PORT = 8080


class MainHandler(tornado.web.RequestHandler):
  def get(self):
     print ("[HTTP](MainHandler) User Connected.")
     self.render("index.html")

    
class WSHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    print ('[WS] Connection was opened.')
 
  def on_message(self, message):
    print ('[WS] Incoming message:'), message
    
    if message == "on_g":
      GPIO.output(17, False)
      GPIO.output(27, False)
      GPIO.output(22, False)
      print ('Motor On')
      
    if message == "off_g":
      GPIO.output(17, True)
      GPIO.output(27, True)
      GPIO.output(22, True)
      print ('Motor Off')

  def on_close(self):
    print ('[WS] Connection was closed.')


application = tornado.web.Application([
  (r'/', MainHandler),
  (r'/ws', WSHandler),
  ], **settings)
 


if __name__ == "__main__":
    try:
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(PORT)
        main_loop = tornado.ioloop.IOLoop.instance()

        print ("RES Server started")
        main_loop.start()

    except:
        print ("Exception triggered - RES Server stopped.")
        GPIO.cleanup()

#End of Program
