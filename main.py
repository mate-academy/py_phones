"""user interface"""
import contacts


def dialog():
    """dialog with user"""
    phb = contacts.PhoneBook()
    while True:
        print("""What do you want to do?
c - create
r - read
u - update
d - delete
q - quit
""")
        action = input("Choose:").lower()
        if action == 'q':
            break
        if action == 'c':
            name = input("User name: ")
            phone = input("User phone: ")
            phb.create(name, phone)
        elif action == 'r':
            try:
                name = input("User name: ")
                print(f"Phone number: {phb.read(name)}")
            except KeyError:
                print("This name is not present in list\n")
        elif action == "u":
            try:
                name = input("User name: ")
                phone = input("Phone: ")
                phb.update(name, phone)
            except ValueError:
                print("This name is not present in list\n")
            else:
                print("Successful!")
        elif action == "d":
            try:
                name = input("User name: ")
                phb.delete(name)
            except ValueError:
                print("This name is not present in list\n")
            else:
                print("Successful!")


if __name__ == "__main__":
    dialog()
