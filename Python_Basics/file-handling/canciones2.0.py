def read_songs():

    with open("songs.txt", "r") as file:

        songs = file.readlines()

    return songs


def sort_songs(songs):

    songs.sort()

    return songs


def write_songs(songs):

    with open("sorted_songs.txt", "w") as file:

        for song in songs:

            file.write(song)


def main():

    songs = read_songs()

    songs = sort_songs(songs)

    write_songs(songs)

    print("Songs sorted successfully")


main()