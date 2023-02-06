from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    db_user: str
    db_password: SecretStr
    db_name: str
    db_host: str
    db_port: int
    
    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password.get_secret_value()}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimeter = '__'
