from python.data_structures.hash_table.hash_func import HashFunction
from python.data_structures.hash_table.map import HashMap
from python.use_caes.contacts.contact import Contact
from python.use_caes.helpers.converter import convert_phone_to_int


class PhoneBook:
    def __init__(self):
        self.__phone_to_name = HashMap()
        self.__name_to_phone = HashMap()
        self.__hash_func = HashFunction(cardinality=1000)

    def add_contact(self, contact: Contact):
        int_phone = convert_phone_to_int(contact.phone)
        self.__hash_func(int_phone)

    def delete_contact(self, contact):
        pass

    def get_phone(self, name):
        pass

    def get_name(self, phone):
        pass