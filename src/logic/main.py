from file_explorer import get_mp3_files
from open_eel import init_eel
from metadata_reader import get_old_metadata
from name_parser import get_title_names
from name_editor import get_files_with_artist
                            
def main():
    print("Running main function!")

    mp3_files = get_mp3_files()

    print("Opening file(s): ")
    for x in mp3_files:
        print("     " + x + "\n")

    file_titles = get_title_names(mp3_files)

    final_titles = get_files_with_artist(file_titles)
    print("PRINTING FINAL TITLES")
    for x in final_titles:
        print(x)


    
def unused_functions():
    init_eel()
    old_metadata = get_old_metadata(mp3_files)


if __name__ == "__main__":
    main()
