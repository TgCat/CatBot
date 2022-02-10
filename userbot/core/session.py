import sys

#from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config
from .client import CatUserBotClient

__version__ = "2.10.6"



if Config.STRING_SESSION:
    session = StringSession(str(Config.STRING_SESSION))
else:
    session = "catuserbot"

try:
    catub = CatUserBotClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        app_version=__version__,
        auto_reconnect=True,
        connect_retries=None,
    )
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()


catub.tgbot = tgbot = CatUserBotClient(
    session="CatTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    app_version=__version__,
    auto_reconnect=True,
    connect_retries=None,
).start(bot_token=Config.TG_BOT_TOKEN)
