import hashlib
import logging
import imp

import config
import os

config = {}

def setupLog():
  if (config['APP_DEBUG'] == True):
      logging.basicConfig(format='%(levelname)s:%(message)s', filename='wallcore.log', level=logging.DEBUG)
  else:
      logging.basicConfig(format='%(levelname)s:%(message)s', filename='wallcore.log', level=logging.WARNING)

def MD5(fn):
    with open(file_name, 'rb') as file_to_check:
        data = file_to_check.read()
        md5_returned = hashlib.md5(data).hexdigest()
        return md5_returned


def getRealPath(path):
    return os.path.expanduser(path)


def writeLog(logtype, msg, sprint=True):
    if logtype == 'd':
        logging.debug(msg)
    elif logtype == 'i':
        logging.info(msg)
    elif logtype == 'w':
        logging.warning(msg)
    else:
        logging.warning('Unrecognized logtype given to writeLog function!')

    if sprint:
        print(msg)


def loadPlugin(uri, absl=False):
    if not absl:
        uri = os.path.normpath(os.path.join(os.path.dirname(__file__), uri))
    path, fname = os.path.split(uri)
    mname, ext = os.path.splitext(fname)

    no_ext = os.path.join(path, mname)

    if os.path.exists(no_ext + '.pyc'):
        try:
            return imp.load_compiled(mname, no_ext + '.pyc')
        except:
          writeLog('w', 'Failed loading plugin: %s', (mname))
    pass


    if os.path.exists(no_ext + '.py'):
        try:
            return imp.load_source(mname, no_ext + '.py')
        except:
          writeLog('w', 'Failed loading plugin: %s', (mname))
    pass


def loadConf(loc):
  global config
  if os.path.isfile(loc):
    execfile(loc, config)
  else:
    print("%s wasn't found.. exiting.." % (loc))
    exit()

  return config
