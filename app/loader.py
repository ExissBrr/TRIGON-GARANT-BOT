from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from app.utils.misc.config_loader import ConfigLoader
from app.utils.misc.links_loader import LinksLoader

config = ConfigLoader('.env').get_config
links = LinksLoader('.links').get_links

bot = Bot(
    token=config.bot.token,
    parse_mode=ParseMode.HTML,
)

dp = Dispatcher(
    bot=bot,
    storage=MemoryStorage()
)
