from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from django.http import JsonResponse
from main.utils.packet import unpacking
from main.apps.file_operation.services.actor import FileManager_check
from main.apps.file_operation.services.actor import FileManager_save
from main.apps.file_operation.services.actor import FileManager_remove
from main.apps.file_operation.services import build_payload
from main.apps.file_operation.services.file_metadata import ModelMetadataWriter
from main.apps.file_operation.services import common_action
import os

@log_trigger("INFO")
@require_POST
def check(request):
    data_dict = unpacking(request, 'json')

    abs_path_str = common_action.build_abs_path(data_dict)
    exis_bol = FileManager_check.check_abs_path(abs_path_str)

    response_dict = {
                    "detail":"File checked successfully",
                    "data": exis_bol
                    }
    return JsonResponse(response_dict, status=200)

@require_POST
def save(request):
    file, data_dict = unpacking(request, 'file')
    print("data_dict: ", data_dict)
    tail = data_dict["folder_path"].split('/')[-1]
    # if tail == "template":
    #     data_dict["folder_path"] = data_dict["folder_path"].replace('/template', '')
    #     print("data dict:", data_dict["folder_path"])
    abs_folder_path_str = FileManager_save.build_abs_folder_path(data_dict)
    is_model_bol, file_extension_str = FileManager_save.save_in_host(abs_folder_path_str, file)
    if tail != "template":    # 代表是model file，更新model metadata
        payload_dict = build_payload.ModelMetadataWriter_update(abs_folder_path_str, file_extension_str)
        ModelMetadataWriter.update(payload_dict, is_model_bol)

    response_dict = {
                    "detail":"File saved successfully"
                    }
    return JsonResponse(response_dict, status=201)

@log_trigger("INFO")
@require_POST
def remove(request):
    data_dict = unpacking(request, 'json')

    abs_path_str = common_action.build_abs_path(data_dict)

    FileManager_remove.remove_abs_path(abs_path_str)

    response_dict = {
                    "detail":"File removed successfully"
                    }
    return JsonResponse(response_dict, status=200)
