
def ModelMetadataWriter_update(folder_path_str, file_extension):
    model_uid_str = folder_path_str.split('/')[-1]
    payload_dict = {
                    "uid": model_uid_str,
                    "file_extension": file_extension
                   }

    return payload_dict