import hashlib
import logging
import config
import os
import imp

if(config.APP_DEBUG == True):
  logging.basicConfig(format='%(levelname)s:%(message)s',filename='wallcore.log', level=logging.DEBUG)
else:
  logging.basicConfig(format='%(levelname)s:%(message)s',filename='wallcore.log',level=logging.WARNING)


def MD5(fn):
  with open(file_name, 'rb') as file_to_check:
    data = file_to_check.read()
    md5_returned = hashlib.md5(data).hexdigest()
    return md5_returned

def getRealPath(path):
    return os.path.expanduser(path)

def writeLog(logtype, msg):
  if logtype == 'd':
    logging.debug(msg)
  elif logtype == 'i':
    logging.info(msg)
  elif logtype == 'w':
    logging.warning(msg)
  else:
    logging.warning('Unrecognized logtype given to writeLog function!')

  print(msg)


def loadPlugin(self, uri, absl=False):
	if not absl:
		uri = os.path.normpath(os.path.join(os.path.dirname(__file__), uri))
	path, fname = os.path.split(uri)
	mname, ext = os.path.splitext(fname)

	no_ext = os.path.join(path, mname)

	if os.path.exists(no_ext + '.pyc'):
		try:
			return imp.load_compiled(mname, no_ext + '.pyc')
		except:
			pass
	if os.path.exists(no_ext + '.py'):
		try:
			return imp.load_source(mname, no_ext + '.py')
		except:
			pass
