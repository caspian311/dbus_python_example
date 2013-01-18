#!/usr/bin/env python

from ldtp import *
import glib
import os
import sys
import dbus
import dbus.mainloop.glib
import json
import time

class Client():
   DEFAULT_SLEEP_AMOUNT = 0.2

   def __init__(self):
      dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
      bus = dbus.SessionBus()
      service = bus.get_object('com.example.Service', "/com/example/Service")
      self._method = service.get_dbus_method('get_message', 'com.example.Service')

   def run(self):
      print "Mesage from service:", self._method()

if __name__ == "__main__":
   Client().run()
