from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_DIALECT: str
    DATABASE_DRIVER: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_DBNAME: str


    class Config:
        env_file = './.env'


settings = Settings()