from .first_numbers import starts_with_numbers
from .dir_remover import return_files_without_dir

__file_names = []

def parse_filename(mp3_files):
    parsed_names = return_files_without_dir(mp3_files)
    
    for x in parsed_names:
        if (starts_with_numbers(x)):
            print(x + " start with number")
        else: print(x + " doesnt start with numbers")
    
    return parsed_names

def get_filenames(mp3_files):
    __file_names = parse_filename
    return __file_names