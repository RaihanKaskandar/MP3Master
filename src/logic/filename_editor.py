from file_explorer import get_mp3_files
from name_parser import get_title_names
from name_parser import get_dir
from name_editor import get_files_with_artist
from name_editor import set_filename


class MusicCollection:
    def __init__(self):
        self.path = []
        self.track_titles = []
        self.location_path = []
        self.final_titles = []


def print_path(mp3_files):
    print("Opening file(s): ")
    for x in mp3_files:
        print("     " + x + "\n")


def print_location_path(mp3_files):
    print("PRINTING PATH LOCATION")
    for x in mp3_files:
        print(x)


def print_final_titles(titles):
    print("PRINTING FINAL TITLES")
    for x in titles:
        print(x)


def rename_mp3_files():
    my_music_collection = MusicCollection()

    my_music_collection.path = get_mp3_files()
    print_path(my_music_collection.path)

    my_music_collection.location_path = get_dir(my_music_collection.path)
    print_location_path(my_music_collection.location_path)

    my_music_collection.track_titles = get_title_names(my_music_collection.path)

    my_music_collection.final_titles = get_files_with_artist(
        my_music_collection.track_titles
    )
    print_final_titles(my_music_collection.final_titles)

    set_filename(
        my_music_collection.path,
        my_music_collection.location_path,
        my_music_collection.final_titles,
    )
