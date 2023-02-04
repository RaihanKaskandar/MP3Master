def word_equals_artist(word, artist):
    if word == artist:
        return True
    else:
        return False


def get_first_word(file):
    splitted_name = file.split(" ", 1)

    try:
        splitted_name = splitted_name[0].split(".")
        word = splitted_name[0]
    except:
        word = splitted_name[0]

    return word


def contains_artist(file, artist):
    word = get_first_word(file)

    if word_equals_artist(word, artist) == True:
        print(file + " contains artist already")
        return True
    else:
        print(file + " doesnt contain artist yet")
        return False
