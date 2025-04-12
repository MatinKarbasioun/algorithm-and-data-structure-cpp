from python.data_structures.hash_table.map import HashTable
from python.use_caes.contacts.contact import Contact
from python.use_caes.helpers.converter import convert_phone_to_int


class PhoneBook:
    def __init__(self):
        self.__phone_to_name = HashTable()
        self.__name_to_phone = HashTable()

    def add_contact(self, contact: Contact):
        int_phone = convert_phone_to_int(contact.phone)
        self.__phone_to_name.set(int_phone, contact)
        self.__name_to_phone.set(contact.name, contact)

    def delete_contact(self, contact: Contact):
        int_phone = convert_phone_to_int(contact.phone)
        self.__phone_to_name.pop(int_phone)
        self.__name_to_phone.pop(contact.name)

    def get_phone(self, name):
        return self.__name_to_phone[name]

    def get_name(self, phone):
        int_phone = convert_phone_to_int(phone)
        return self.__phone_to_name[int_phone]