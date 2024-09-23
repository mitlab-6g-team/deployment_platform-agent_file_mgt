"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config

def update(payload_dict, start_bol):
    """
    Call file_metadata.ModelMetadataWriter.update API
    """
    if start_bol:
        module_name_str = config.FILE_METADATA.NAME
        actor_name_str = "ModelMetadataWriter"
        function_name_str = "update"

        response = request.for_json(module_name_str, actor_name_str, function_name_str, payload_dict)
        print('response: ',response)
        response_dict = response.json()
        response_dict = response_dict["data"]

        return response_dict
