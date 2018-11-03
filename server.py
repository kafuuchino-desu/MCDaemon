#!/bin/bash
# -*- coding: utf-8 -*-
# this file includes basic minecraft server class functions
from subprocess import Popen, PIPE
import select
import fcntl, os
import time
import sys
#import mcdplugin #still in develop
from mcdlog import *

def notice():
  print('thanks for using MCDaemon,this software is open source and u can find it here:')
  print('https://github.com/kafuuchino-desu/MCDaemon')
  print('please notice that this software is still in alpha version,things may not work well')
  print('this software is maintained by chino_desu,welcome for your issues and PRs')

class Server(object):
  def __init__(self):
    self.process = Popen('./start.sh', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    flags = fcntl.fcntl(self.process.stdout, fcntl.F_GETFL)
    fcntl.fcntl(self.process.stdout, fcntl.F_SETFL, flags | os.O_NONBLOCK)

  def tick(self):
    try:
      print(self.recv())
      '''
      for singleplugin in plugins.plugins():
        singleplugin.onServerInfo()
      '''
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
      print('forced server to stop')
    except:
      pass
    

if __name__ == "__main__":
  notice()
  log('initalizing plugins') #no use now
  '''
  try:
    import mcdplugin
    plugins = mcdplugin.mcdplugin()
    plugins.initplugins()
  except:
    errlog('error initalizing plugins,printing traceback')
    sys.exit(0)
  '''
  
  server = Server()
  while True:
    try:
      server.tick()
    except SystemExit:
      log('server stopped')
      sys.exit(0)
    except:
      errlog('error ticking MCD')
      server.stop()
      sys.exit(0)
      

