import os


def get_column(dataframe, column):
    labels = dataframe[column]
    return labels

def join_directory(path1, path2):
    joined_path = os.path.join(path1, path2)
    return joined_path

def find_file(file):
    user_directory = os.path.expanduser("~")
    downloads_folder = join_directory(user_directory, "Downloads")
    file_path = join_directory(downloads_folder, file)
    
    if os.path.exists(file_path):
        return file_path
    else:
        raise FileNotFoundError(f"File '{file}' was not found in '{downloads_folder}' folder..")