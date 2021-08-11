from dataclasses import dataclass
from typing import List


@dataclass
class BotConfig:
    token: str
    languages: List[str]
    timezone: int
    admin_id: int
    main_chats_id: List[int]
    chats_id: List[int]
    chat_id_service: int
    commands: dict
    is_active: bool = True


@dataclass
class DatabaseConfig:
    host: str
    port: int
    db: str
    db_user: str
    db_pass: str
    url: str


@dataclass
class ImgbbConfig:
    token: str


@dataclass
class Config:
    bot: BotConfig
    database: DatabaseConfig
    imgbb: ImgbbConfig
