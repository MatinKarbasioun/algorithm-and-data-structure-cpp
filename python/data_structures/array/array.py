from ctypes import py_object, Array


class DynamicArray:
    def __init__(self, capacity=5):
        self.__size = 0
        self.__capacity = capacity
        self.__current = 0
        generic_array  = py_object * self.__capacity
        self.__array = generic_array()

    def __resize(self):
        self.__capacity *= 2
        generic_array = py_object * self.__capacity
        previous_array = self.__array
        self.__array = generic_array()

        self.__fill_array(previous_array)

    def __fill_array(self, previous_array: Array):
        for index in range(self.__size):
            self.__array[index] = previous_array[index]

    def push_back(self, item):
        if self.__size == self.__capacity:
            self.__resize()

        self.__array[self.__size] = item
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            raise IndexError('pop from an empty dynamic array')

        value = self.__array[self.__size]
        self.__array[self.__size - 1] = None
        self.__size -= 1
        return value

    def remove(self, index):
        self.__check_index(index)
        for j in range(index, self.__size-1):
            self.__array[j] = self.__array[j+1]

        self.__size -= 1

    def find(self, key):
        for i in range(self.__size):
            if self.__array[i] == key:
                return i

        return None

    def __getitem__(self, index):
        self.__check_index(index)
        return self.__array[index]

    def __setitem__(self, index, value):
        self.__check_index(index)
        self.__array[index] = value

    def __len__(self):
        return self.__size

    def __str__(self):
        return "[" + ", ".join(repr(self.__array[i]) for i in range(self.__size)) + "]"

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current == self.__size:
            raise StopIteration

        value = self.__array[self.__current]
        self.__current += 1
        return value

    def __check_index(self, index):
        print('size of array', self.__size)
        print('index', index)
        if index > self.__size or index < 0:
            raise IndexError

    def append(self, value):
        self.push_back(value)
