import os


def get_new_filenames(location, track_names):
    concatenated_list = []
    for x in range(len(location)):
        concatenated_list.append(location[x] + "/" + track_names[x])
    return concatenated_list


def set_filename(old_tracks, location, track_names):
    new_tracks = get_new_filenames(location, track_names)

    for x in range(len(new_tracks)):
        os.rename(old_tracks[x], new_tracks[x])
