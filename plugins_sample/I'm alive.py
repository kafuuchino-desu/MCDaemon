from time import sleep

def onServerStartup(server):
  while True:
    server.say('I'm alive!')
    sleep(10)
