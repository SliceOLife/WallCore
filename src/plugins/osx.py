import sqlite3
import utils


def getWallpaper():
    db = sqlite3.connect(dbPath)
    cursor = db.cursor()

    # Get current Mac wallpaper from SQLite DB.
    cursor.execute('''SELECT value FROM data''')
    rowSet = cursor.fetchall()
    db.close()

    wpHolder = []
    # Make sure we get the one with a wallpaper in it
    for row in rowSet:
        if os.path.isfile(utils.getRealPath(row[0])):
            wpHolder.append(utils.getRealPath(row[0]))

    utils.writeLog('d', 'Found %s wallpaper links in DB!', len(wpHolder))
    for item in enumerate(wpHolder):
        utils.writeLog('i', 'Got wallpaper: %s', item)
    wallVar = wpHolder[1]
    return wallVar
