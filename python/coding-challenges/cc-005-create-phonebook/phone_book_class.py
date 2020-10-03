class PhoneBook:
    phone_book = {} # class attribute
    liste = []
    demet = ()
    print("Sınıf niteliği")

    def __init__(self):
        print("init çalıştı")
        self.elma = ""
        self.liste2 = []
        self.demet2 = ()
        self.start()
    
    def start(self):
        #self.book = {}
        print("""
        Welcome to the phonebook application
        1. Find phone number
        2. Insert a phone number
        3. Delete a person from the phonebook
        4. Terminate
        """)
        entered_number = input("Select operation on Phonebook App (1/2/3) :")
        if entered_number == "1":
            self.find_number()
            self.start()
        elif entered_number == "2":
            self.insert_number()
            self.start()
        elif entered_number == "3":
            self.delete_number()
            self.start()
        elif entered_number == "4":
            print("Exiting Phonebook")
        else:
            print("Please enter a valid number")
            self.start()

    def insert_number(self):
        name = input("Insert name of the person : ")
        number = input("Insert phone number of the person: ")

        if name and number.isdigit():
            self.phone_book[name] = number
            # phone_book = { "ali": 123456}
            print(self.phone_book)
        
        else:
            print("Invalid input format, cancelling operation ...")
        
            print(self.phone_book)


    def find_number(self):
        name = input("Find the phone number of : ")
        if name:
            value = self.phone_book.get(name, f"Couldn't find phone number of {name}")
            print(value)
        

    def delete_number(self):
        name = input("Whom to delete from phonebook : ")
        if name:
            value = self.phone_book.pop(name, "")
            if value:
                print(f"{name} is deleted from the phonebook")
            
            else:
                print(f"{name} is not in the phonebook")


#ahmet = PhoneBook()



