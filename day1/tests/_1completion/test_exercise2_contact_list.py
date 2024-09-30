import unittest
from day1._1completion.exercise2_contact_list import Contact, ContactList

class TestContactListManager(unittest.TestCase):
    def setUp(self):
        self.contact_list = ContactList()
        self.contact1 = Contact("Alice", "123-456-7890")
        self.contact2 = Contact("Bob", "987-654-3210")
        self.contact_list.add_contact(self.contact1)
        self.contact_list.add_contact(self.contact2)

    def test_add_contact(self):
        self.assertEqual(len(self.contact_list.contacts), 2)
        self.contact_list.add_contact(Contact("Charlie", "555-555-5555"))
        self.assertEqual(len(self.contact_list.contacts), 3)

    def test_remove_contact(self):
        self.contact_list.remove_contact("Alice")
        self.assertEqual(len(self.contact_list.contacts), 1)
        self.assertEqual(self.contact_list.contacts[0].name, "Bob")

    def test_find_contact(self):
        contact = self.contact_list.find_contact("Bob")
        self.assertIsNotNone(contact)
        self.assertEqual(contact.phone, "987-654-3210")

        contact = self.contact_list.find_contact("Charlie")
        self.assertIsNone(contact)

if __name__ == '__main__':
    unittest.main()
