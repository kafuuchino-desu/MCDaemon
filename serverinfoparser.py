#!/bin/bash
# -*- coding: utf-8 -*-
#this file is for handleing server info and parsing those info into a object

import re

class parseResult(object):
  def __init__(self):
    self.hour = 0
    self.min = 0
    self.sec = 0
    self.sourceProcess = ''
    self.isPlayer = 0
    self.player = ''
    self.content = ''

def parse(line):
  result = parseResult()
  result.hour = line[1:3]
  result.min = line[4:6]
  result.sec = line[7:9]
  result.sourceProcess = re.search(r'[[](.*?)[]]', line[11:]).group()[1:-1]
  if (result.sourceProcess == 'Server thread/INFO') and (line[33:].startswith('<')):
    player = re.search(r'[<](.*?)[>]', line[33:]).group()[1:-1]
    if player != '':
      result.isPlayer = 1
      result.player = player
      content = line[33:].replace('[' + result.sourceProcess + ']: ', '' , 1)
      result.content = content.replace('<' + result.player + '> ', '', 1)
  else:
    result.isPlayer = 0
    result.player = ''
    result.content = line[11:].replace('[' + result.sourceProcess + ']: ' , '' , 1)
  return result
