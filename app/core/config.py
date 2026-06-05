from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field

class Settings(BaseSettings):
    # Nombre de tu API
    PROJECT_NAME: str = "Sistema de Reservas"
    
    # Declaramos las variables individuales que están en tu .env
    DB_USER: str
    DB_PW: str
    DB_HOST: str
    DB_PORT: str
    DB_SCHEMA: str

    # Pydantic construirá esta variable al vuelo usando las anteriores
    #postgresql+asyncpg://usuario:password@host:puerto/nombre_bd

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PW}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_SCHEMA}"
    

# Instanciamos la configuración para poder importarla en otros archivos como 'settings.DATABASE_URL'
settings = Settings()