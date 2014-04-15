WallCore
========

WallCore is a Python utility to keep your wallpapers in sync across multiple devices via Dropbox


### Configuration
In development, configuration is done by creating a config.py with the following variables:

```python
APP_DEBUG = True # or false if you have no access token(debugkey) yet.
APP_VER = '0.1.1'
DROPBOX_KEY = ''
DROPBOX_SECRET = ''
DROPBOX_DEBUGKEY = ''
```

### What is it?

In the end, WallCore should hopefully provide a nice and easy way to sync your desktop wallpaper between your OS X, Windows and Linux machines, detecting changes as you change it one system, then automatically changing it on the other, all powered by Dropbox in the back.
