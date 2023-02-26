from .artist_checker import contains_artist


def get_artist():
    return input("Which artist performs the song: ")


def add_artist(file, artist):
    file_with_artist = artist + " - " + file
    return file_with_artist


def set_files_with_artist(file_titles):
    artist = get_artist()
    new_files = []
    for x in file_titles:
        if contains_artist(x, artist) == True:
            new_files.append(x)
        else:
            new_files.append(add_artist(x, artist))

    return new_files


def get_files_with_artist(file_titles):
    files_with_artist = set_files_with_artist(file_titles)
    return files_with_artist
