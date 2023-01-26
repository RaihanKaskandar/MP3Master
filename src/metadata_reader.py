import eyed3

def test(mp3_files):
    audiofile = eyed3.load(mp3_files[0])

    print("Before = " + audiofile.tag.artist)

    audiofile.tag.artist = "MY dick"
    audiofile.tag.save()

    afterfile = eyed3.load(mp3_files[0])

    print("After = " + afterfile.tag.artist)



