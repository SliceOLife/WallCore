import rumps

class WallSync(rumps.App):
    def __init__(self):
        super(WallSync, self).__init__("WallSync", icon="wallsync.png")
        self.menu = ["Sync Now", "Preferences"]

    @rumps.clicked("Sync Now")
    def sync(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

    @rumps.clicked("Preferences")
    def prefs(self, sender):
        sender.state = not sender.state

if __name__ == "__main__":
    WallSync().run()
