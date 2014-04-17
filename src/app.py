import argparse
import glob

from dropboxService import auth
from dropboxService import sync
from modules.utils import writeLog, loadPlugin, loadConf, setupLog



# Parse arguments
parser = argparse.ArgumentParser(description='WallCore command line options')
#parser.add_argument('-d', help='debug switch for development', action='store_true')
parser.add_argument('-conf', help='set config file to load', dest='conf')
args = parser.parse_args()

if args.conf is not None:
  config = loadConf(args.conf)
else:
  config = loadConf('default.conf')

# Setup logging
setupLog()

# Load-up (default) plugins
# pluginsAvailable = glob.glob("plugins/*.py")
# pluginsLoaded = {}
# for plugin in pluginsAvailable:
#     writeLog('i', 'Found plugin: %s' % (plugin))
#     loadPlugin(plugin)

# Dropbox auth
if config['DROPBOX_DEBUGKEY'] is not None:
    syncService = sync(config['DROPBOX_DEBUGKEY'])
else:
    authService = auth(config['DROPBOX_KEY'], config['DROPBOX_SECRET'])
    print("Please navigate to: " + authService.getAuthURL())
    user_code = raw_input("Please enter Dropbox' response code")
    flowAuth = authService.finishFlow(user_code)
    writeLog('d', flowAuth)
    syncService = sync(flowAuth)

uid = syncService.getUserInfo()['uid']
name = syncService.getUserInfo()['display_name']
writeLog('i', "Logged into %s[%s]'s Dropbox " % (name, uid))
writeLog('i', 'Using WallCore v%s' % (config['APP_VER']))
