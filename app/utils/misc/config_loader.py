import configparser

from app.data.types.config import BotConfig, Config, DatabaseConfig


class ConfigLoader:

    def __init__(self, path_to_config: str):
        self._path_to_config = path_to_config
        self._config = configparser.ConfigParser()

        self._config.read(self._path_to_config)

    @property
    def get_config(self) -> Config:
        config = Config(
            bot=self._get_bot_config,
            database=self._get_database_config
        )
        return config

    @property
    def get_bot_commands(self):
        return dict(self._config['BotCommands'])

    @property
    def _get_bot_config(self) -> BotConfig:
        bot_config = BotConfig(
            token=self._config['BotConfig']['token'],
            languages=self._config['BotConfig']['languages'].split(),
            timezone=int(self._config['BotConfig']['timezone']),
            admin_id=int(self._config['BotConfig']['admin_id']),
            chats_id=[int(chat_id) for chat_id in self._config['BotConfig']['chats_id'].split()],
            main_chats_id=[int(chat_id) for chat_id in self._config['BotConfig']['main_chats_id'].split()],
            commands=self.get_bot_commands
        )
        return bot_config

    @property
    def _get_database_config(self) -> DatabaseConfig:
        host = self._config['DatabaseConfig']['host']
        port = self._config['DatabaseConfig']['port']
        db = self._config['DatabaseConfig']['db']
        db_user = self._config['DatabaseConfig']['db_user']
        db_pass = self._config['DatabaseConfig']['db_pass']
        database_config = DatabaseConfig(
            host=host,
            port=port,
            db=db,
            db_user=db_user,
            db_pass=db_pass,
            url=f'postgresql://{db_user}:{db_pass}@{host}:{port}/{db}',
        )
        return database_config
