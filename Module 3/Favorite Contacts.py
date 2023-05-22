import sys
from typing import Dict

contact: dict[str, str] = {}
favorite: dict[str, str] = {}


def display_contact():
    print('Name\t\tContact Number')
    for key in contact:
        print('{}\t\t{}'.format(key, contact.get(key)))


def display_favorite():
    print('Name\t\tFavorite Number')
    for ky in favorite:
        print('{}\t\t{}'.format(ky, favorite.get(ky)))


while True:
    choice = input(' 1. Add Contact \n 2. Display Contact\n 3. Display Favorites\n 4. Edit Contact\n 5. Delete '
                   'Contact\n 6. Exit\n')
    if choice == '1':
        fav = input('Will this be a favorite? Y/N\n')
        if fav == 'N':
            name = input('Enter contact name\n')
            phone = input('Enter phone number\n')
            contact[name] = phone
        elif fav == 'Y':
            fav_name = input('Enter favorite contact name\n')
            fav_phone = input('Enter phone number\n')
            favorite[fav_name] = fav_phone
            contact[fav_name] = fav_phone

    elif choice == '2':
        if not contact:
            print('Contact list is empty')
        else:
            display_contact()
    elif choice == '3':
        if not favorite:
            print('Favorites list is empty')
        else:
            display_favorite()
    elif choice == '4':
        edit_contact = input('Enter contact to be edited\n')
        if edit_contact in contact:
            phone = input('Enter phone number\n')
            new_fav = input('Add as favorite? Y/N\n')
            if new_fav == 'N':
                contact[edit_contact] = phone
                if edit_contact in favorite:
                    favorite.pop(edit_contact)
                    print('Contacts updated')
                    display_contact()
                else:
                    print('Contacts updated')
                    display_contact()
            else:
                favorite[edit_contact] = phone
                contact[edit_contact] = phone
                print('Favorites updates')
                display_favorite()
        else:
            print('Contact not found in list')
    elif choice == '5':
        del_contact = input('Enter contact to be deleted\n')
        if del_contact in contact:
            confirm = input('Do you want to delete ' + del_contact + '? Y/N\n')
            if confirm == 'Y' or 'y':
                contact.pop(del_contact)
                favorite.pop(del_contact)
        else:
            print('Contact not found in list')
    else:
        break
