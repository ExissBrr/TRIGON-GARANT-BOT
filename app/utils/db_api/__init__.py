from loguru import logger

from app.loader import config
from app.utils.db_api.db import db


async def on_startup(drop_all: bool = False):
    # Подключение к базе данных.

    logger.info('Db: Connect to db')
    await db.set_bind(bind=config.database.url)
    from app.utils.db_api.models.categories import ServiceCategory
    from app.utils.db_api.models.deals import Deal
    from app.utils.db_api.models.feedback import Feedback
    from app.utils.db_api.models.messages_for_sending import MessageForSending
    from app.utils.db_api.models.payment_systems import PaymentSystem
    from app.utils.db_api.models.photo_cache import PhotoCache
    from app.utils.db_api.models.sellers import Seller
    from app.utils.db_api.models.start_link import StartLinkHistory
    from app.utils.db_api.models.user_requisites import UserRequisite
    from app.utils.db_api.models.user import User
    from app.utils.db_api.models.user_views import UserView
    if drop_all:
        logger.warning('Db: Drop all')
        await db.gino.drop_all()

    # Создание таблиц.
    logger.info('Db: Create all')
    await db.gino.create_all()
