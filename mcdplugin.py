#!/bin/bash
# -*- coding: utf-8 -*-
#this file includes basic plugin features

import os
import sys
import traceback
from imp import load_source
from mcdlog import *

class mcdplugin(object):
  def __init__(self):
    self.pluginList = []
    self.plugins = []
    self.initPlugins()
    
  def initPlugins(self): #find plugins and init
    path = 'plugins'
    filelist = os.listdir(path)
    for singleFile in filelist:
      filepath = path + '/' + singleFile
      if os.path.isfile(filepath):
        if singleFile.endswith('.py'):
          self.pluginList.append(singleFile[:-3])
          self.plugins.append(load_source('MCDplugin', filepath))


