import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load existing contacts


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

# Save contacts


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a contact


def add_contact(contacts):
    name = input("Enter name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"{name} added successfully!\n")

# View all contacts


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n📒 Contact List:")
    for name, info in contacts.items():
        print(f"{name} - 📞 {info['phone']} | ✉️ {info['email']}")
    print()

# Search for a contact


def search_contact(contacts):
    name = input("Enter name to search: ").strip().title()
    if name in contacts:
        info = contacts[name]
        print(f"\n{name} found:")
        print(f"📞 Phone: {info['phone']}")
        print(f"✉️ Email: {info['email']}\n")
    else:
        print(f"{name} not found.\n")

# Delete a contact


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name} deleted successfully!\n")
    else:
        print(f"{name} not found.\n")

# Main menu


def main():
    contacts = load_contacts()

    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
