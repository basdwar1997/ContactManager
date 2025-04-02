import json
import re

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def validate_phone(phone):
    return re.match(r"^\+?[0-9]{10,15}$", phone)

def validate_email(email):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    if not validate_phone(phone):
        print("Invalid phone number format!")
        return
    if not validate_email(email):
        print("Invalid email format!")
        return

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

def search_contact():
    query = input("Enter name or phone to search: ")
    contacts = load_contacts()
    results = [c for c in contacts if query in c["name"] or query in c["phone"]]

    if results:
        for contact in results:
            print(contact)
    else:
        print("No contact found!")

def delete_contact():
    phone = input("Enter phone number of contact to delete: ")
    contacts = load_contacts()
    contacts = [c for c in contacts if c["phone"] != phone]
    save_contacts(contacts)
    print("Contact deleted (if existed).")

def main():
    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
