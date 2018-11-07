#!/bin/bash
# -*- coding: utf-8 -*-
# this file includes basic minecraft server class functions

from subprocess import Popen, PIPE
import select
import fcntl, os
import time
import sys
import traceback
import mcdplugin
from mcdlog import *
import serverinfoparser

def notice():
  print('thanks for using MCDaemon,it\'s open source and u can find it here:')
  print('https://github.com/kafuuchino-desu/MCDaemon')
  print('please notice that this software is still in alpha version,it may not work well')
  print('this software is maintained by chino_desu,welcome for your issues and PRs')
  

class Server(object):
  def __init__(self):
    self.process = Popen('./start.sh', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    flags = fcntl.fcntl(self.process.stdout, fcntl.F_GETFL)
    fcntl.fcntl(self.process.stdout, fcntl.F_SETFL, flags | os.O_NONBLOCK)

  def tick(self):
    try:
      receive=self.recv()
      if receive != '':
        print(receive)
      for line in receive.splitlines():
        if line[11:].startswith('[Server Shutdown Thread/INFO]: Stopping server') or line[11:].startswith('[Server thread/INFO]: Stopping server'): #sometimes this two message will only show one of them
          log('Server stopped by itself.Exiting...')
          sys.exit(0)
        if line[11:].startswith('[Server Watchdog/FATAL]: A single server tick took 60.00 seconds (should be max 0.05)'):
          exitlog('single tick took too long for server and watchdog forced the server off', 1)
          sys.exit(0)
        result = serverinfoparser.parse(line)
        for singleplugin in plugins.plugins:
          try:
            singleplugin.onServerInfo(server, result)
          except:
            errlog('error processing plugin: ' + str(singleplugin),traceback.format_exc())
      time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
      self.stop()
      sys.exit(0) 

  def send(self, data): #send a string to STDIN
    self.process.stdin.write(data)
    self.process.stdin.flush()

  def execute(self, data , tail = '\n'): #puts a command in STDIN with \n to execute
    self.send(data + tail)

  def recv(self, t=0.1): #returns latest STDOUT
    r = ''
    pr = self.process.stdout
    while True:
      if not select.select([pr], [], [], 0)[0]:
        time.sleep(t)
        continue
      r = pr.read()
      return r.rstrip()
    return r.rstrip()

  def cmdstop(self): #stop the server using command
    print(self.recv()) #donnt use tick() here because it can cause loop
    self.send('stop\n')

  def forcestop(self): #stop the server using pclose, donnt use it until necessary
    try:
      pclose(self)
    except:
      raise ForceStopError
      
  def stop(self):
    self.cmdstop()
    try:
      self.forcestop()
      log('forced server to stop')
    except:
      pass
    
  def say(self, data):
    self.execute('say ' + data)

  def tell(self, player, data):
    self.execute('tellraw '+ player + ' {"text":"' + data + '"}')
    

if __name__ == "__main__":
  notice()
  log('initalizing plugins')
  try:
    import mcdplugin
    plugins = mcdplugin.mcdplugin()
  except:
    errlog('error initalizing plugins,printing traceback.')
    sys.exit(0)
  try:
    server = Server()
  except:
    exitlog('failed to initalize the server.', 1, traceback.format_exc())
    sys.exit(0)
  while True:
    try:
      server.tick()
    except (SystemExit,IOError):
      log('server stopped')
      sys.exit(0)
    except:
      errlog('error ticking MCD')
      server.stop()
      sys.exit(0)
      

