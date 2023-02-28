# from metadata_reader import get_old_metadata
from open_eel import init_eel
from mp3_editor import rename_mp3_files


def main():
    print("Running main function!")
    init_eel()
    # rename_mp3_files()


# def unused_functions():

#     old_metadata = get_old_metadata(mp3_files)


if __name__ == "__main__":
    main()
