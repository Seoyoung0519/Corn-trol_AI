from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Corn-trol AI Server"
    APP_VERSION: str = "0.1.0"
    ENV: str = "local"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # 추후 백엔드 서버 주소 연결 시 사용
    BACKEND_BASE_URL: str = "http://localhost:8080"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()