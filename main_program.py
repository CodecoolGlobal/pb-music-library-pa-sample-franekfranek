import display
import file_handling
import sys
"""
The main program should use functions from music_reports and display modules
"""

DATA = file_handling.import_data() 
ARTIST = 0
ALBUM_NAME = 1

def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    start = True
    while start:
        handle_menu()
        choice()


def handle_menu():
    options = ["remove a record",
                "get_albums_by_genre",
                "get_longest_album",
                "get_total_albums_length"]
    display.print_program_menu(options, "q-----> quit program" + "\n")            


def get_input(list_of_inputs, prompt):
    print(prompt)
    inputs = []
    for i in range(len(list_of_inputs)):
        inputs.append(input(list_of_inputs[i]))
    return inputs


def delete_record(albums, artist, album_name):
    for album in albums:
        artis_name = album[ARTIST]
        album_title = album[ALBUM_NAME]
        if artis_name == artist and album_title == album_name:
            albums.remove(album)
            file_handling.export_data(albums, mode="w")
    return albums        


def choice():
    inputs = get_input(["Please provide a valid input: "], "")
    option = inputs[0]
    if option == "1":
        inputs_del = get_input(["Enter artist name: ", "Enter album title: "], "")
        delete_record(DATA, inputs_del[ARTIST], inputs_del[ALBUM_NAME]) 
    if option == "2":
        pass
    if option == "3":
        pass    
    if option == "4":
        pass
    if option == "5":
        pass
    if option == "q":
        sys.exit()           



if __name__ == '__main__':
    main()
