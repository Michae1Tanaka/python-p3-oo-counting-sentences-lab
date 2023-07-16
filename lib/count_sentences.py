#!/usr/bin/env python3

import re


class MyString:
    def __init__(self, value=""):
        self.word = value

    def get_string(self):
        return self.word

    def set_string(self, value):
        if isinstance(value, str):
            self._word = value
        else:
            print("The value must be a string.")

    value = property(get_string, set_string)

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        formatted_string = re.split("[.?!...]+", self.value)
        formatted_string = list(filter(None, formatted_string))
        return len(formatted_string)
