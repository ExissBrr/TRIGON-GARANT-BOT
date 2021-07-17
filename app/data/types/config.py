from dataclasses import dataclass
from typing import List


@dataclass
class BotConfig:
    token: str
    languages: List[str]
    timezone: int
    admin_id: int
    chats_id: List[int]
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
class Config:
    bot: BotConfig
    database: DatabaseConfig
