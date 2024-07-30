import json
import os

# File to store contacts
CONTACTS_FILE = 'contacts.json'


def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def edit_contact(contacts):
    """Edit an existing contact."""
    view_contacts(contacts)
    index = int(input("Enter the contact number to edit: ")) - 1

    if 0 <= index < len(contacts):
        contacts[index]['name'] = input("Enter new name: ")
        contacts[index]['phone'] = input("Enter new phone number: ")
        contacts[index]['email'] = input("Enter new email address: ")
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Invalid contact number.")


def delete_contact(contacts):
    """Delete a contact."""
    view_contacts(contacts)
    index = int(input("Enter the contact number to delete: ")) - 1

    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Invalid contact number.")


def main():
    """Main function to run the contact management program."""
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
