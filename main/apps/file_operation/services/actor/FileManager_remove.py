import os
import shutil

def remove_abs_path(abs_path_str):
    model_or_template_str = abs_path_str.split('/')[-1]

    if model_or_template_str == "template":
        shutil.rmtree(abs_path_str)
        # os.remove(abs_path_str)
    elif model_or_template_str == "uav_template":
        shutil.rmtree(abs_path_str)
    else:
        os.remove(abs_path_str)
