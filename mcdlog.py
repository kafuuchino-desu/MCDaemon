import traceback
PREFIX='[MCDaemon]:'

def log(data):
  print(PREFIX + data)

def errlog(data):
  print(PREFIX + data)
  traceback.print_exc()

def exitlog(data, crit=0, traceback=''):
  if crit == 0:
    print(PREFIX + data)
    print(PREFIX + 'Exiting...')
  if crit == 1:
    print(PREFIX + 'Critical Error Occured')
    print(PREFIX + 'Reason:' + data)
    if traceback != '':
      print(traceback)
    print(PREFIX + 'Exiting...')

  
