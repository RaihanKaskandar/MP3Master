from file_explorer import get_mp3_files
from open_eel import init_eel
from metadata_reader import get_old_metadata
                                
def main():
    print("Running main function!")
    # init_eel()

    mp3_files = get_mp3_files()
    print("Opening file(s): ")
    for x in mp3_files:
        print("     " + x + "\n")
    
    get_old_metadata(mp3_files)
    
    

if __name__ == "__main__":
    main()
