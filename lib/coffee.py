#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def get_size(self):
        return self._size
    
    @size.setter
    def set_size(self, value):
        options = ["Small", "Medium", "Large"]
        # for o in options:
        if value not in options:
            print("size must be Small, medium, or Large")
        else:
            self._size = value

    def tip(self, amount):
        self.price += amount
        print("This coffee is great, hears a tip!")

    size = property(get_size, set_size)