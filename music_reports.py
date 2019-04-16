YEAR = 2
GENRE = 3
LEN_OF_ALBUM = 4
SECONDS = 60

def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    list_of_albums = []
    second_list = []
    for album in albums:
        genre_of_album = album[GENRE]
        second_list.append(genre_of_album)
        if genre_of_album == genre:
            list_of_albums.append(album)
    if genre not in second_list:
        raise ValueError('Wrong genre')   


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    
    max_len= 0 
    max_album = None
    for album in albums:
        album_year = album[YEAR]
        album_len = (album[LEN_OF_ALBUM].split(":"))
        album_len_sec = int(album_len[0]) * SECONDS + int(album_len[1])
        if album_len_sec > max_len or max_len == 0:
            max_len = album_len_sec
            max_album = album
    return max_album         

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    list_of_len = []
    for album in albums:
        album_len = album[LEN_OF_ALBUM].split(":")
        len_in_sec = [int(album_len[0]) * SECONDS + int(album_len[1])]
        list_of_len.extend(len_in_sec)
    return round(list_of_len / SECONDS, 2)    


def     