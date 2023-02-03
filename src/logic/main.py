from file_explorer import get_mp3_files
from open_eel import init_eel
from metadata_reader import get_old_metadata

from name_parser import parse_filename

# import parser
# from "file reader" import parse_filename

# from connect_api import test
                                
def main():
    print("Running main function!")
    # init_eel()

    mp3_files = get_mp3_files()
    print("Opening file(s): ")
    for x in mp3_files:
        print("     " + x + "\n")
    
    parse_filename(mp3_files)
    # old_metadata = get_old_metadata(mp3_files)
    # test(old_metadata)

    

if __name__ == "__main__":
    main()
