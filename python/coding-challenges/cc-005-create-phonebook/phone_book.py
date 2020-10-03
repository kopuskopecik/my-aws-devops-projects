phone_book = {}

def start():
    print("""
    Welcome to the phonebook application
    1. Find phone number
    2. Insert a phone number
    3. Delete a person from the phonebook
    4. Terminate
    """)
    entered_number = input("Select operation on Phonebook App (1/2/3) :")
    if entered_number == "1":
        find_number()
        start()
    elif entered_number == "2":
        insert_number()
        start()
    elif entered_number == "3":
        delete_number()
        start()
    elif entered_number == "4":
        print("Exiting Phonebook")
    else:
        print("Please enter a valid number")
        start()

def insert_number():
    name = input("Insert name of the person : ")
    number = input("Insert phone number of the person: ")

    if name and number.isdigit():
        phone_book[name] = number
        # phone_book = { "ali": 123456}
        print(phone_book)
        
    else:
        print("Invalid input format, cancelling operation ...")
        
        print(phone_book)


def find_number():
    name = input("Find the phone number of : ")
    if name:
        value = phone_book.get(name, f"Couldn't find phone number of {name}")
        print(value)
        

def delete_number():
    name = input("Whom to delete from phonebook : ")
    if name:
        value = phone_book.pop(name, "")
        if value:
            print(f"{name} is deleted from the phonebook")
            
        else:
            print(f"{name} is not in the phonebook")    



start()