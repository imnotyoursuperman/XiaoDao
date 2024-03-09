#https://github/thetrueheavensequal

class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

#ENVIRONMENT VARIABLES

#From BotFather
TOKEN = ""

#From my.telegram.org
API_ID = ""
API_HASH = ""

#Use any bot /id command
OWNER_ID = ""

#Postgres or MySQL database url
SQL_URL = ""

#MongoDB database url
MONGO_URL = ""

#Anything is fine but don't change it after 
DB_NAME = ""

#Support Chat link
SUPPORT_CHAT = ""

#Log Channel ID, reply to a forwarded msg from the channel with /id in Rose Bot
LOG_CHANNEL = ""

# Event logs chat ID and message dump chat ID
EVENT_LOGS = 
MESSAGE_DUMP = 

# List of groups to blacklist
BL_CHATS = []

# User IDs of sudo users, dev users, support users, tiger users, and whitelist users
DRAGON = []  # Sudo users
DEV_USER = []  # Dev users
VERMILION = []  # Support users
TIGERS = []  # Tiger users
TORTOISE = []  # Whitelist users

# Toggle features
ALLOW_CHATS = True
ALLOW_EXCL = True
DEL_CMDS = True
INFOPIC = True

# Modules to load or exclude
LOAD = []
NO_LOAD = []

# Global ban settings
STRICT_GBAN = True

# Temporary download directory
TEMP_DOWNLOAD_DIRECTORY = "./"

class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
