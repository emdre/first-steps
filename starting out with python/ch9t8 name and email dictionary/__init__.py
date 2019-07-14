import menu_choices
import save_load_dictionary


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():

    emails = save_load_dictionary.unpickle_it()

    choice = 0

    while choice != QUIT:

        choice = menu_choices.get_menu_choice()

        if choice == LOOK_UP:
            menu_choices.look_up(emails)
        elif choice == CHANGE:
            menu_choices.change(emails)
        elif choice == ADD:
            menu_choices.add(emails)
        elif choice == DELETE:
            menu_choices.delete(emails)

    save_load_dictionary.pickle_it(emails)


main()
