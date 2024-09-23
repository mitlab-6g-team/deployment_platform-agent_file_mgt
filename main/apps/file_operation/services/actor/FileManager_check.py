import os

def check_abs_path(abs_path_str):
    model_or_template_str = abs_path_str.split('/')[-1]
    exis_bol = True

    if model_or_template_str == "template":
        folder_exis_bol = os.path.isdir(abs_path_str)
        exis_bol = folder_exis_bol
    else:
        file_exis_bol = os.path.isfile(abs_path_str)
        exis_bol = file_exis_bol

    return exis_bol