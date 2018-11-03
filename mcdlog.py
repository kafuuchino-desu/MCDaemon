import traceback

def log(data):
  prefix='[MCDaemon]:'
  print(prefix + data)

def errlog(data):
  prefix='[MCDaemon]:'
  print(prefix + data)
  traceback.print_exc()
