def remove_number(file):
    splitted_name = file.split(" ", 1)
    removed_number_file = splitted_name[1]
    return removed_number_file


def get_removed_number_file(file):
    return remove_number(file)