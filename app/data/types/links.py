from dataclasses import dataclass


@dataclass
class MiscLinks:
    pass


@dataclass
class PhotoLinks:
    photo: str


@dataclass
class VideoLinks:
    read_rules: str
    window_windows_xp: str


@dataclass
class DocumentLinks:
    doc: str


@dataclass
class TelegraphLinks:
    bot_rules: str
    bot_instructions: str


@dataclass
class Links:
    misc: MiscLinks
    photo: PhotoLinks
    video: VideoLinks
    document: DocumentLinks
    telegraph: TelegraphLinks


category_link = {
    'DRIVING_SCHOOL_OR_LAW': 'https://i.imgur.com/V4gBQ7X.jpg',
    'ALCOHOL_OR_TOBACCO': 'https://i.imgur.com/35LHl3s.jpg',
    'ANONYMIZERS': 'https://i.imgur.com/kcSc067.jpg',
    'DATABASES_OR_LOGS': 'https://i.imgur.com/zV1jvda.jpg',
    'BANK_CARDS': 'https://i.imgur.com/G2Vj4vc.jpg',
    'BOMBERS_OR_CALLS_OR_SPAM_MAILING': 'https://i.imgur.com/WoYGrn4.jpg',
    'HACKING_SOCIAL_NETWORKS_OR_MAILS': 'https://i.imgur.com/jz3Mvwm.jpg',
    'GRANDPA': 'https://i.imgur.com/L4iWzwl.jpg',
    'DETECTIVES': 'https://i.imgur.com/IvE0Vcm.jpg',
    'DESIGN_OR_RENDERING': 'https://i.imgur.com/rrm7MJT.jpg',
    'DROP_SKIP_SERVICE': 'https://i.imgur.com/FZDV20b.jpg',
    'DUPLICATE_DOCUMENTS': 'https://i.imgur.com/HoE6BLY.jpg',
    'FOOD': 'https://i.imgur.com/Dzz2W0X.jpg',
    'LOANS': 'https://i.imgur.com/VnI3Zml.jpg',
    'GAME_ITEMS': 'https://i.imgur.com/0bY2iP2.jpg',
    'TRACKING_INFORMATION': 'https://i.imgur.com/uCvodYo.jpg',
    'COSMETICS': 'https://i.imgur.com/6lRlwdj.jpg',
    'WALLETS': 'https://i.imgur.com/TgZtsg5.jpg',
    'LENDING': 'https://i.imgur.com/uTMZVa9.jpg',
    'CRYPTOCURRENCY': 'https://i.imgur.com/j2f9XxV.jpg',
    'MEDICINE': 'https://i.imgur.com/ioUxpqY.jpg',
    'MERCH': 'https://i.imgur.com/GpD8ytN.jpg',
    'BOOST_SUBSCRIBERS': 'https://i.imgur.com/ZiRtnwC.jpg',
    'CHEAT': 'https://i.imgur.com/NOrXNba.jpg',
    'CASH_OUT': 'https://i.imgur.com/BpI3lpx.jpg',
    'HOTELS_AND_LEISURE': 'https://i.imgur.com/ayLGXif.jpg',
    'PRANK_AND_RINGTONES': 'https://i.imgur.com/xqFxHR0.jpg',
    'BREAKING_THROUGH': 'https://i.imgur.com/Ku8stNw.jpg',
    'PROGRAMMING_AND_DEVELOPMENT': 'https://i.imgur.com/imTeB2i.jpg',
    'SOFTWARE_OR_PROGRAMMING': 'https://i.imgur.com/sLOrnZd.jpg',
    'PROMO_CODES_OR_DISCOUNTS_OR_VOTES_OR_CASHBACK': 'https://i.imgur.com/EtWzi5v.jpg',
    'REWARDS': 'https://i.imgur.com/d8lL2Nu.jpg',
    'REFUNDS': 'https://i.imgur.com/n9LVuPr.jpg',
    'SPORTSMEN': 'https://i.imgur.com/4IbmR5s.jpg',
    'SIM_CARDS_OR_TARIFFS': 'https://i.imgur.com/bhHd7sN.jpg',
    'INSURANCE': 'https://i.imgur.com/vgcOGk2.jpg',
    'SCHEMES_OR_TRAINING': 'https://i.imgur.com/MV28n8Q.jpg',
    'TAXI': 'https://i.imgur.com/sMTgCY9.jpg',
    'TECHNICS': 'https://i.imgur.com/wGMtssB.jpg',
    'TRAFFIC': 'https://i.imgur.com/vS9qR19.jpg',
    'LEGAL_SERVICES': 'https://i.imgur.com/C5zqQk9.jpg'
}