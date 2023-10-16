#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count
        self._current_page = 1

    def page_count(self):
        return self._page_count

    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        self._current_page += 1
    
    def current_page(self):
        return self._current_page





    
        