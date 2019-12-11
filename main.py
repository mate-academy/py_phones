"""This script represents communication with program user"""
import contacts


P_B = contacts.PhoneBook()


def ask_to_do():
    """Provide list of phonebook action options for user"""
    print("""What do you want to do?
    c - create
    r - read
    u - update
    d - delete
    q - quit
    """)


def confirm_action(text):
    """Notify user of action executed"""
    print(text)


def main():
    """Execute user's commands"""
    while True:
        ask_to_do()
        action = input("?").lower()

        if action == 'c':
            name = input("Provide contact name:\n")
            phone = input("Provide contact phone:\n")
            P_B.create(name, phone)
            confirm_action(f"New contact {name} has been added.")
        elif action == 'q':
            confirm_action("Goodbye!")
            break
        elif action == 'r':
            try:
                name = input("Provide contact name to search by:\n")
                phone = P_B.read(name)
                confirm_action(f"Contact found:\n Name: {name}\n "
                               f"Phone: {phone}")
            except KeyError:
                confirm_action(f"Contact {name} is not found.")
        elif action == 'u':
            try:
                name = input("Provide contact whose phone number "
                             "should be updated:\n")
                phone = input("Provide new phone value:\n")
                P_B.update(name, phone)
                confirm_action("Contact has been updated.")
            except KeyError:
                confirm_action(f"Contact {name} is not found.")
        elif action == 'd':
            try:
                name = input("Provide contact to be deleted:\n")
                P_B.delete(name)
                confirm_action(f"Contact {name} is deleted.")
            except KeyError:
                confirm_action(f"Contact {name} is not found.")
        else:
            print("""Please choose one of options below:
            c - create
            r - read
            u - update
            d - delete
            q - quit
            """)


if __name__ == "__main__":
    P_B.read_contacts_from_file()
    main()
    P_B.write_to_file()
