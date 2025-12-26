#!/usr/bin/python3
"""inheritance"""


class BaseGeometry:
    """s"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is int:
            except TypeError:
                print("{} must be an integer".format(name))

        if value <= 0:
            except ValueError:
                print("{} must be greater than 0".format(name))

