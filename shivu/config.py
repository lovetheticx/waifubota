class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6216046291"
    sudo_users = "6216046291"
    GROUP_ID = -1001892105484
    TOKEN = "6574068893:AAFZ3wukYpLmMRzXo8OzKQLVG6bFBQ1s250"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "AniverseGroup"
    UPDATE_CHAT = "AniverseGroup"
    BOT_USERNAME = "AniverseWaifubot"
    CHARA_CHANNEL_ID = "-1001892105484"
    api_id = 29668491
    api_hash = "84feb2e86bc3fa3b0b9bc1e3a3428177"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
