from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Nombre de tu API
    PROJECT_NAME: str = "Sistema de Reservas"
    
    # URL de conexión a la base de datos.
    # Al estar usando FastAPI (asíncrono) y PostgreSQL, el driver ideal es 'asyncpg'.
    # Formato: postgresql+asyncpg://usuario:password@host:puerto/nombre_bd
    DATABASE_URL: str = "postgresql+asyncpg://postgres.nibylsfeiptecqdnxcbb:k9Vb#p2Lq$mR7zW!x5Ty@aws-1-us-west-2.pooler.supabase.com:5432/postgres"

    # Configuración de Pydantic para que lea automáticamente un archivo .env si existe en la raíz
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

# Instanciamos la configuración para poder importarla en otros archivos como 'settings.DATABASE_URL'
settings = Settings()