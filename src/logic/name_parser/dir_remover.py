def remove_directory(file):
    file_without_dir = file.split("/")
    return file_without_dir[len(file_without_dir) - 1]

def get_files_without_dir(mp3_files):
    files_without_dir = []
    for x in mp3_files:
        files_without_dir.append(remove_directory(x))

    return files_without_dir