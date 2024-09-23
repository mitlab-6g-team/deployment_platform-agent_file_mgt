import os
import zipfile

def build_abs_folder_path(data_dict):
    current_dir_str = os.getcwd()
    previous_dir_str = os.path.dirname(current_dir_str)
    folder_path_str = data_dict['folder_path']
    # abs_folder_path_str = previous_dir_str + '/' + folder_path_str
    abs_folder_path_str = previous_dir_str + folder_path_str

    return abs_folder_path_str

def save_in_host(folder_path_str, file):
    file_extension_str = ""
    is_model_bol = False
    
    tail = folder_path_str.split('/')[-1]
    if tail == "template":
        folder_path_str = folder_path_str.replace('/template', '')
    
    os.makedirs(folder_path_str, exist_ok=True)

    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(folder_path_str)

        
        file_info  = zip_ref.infolist()[0]
        old_file_path = folder_path_str + '/' + file_info.filename
        new_file_path = folder_path_str + '/template'
        
        if not file_info.is_dir():
            is_model_bol = True
            _, file_extension_str = os.path.splitext(file_info.filename)
            model_uid_str = folder_path_str.split('/')[-1]
            file_name_str = model_uid_str + file_extension_str
            new_file_path = folder_path_str + '/' + file_name_str
            file_extension_str = file_extension_str.split('.')[-1]

        os.rename(old_file_path, new_file_path)
    return is_model_bol, file_extension_str
