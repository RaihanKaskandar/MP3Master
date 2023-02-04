import eyed3


def get_old_metadata(mp3_files):
    old_metadata = []
    audio_file = eyed3.load(mp3_files[0])

    old_metadata.append(audio_file.tag.artist)
    old_metadata.append(audio_file.tag.title)
    old_metadata.append(audio_file.tag.album)

    # for x in old_metadata:
    #     print(x)

    return old_metadata
