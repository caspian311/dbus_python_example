#!/usr/bin/env python

import dbus
import dbus.service

import gobject

class Service(dbus.service.Object):
   def __init__(self, message):
      self._message = message

   def run(self):
      bus_name = dbus.service.BusName("com.example.Service", dbus.SessionBus())
      dbus.service.Object.__init__(self, bus_name, "/com/example/Service")

      loop = gobject.MainLoop()
      loop.run()

   @dbus.service.method("com.example.Service", in_signature='', out_signature='s')
   def get_message(self):
      return self._message


if __name__ == "__main__":
   print "Service running..."
   Service("This is the servie").run()
