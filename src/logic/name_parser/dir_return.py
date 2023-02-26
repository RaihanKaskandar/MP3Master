def split_filename(file):
    last_slash_index = file.rfind("/")
    new_string = file[:last_slash_index]
    return new_string


def get_dir(mp3_files):
    files_without_dir = []
    for x in mp3_files:
        files_without_dir.append(split_filename(x))

    return files_without_dir
