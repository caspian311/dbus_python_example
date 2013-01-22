#!/usr/bin/env python

import dbus
import dbus.service
import dbus.mainloop.glib

import gobject

class Service(dbus.service.Object):
   def __init__(self, message):
      self._message = message

   def run(self):
      dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
      bus_name = dbus.service.BusName("com.example.service", dbus.SessionBus())
      dbus.service.Object.__init__(self, bus_name, "/com/example/service")

      self._loop = gobject.MainLoop()
      print "Service running..."
      self._loop.run()
      print "Service stopped"

   @dbus.service.method("com.example.service.Message", in_signature='', out_signature='s')
   def get_message(self):
      print "  sending message"
      return self._message

   @dbus.service.method("com.example.service.Quit", in_signature='', out_signature='')
   def quit(self):
      print "  shutting down"
      self._loop.quit()



if __name__ == "__main__":
   Service("This is the servie").run()
