#!/bin/bash
# -*- coding: utf-8 -*-
#this file includes the mcgit object

import configparser
import json
from gittle import Gittle
from mcdlog import *

helpmsg = '''------thanks for use mcgit------
those are basic functions:
!!mcg help -show this help message
!!mcg commit list -show a list of commits available
!!mcg commit [info] -reboot the server and commit current world
!!mcg rollback [commit] -reboot the server and rollback the world to a commit
!!mcg branch now -show which branch the server is on now
!!mcg branch list -show all branches avaliable
!!mcg branch change [branch] -reboot and change the server to another branch
(the world now will commit with info 'changebranch')
!!mcg branch delete [branch] -delete a branch
(if you are deleting the branch server is running on,the server will load master branch after reload)
!!mcg merge [branch] -merge the branch to master
--------------------------------'''

class mcgit(object):
  def __init__(self):
    conf =  configparser.ConfigParser()
    try:
      conf.read('mcgit.properties')
    except:
      log('mcgit failed to read a config file.Creating a new one')
      conf.add_section('savePath')
      conf.set('savePath', 'path', './mcgit')
    #try:
      #saveRepo = Gittle.init(conf.get('savePath','path'))
    #except:
      #exitlog('failed to init world repo...', 1, traceback.format_exc())

  def onServerInfo(self, server, info):
    if (info.isPlayer == 0):
      pass
    else:
      if info.content.startswith('!!mcg'):
        args = info.content.split(' ')
        if (args[1] == 'help'):
          for line in helpmsg.splitlines():
            server.tell(info.player, line)
          
            

