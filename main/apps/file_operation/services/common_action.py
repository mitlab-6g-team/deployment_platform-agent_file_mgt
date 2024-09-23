import os

def build_abs_path(data_dict):

    current_dir_str = os.getcwd()
    previous_dir_str = os.path.dirname(current_dir_str)
    file_path_str = data_dict['file_path']
    abs_path_str = previous_dir_str + '/' + file_path_str

    return abs_path_str
