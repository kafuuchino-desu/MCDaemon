def onServerInfo(server, info):
  if (info.isPlayer == 0):
    pass
  else:
    if info.content.startswith('!!restart'):
      server.say('restarting')
      server.stop()
      server.start()
