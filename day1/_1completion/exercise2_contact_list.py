class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """Adds a contact to the contact list."""
        self.contacts.append(contact)

    def remove_contact(self, name):
        """Removes a contact from the contact list by name."""
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                return  # Exit the function after removing the contact

    def find_contact(self, name):
        """Finds a contact by name and returns the Contact object, or None if not found."""
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None  # Contact not found

# Example usage
if __name__ == "__main__":
    contact_list = ContactList()
    contact_list.add_contact(Contact("Alice", "123-456-7890"))
    contact_list.add_contact(Contact("Bob", "987-654-3210"))
    print("Contacts after adding Alice and Bob:")
    for contact in contact_list.contacts:
        print(f"{contact.name}: {contact.phone}")

    contact_list.remove_contact("Alice")
    print("Contacts after removing Alice:")
    for contact in contact_list.contacts:
        print(f"{contact.name}: {contact.phone}")

    found_contact = contact_list.find_contact("Bob")
    if found_contact:
        print(f"Found contact: {found_contact.name}: {found_contact.phone}")
    else:
        print("Contact not found.")
