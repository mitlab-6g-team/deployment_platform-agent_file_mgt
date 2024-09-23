from django.urls import path
from main.utils.config import config
from main.apps.file_operation.actors import FileManager

FILE_OPERATION_NAME=config.FILE_OPERATION.NAME

urlpatterns = [
    path(
        f'{FILE_OPERATION_NAME}/FileManager/check',
        FileManager.check
    ),
    path(
        f'{FILE_OPERATION_NAME}/FileManager/save',
        FileManager.save
    ),
    path(
        f'{FILE_OPERATION_NAME}/FileManager/remove',
        FileManager.remove
    )
]
