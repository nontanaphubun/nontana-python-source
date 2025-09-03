def contact_book():
    """
    Contact management system using dictionaries
    Each contact: {"name": str, "phone": str, "email": str, "category": str}
    """
    
    contacts = {
        "John Doe": {"phone": "123-456-7890", "email": "john@example.com", "category": "friend"},
        "Jane Smith": {"phone": "987-654-3210", "email": "jane@example.com", "category": "work"},
    }
    
    def add_contact():
        """Add a new contact to the address book"""
        print("\n=== Add New Contact ===")
        name = input("Enter contact name: ").strip()
        
        if name in contacts:
            print("Contact already exists.")
            choice = input("Do you want to update it? (y/n): ").strip().lower()
            if choice != 'y':
                return

        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()
        category = input("Enter category (family/friend/work/other): ").strip().lower()
        
        contact_info = {
            "phone": phone,
            "email": email,
            "category": category
        }
        
        contacts[name] = contact_info
        print(f"Contact '{name}' added/updated successfully!")
    
    def view_contact():
        """View details of a specific contact"""
        print("\n=== View Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to view: ").strip()
        
        if name in contacts:
            contact = contacts[name]
            print(f"\nName: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Category: {contact['category']}")
        else:
            print(f"Contact '{name}' not found.")
    
    def search_contacts():
        """Search contacts by name, phone, or email"""
        print("\n=== Search Contacts ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        search_term = input("Enter search term (name/phone/email): ").strip().lower()
        found_contacts = []

        for name, info in contacts.items():
            if (search_term in name.lower() or
                search_term in info['phone'].lower() or
                search_term in info['email'].lower()):
                found_contacts.append((name, info))
        
        if found_contacts:
            print(f"\nFound {len(found_contacts)} contact(s):")
            print(f"{'Name':<20} {'Phone':<15} {'Email':<25} {'Category':<10}")
            print("-" * 70)
            for name, info in found_contacts:
                print(f"{name:<20} {info['phone']:<15} {info['email']:<25} {info['category']:<10}")
        else:
            print("No contacts found matching your search.")
    
    def list_all_contacts():
        """Display all contacts in a formatted way"""
        print("\n=== All Contacts ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        print(f"{'Name':<20} {'Phone':<15} {'Email':<25} {'Category':<10}")
        print("-" * 70)
        for name, info in contacts.items():
            print(f"{name:<20} {info['phone']:<15} {info['email']:<25} {info['category']:<10}")
    
    def update_contact():
        """Update an existing contact"""
        print("\n=== Update Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to update: ").strip()
        
        if name in contacts:
            contact = contacts[name]
            print(f"Current info for '{name}':")
            print(f"1. Phone: {contact['phone']}")
            print(f"2. Email: {contact['email']}")
            print(f"3. Category: {contact['category']}")
            print("Which field do you want to update? (1/2/3/all): ")
            choice = input().strip().lower()

            if choice in ['1', 'all']:
                contact['phone'] = input("Enter new phone number: ").strip()
            if choice in ['2', 'all']:
                contact['email'] = input("Enter new email address: ").strip()
            if choice in ['3', 'all']:
                contact['category'] = input("Enter new category: ").strip().lower()
            
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")
    
    def delete_contact():
        """Delete a contact"""
        print("\n=== Delete Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to delete: ").strip()
        
        if name in contacts:
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
            if confirm == 'y':
                del contacts[name]
                print(f"Contact '{name}' deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"Contact '{name}' not found.")
    
    # Main menu loop
    while True:
        print("\n" + "="*50)
        print("           CONTACT BOOK MANAGER")
        print("="*50)
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contacts")
        print("4. List All Contacts")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            list_all_contacts()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            print("Thank you for using Contact Book Manager!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-7.")

if __name__ == "__main__":
    print("Starting Contact Book Manager...")
    contact_book()