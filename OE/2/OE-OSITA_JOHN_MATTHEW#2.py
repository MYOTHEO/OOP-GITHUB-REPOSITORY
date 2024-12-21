class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def update_brand(self, new_brand):
        self.brand = new_brand

    def update_model(self, new_model):
        self.model = new_model
    
    def update_price(self, new_price):
        self.price = new_price
    
    def delete_attribute(self, attribute):
        if attribute == 'brand':
            self.brand = None
        elif attribute == 'model':
            self.model = None
        elif attribute == 'price':
            self.price = None
    
    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"

# List to hold all phones
phones_list = []

def create_phone():
    brand = input("Enter phone brand: ")
    model = input("Enter phone model: ")
    price = input("Enter phone price: ")
    new_phone = Phone(brand, model, price)
    phones_list.append(new_phone)
    print("\nPhone created successfully!\n")

def modify_phone():
    if len(phones_list) == 0:
        print("\nNo phones to modify.\n")
        return

    print("\nSelect a phone to modify:")
    for idx, phone in enumerate(phones_list):
        print(f"{idx + 1}. {phone}")

    choice = int(input("\nEnter the phone number: ")) - 1

    if choice < 0 or choice >= len(phones_list):
        print("\nInvalid selection.\n")
        return

    print("\nSelect an attribute to modify:")
    print("1. Brand")
    print("2. Model")
    print("3. Price")

    attr_choice = int(input("\nEnter your choice: "))

    if attr_choice == 1:
        new_brand = input("Enter new brand: ")
        phones_list[choice].update_brand(new_brand)
    elif attr_choice == 2:
        new_model = input("Enter new model: ")
        phones_list[choice].update_model(new_model)
    elif attr_choice == 3:
        new_price = input("Enter new price: ")
        phones_list[choice].update_price(new_price)
    else:
        print("\nInvalid selection.\n")
    
    print("\nPhone updated successfully!\n")

def delete_phone():
    if len(phones_list) == 0:
        print("\nNo phones to delete.\n")
        return

    print("\nSelect a phone to delete:")
    for idx, phone in enumerate(phones_list):
        print(f"{idx + 1}. {phone}")

    choice = int(input("\nEnter the phone number to delete: ")) - 1

    if choice < 0 or choice >= len(phones_list):
        print("\nInvalid selection.\n")
        return

    phones_list.pop(choice)
    print("\nPhone deleted successfully!\n")

def delete_phone_attribute():
    if len(phones_list) == 0:
        print("\nNo phones to modify.\n")
        return

    print("\nSelect a phone to delete an attribute from:")
    for idx, phone in enumerate(phones_list):
        print(f"{idx + 1}. {phone}")

    choice = int(input("\nEnter the phone number: ")) - 1

    if choice < 0 or choice >= len(phones_list):
        print("\nInvalid selection.\n")
        return

    print("\nSelect an attribute to delete:")
    print("1. Brand")
    print("2. Model")
    print("3. Price")

    attr_choice = int(input("\nEnter your choice: "))

    if attr_choice == 1:
        phones_list[choice].delete_attribute('brand')
    elif attr_choice == 2:
        phones_list[choice].delete_attribute('model')
    elif attr_choice == 3:
        phones_list[choice].delete_attribute('price')
    else:
        print("\nInvalid selection.\n")
    
    print("\nAttribute deleted successfully!\n")

def show_phones():
    if len(phones_list) == 0:
        print("\nNo phones in the list.\n")
        return

    print("\nList of Phones:")
    for idx, phone in enumerate(phones_list):
        print(f"{idx + 1}. {phone}")
    print()

def main_menu():
    while True:
        print("=== Phone Management System ===")
        print("1. Create a new phone")
        print("2. Modify a phone")
        print("3. Delete a phone")
        print("4. Delete an attribute from a phone")
        print("5. Show all phones")
        print("6. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            create_phone()
        elif choice == 2:
            modify_phone()
        elif choice == 3:
            delete_phone()
        elif choice == 4:
            delete_phone_attribute()
        elif choice == 5:
            show_phones()
        elif choice == 6:
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice. Try again.\n")

if __name__ == "__main__":
    main_menu()