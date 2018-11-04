import traceback
PREFIX='[MCDaemon]:'

def log(data):
  print(PREFIX + data)

def errlog(data):
  print(PREFIX + data)
  traceback.print_exc()

def exitlog(data, crit=0, traceback=0):
  if crit == 0:
    print(PREFIX + data)
    print(PREFIX + 'Exiting...')
  if crit == 1:
    print(PREFIX + 'Critical Error Occured')
    print(PREFIX + 'Reason:' + data)
    if traceback == 1:
      traceback.print_exc()
  
