import dropbox
import os.path

class auth:

  flow = None

  def __init__(self, appkey, appsecret):
    global flow
    self.app_key = appkey
    self.app_secret = appsecret
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(self.app_key, self.app_secret)


  def getAuthURL(self):
    global flow
    auth_url = flow.start()
    if auth_url:
      return auth_url


  def finishFlow(self, code):
    global flow
    access_token, user_id = flow.finish(code)
    return access_token


class sync:

  client = None
  def __init__(self, access_token):
    global client
    self.access_token = access_token
    self.debug = 1
    client = dropbox.client.DropboxClient(access_token)


  def getUserInfo(self):
    global client
    accountInfo = client.account_info()
    if accountInfo:
      return accountInfo

  def syncWallpaper(self, initLoc):
    global client
    if os.path.isfile(initLoc):
      f = open(initLoc, 'rb')
      resp = client.put_file('/wall_latest.png', f)

      if resp:
        return True
      else:
        return False
