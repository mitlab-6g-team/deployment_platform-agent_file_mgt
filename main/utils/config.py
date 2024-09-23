import os
from dotenv import load_dotenv
from dataclasses import dataclass

# Initialization
load_dotenv(".env.common")
load_dotenv('.env', override=True)


@dataclass
class ServerConfig:
    """
       Server config
    """
    HOST_IP: str
    PORT: str
    NAME: str
    VERSION: str

@dataclass
class Config:
    """
        Config sets
    """
    LOGS_FOLDER_PATH: str
    SECRET_KEY: str
    DJANGO_SETTINGS_MODULE: str
    DEBUG: str
    ALLOWED_HOSTS: str

    FILE_OPERATION:ServerConfig
    FILE_METADATA:ServerConfig


config = Config(
    #Default 
    LOGS_FOLDER_PATH=os.getenv("LOGS_FOLDER_PATH"),
    SECRET_KEY=os.getenv("SECRET_KEY"),
    DJANGO_SETTINGS_MODULE=os.getenv("DJANGO_SETTINGS_MODULE"),
    DEBUG=os.getenv("DEBUG"),
    ALLOWED_HOSTS=os.getenv("ALLOWED_HOSTS"),
    #agent-layer.agent_mgt.file_mgt.file_operation
    FILE_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_FILE_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_FILE_OPERATION_PORT"),
        NAME=os.getenv("HTTP_FILE_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_FILE_OPERATION_VERSION"),
    ),FILE_METADATA=ServerConfig(
        HOST_IP=os.getenv("HTTP_FILE_METADATA_HOST_IP"),
        PORT=os.getenv("HTTP_FILE_METADATA_PORT"),
        NAME=os.getenv("HTTP_FILE_METADATA_NAME"),
        VERSION=os.getenv("HTTP_FILE_METADATA_VERSION"),
    )

)
