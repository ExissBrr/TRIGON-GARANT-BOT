from sqlalchemy import Column, BigInteger, Sequence, String, Integer

from app.utils.db_api.db import BaseModel


class ServiceCategoryType:
    DRIVING_SCHOOL_OR_LAW = 'Автошкола,права'
    ALCOHOL_OR_TOBACCO = 'Алкоголь, табак'
    ANONYMIZERS = 'Анонимайзеры'
    DATABASES_OR_LOGS = 'Базы данных, логи'
    BANK_CARDS = 'Банковские карты'
    BOMBERS_OR_CALLS_OR_SPAM_MAILING = 'Бомберы,спам-рассылка'
    HACKING_SOCIAL_NETWORKS_OR_MAILS = 'Взлом соцсетей,почт'
    GRANDPA = 'Дедики'
    DETECTIVES = 'Детективы'
    DESIGN_OR_RENDERING = 'Дизайн,отрисовка'
    DROP_SKIP_SERVICE = 'Дроп-скупсервис'
    DUPLICATE_DOCUMENTS = 'Дубликаты документов'
    FOOD = 'Еда'
    LOANS = 'Займы'
    GAME_ITEMS = 'Игровые предметы'
    TRACKING_INFORMATION = 'Информация об отслеживании'
    COSMETICS = 'Косметика'
    WALLETS = 'Кошельки'
    LENDING = 'Кредитование'
    CRYPTOCURRENCY = 'Криптовалюта'
    MEDICINE = 'Медицина'
    MERCH = 'Мерчи'
    BOOST_SUBSCRIBERS = 'Накрутка подписчиков'
    CHEAT = 'Накрутка'
    CASH_OUT = 'Обнал'
    HOTELS_AND_LEISURE = 'Отели,Отдых'
    PRANK_AND_RINGTONES = 'Пранки и Прозвоны'
    BREAKING_THROUGH = 'Пробив'
    PROGRAMMING_AND_DEVELOPMENT = 'Программирование/Разработка'
    SOFTWARE_OR_PROGRAMMING = 'ПO,софты'
    PROMO_CODES_OR_DISCOUNTS_OR_VOTES_OR_CASHBACK = 'Промокоды,скидки,кэшбэк'
    REWARDS = 'Реварды'
    REFUNDS = 'Рефаунд'
    SPORTSMEN = 'Спортики'
    SIM_CARDS_OR_TARIFFS = 'Сим-карты,тарифы'
    INSURANCE = 'Страхование'
    SCHEMES_OR_TRAINING = 'Схемы,обучения'
    TAXI = 'Такси'
    TECHNICS = 'Техника'
    TRAFFIC = 'Трафик'
    LEGAL_SERVICES = 'Юридические Услуги'


class ScamStatusType:
    ACTIVE: str = 'active'
    CLOSED: str = 'closed'
    REJECTED: str = 'rejected'


class ScamComplain(BaseModel):
    __tablename__ = "ScamComplains"
    id: int = Column(BigInteger, Sequence("scam_counter"), primary_key=True)
    status: str = Column(String, default=ScamStatusType.ACTIVE)
    scam_victim_id: int = Column(BigInteger)
    scam_user_id: int = Column(BigInteger)
    scam_user_username: str = Column(String, default='-')
    scam_user_fullname: str = Column(String)
    description: str = Column(String(200), default='-')
    photo_proofs: str = Column(String, default='-')
    amount: int = Column(Integer, default=0)
    extra_accounts_id: str = Column(String, default='-')
    extra_accounts_username: str = Column(String, default='-')
    scam_category: str = Column(String)

    def get_accounts_id(self):
        if self.extra_accounts_id == "-":
            return []
        return list(map(int, self.extra_accounts_id.split()))

    def get_photo_proofs(self):
        if self.photo_proofs == '-':
            return []
        return self.photo_proofs.split()

    def get_accounts_username(self):
        if self.extra_accounts_username == "-":
            return []
        return list(map(int, self.extra_accounts_username.split()))

    async def update_status(self, new_status):
        await self.update_data(status=new_status)
        return new_status
