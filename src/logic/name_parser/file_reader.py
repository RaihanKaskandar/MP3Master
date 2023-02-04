from .first_numbers import starts_with_numbers
from .dir_remover import get_files_without_dir
from .number_remover import get_removed_number_file


def change_filenames(mp3_files):
    files_without_dir = get_files_without_dir(mp3_files)
    files_with_titles_only = []

    for x in files_without_dir:
        if starts_with_numbers(x):
            files_with_titles_only.append(get_removed_number_file(x))
        else:
            files_with_titles_only.append(x)

    return files_with_titles_only


def get_title_names(mp3_files):
    return change_filenames(mp3_files)
