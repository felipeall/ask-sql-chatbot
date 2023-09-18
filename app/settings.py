from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    A class used to represent application settings.

    Attributes
    ----------
    model_config : SettingsConfigDict
        Configuration dictionary for the settings model.
    OPENAI_API_KEY : str
        API key for OpenAI.
    OPENAI_MODEL : str
        Model name to use for OpenAI.
    OPENAI_TEMPERATURE : float
        Temperature setting for OpenAI model.
    POSTGRES_USER : str
        Username for PostgreSQL database.
    POSTGRES_PASSWORD : str
        Password for PostgreSQL database.
    POSTGRES_DB : str
        Database name for PostgreSQL database.
    POSTGRES_PORT : int
        Port number for PostgreSQL database.
    POSTGRES_HOST : str
        Hostname for PostgreSQL database.
    GRADIO_SERVER_PORT : int
        Port number for Gradio server.
    GRADIO_SERVER_NAME : str
        Server name for Gradio server.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    OPENAI_API_KEY: str
    OPENAI_MODEL: Literal["gpt-4", "gpt-3.5-turbo"] = "gpt-4"
    OPENAI_TEMPERATURE: float = 0.2

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_HOST: str = "localhost"

    GRADIO_SERVER_PORT: int = 7806
    GRADIO_SERVER_NAME: str = "chatbot"


settings = Settings()
