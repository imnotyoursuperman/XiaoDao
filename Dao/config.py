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


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
