

__file_names = []

def return_number(string_name):
    first_number = int(string_name[0][0])
    second_number = int(string_name[1][0])
    total_number = first_number * 10 + second_number
    return total_number

def check_number(string_name):
    try:
        int(string_name[0][0])
    except:
        print("First character is not a number")
        return False

    try:
        int(string_name[1][0])
    except:
        print("Second character is not a number")
        return False

    return True

def starts_with_numbers(file):
    splitted_name = file.split(" ", 1)
    numbers_string = splitted_name[0]

    if (check_number(numbers_string) == True): 
        number = return_number(numbers_string)
        # Assuming albums don't have more than 50 tracks
        if (number < 50): return True
        else: return False
    else: return False

def remove_directory(file):
    file_without_dir = file.split("/")
    return file_without_dir[len(file_without_dir) - 1]

def set_files_without_dir(mp3_files):
    files_without_dir = []
    for x in mp3_files:
        files_without_dir.append(remove_directory(x))

    return files_without_dir

def parse_filename(mp3_files):
    parsed_names = set_files_without_dir(mp3_files)
    starts_with_numbers(parsed_names[0])

    # for x in parsed_names:
    #     if (starts_with_numbers(x) == True):
    #         print("True")
    #     else: 
    #         print("False")

    return parsed_names

def get_filename(mp3_files):
    __file_names = parse_filename
    return __file_names
