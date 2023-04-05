#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "new", getattr(magic_string, "new", -1) + 1)
    return "BestSchool" + ", BestSchool" * getattr(magic_string, "new", 0)
