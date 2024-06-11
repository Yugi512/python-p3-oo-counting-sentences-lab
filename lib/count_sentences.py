#!/usr/bin/env python3

class MyString:
    def __init__(self,value = ""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        tex = self._value.endswith(".")
        if tex == True:
            return True
        else:
            return False
    
    def is_question(self):
        tex = self._value.endswith("?")
        if tex == True:
            return True
        else:
            return False
    
    def is_exclamation(self):
        tex = self._value.endswith("!")
        if tex == True:
            return True
        else:
            return False
        
    def count_sentences(self):
        lists = []
        text = self._value.split()
        for word in text:
            if word.endswith("."):
                lists.append(word)
            elif word.endswith("?"):
                lists.append(word)
            elif word.endswith("!"):
                lists.append(word)
        return len(lists)
       