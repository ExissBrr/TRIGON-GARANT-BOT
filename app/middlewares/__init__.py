from loguru import logger

from app.loader import dp
from app.middlewares.antiflood_private import AntiFloodMiddleware
from app.middlewares.bun_user import UserBannedMiddleware
from app.middlewares.flood_defender import FloodDefenderMiddleware
from app.middlewares.getting_bot_data import BotDataMiddleware
from app.middlewares.getting_state_data import StateDataMiddleware
from app.middlewares.getting_user_from_db import GettingUserFromDataBaseMiddleware

logger.info(f'Setup middleware')
dp.setup_middleware(FloodDefenderMiddleware())
dp.setup_middleware(GettingUserFromDataBaseMiddleware())
dp.setup_middleware(StateDataMiddleware())
dp.setup_middleware(BotDataMiddleware())
dp.setup_middleware(AntiFloodMiddleware())
dp.setup_middleware(UserBannedMiddleware())
