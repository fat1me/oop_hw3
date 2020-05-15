class VirtualException(BaseException):
    def __init__(self, _type, _func):
        BaseException(self)

class newClass():
    def printing(self):
        raise VirtualException()

class Container():
    def printing(self):
        print("Container")
        print("Name: NewContainer")
        print("Number of ithem: 2")

class Tree():
    def printing(self):
        print("Tree")
        print("Indicator to the root: 2")
        print("Number of level: 5")

class Turn():
    def printing(self):
        print("Turn")
        print("Indicator on the head: 1")
        print("Indicator of tail: 20")

array = [Container(), Tree(), Turn()]
for _new in array:
    _new.printing()