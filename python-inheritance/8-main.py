#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle
BaseGeometry = __import__('8-rectangle').BaseGeometry # Əgər hər ikisi eyni fayldadırsa

print(issubclass(Rectangle, BaseGeometry))

try:
    r = Rectangle(4, "5")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(-4, 5)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

