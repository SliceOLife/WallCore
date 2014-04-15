from dropboxService import auth
from dropboxService import sync

import argparse
import glob
import config
from modules.utils import writeLog


# Parse arguments
parser = argparse.ArgumentParser(description='WallCore command line options')
parser.add_argument('-d', help='Debug switch for development', action='store_true')
args = parser.parse_args()


# Load-up (default) plugins
pluginsAvailable = glob.glob("plugins/*.py")
pluginsLoaded = {}
for plugin in pluginsAvailable:
  writeLog('i', 'Found plugin: %s' % (plugin))

# Dropbox auth
if args.d:
  syncService = sync(config.DROPBOX_DEBUGKEY)
else:
  authService = auth(config.DROPBOX_KEY, config.DROPBOX_SECRET)
  print("Please navigate to: " + authService.getAuthURL())
  user_code = raw_input("Please enter Dropbox' response code")
  flowAuth = authService.finishFlow(user_code)
  writeLog('d', flowAuth)
  syncService = sync(flowAuth)

uid = syncService.getUserInfo()['uid']
name = syncService.getUserInfo()['display_name']
writeLog('i', "Logged into %s[%s]'s Dropbox " % (name, uid))
writeLog('i', 'Using WallCore v%s' % (config.APP_VER))
