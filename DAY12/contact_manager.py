contacts = []
def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    
    # Bonus: Prevent duplicate entries
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact already exists!")
            return # Exit the function early

    phone = input("Enter Phone: ").strip()
    
    # Create dictionary and add to list
    new_contact = {"name": name, "phone": phone}
    contacts.append(new_contact)
    print("Contact Added Successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        # Bonus: Sort contacts alphabetically by name
        sorted_contacts = sorted(contacts, key=lambda x: x["name"].lower())
        for contact in sorted_contacts:
            print(f"{contact['name']} - {contact['phone']}")

def search_contact():
        print("Contact Not Found.")

def delete_contact():
    print("\n--- Delete Contact ---")
    delete_name = input("Enter Name to delete: ").strip()
    
    found = False
    for i in range(len(contacts)):
        if contacts[i]["name"].lower() == delete_name.lower():
            # Remove from list
            deleted_contact = contacts.pop(i)
            print(f"Contact {deleted_contact['name']} Deleted Successfully!")
            found = True
            break
            
    if not found:
        print("Contact Not Found.")

# Main Program Loop
def main():
    while True:
        print("\n" + "="*25)
        print("     CONTACT MANAGER     ")
        print("="*25)
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("="*25)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()