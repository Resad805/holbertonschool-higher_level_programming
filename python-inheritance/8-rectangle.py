#!/usr/bin/python3
"""
Bu modul həndəsi fiqurların təməlini təşkil edən 
BaseGeometry və ondan törəyən Rectangle siniflərini saxlayır.
"""
class BaseGeometry:
    """
    Həndəsi fiqurlar üçün baza sinfi.
    """

    def area(self):
        """
        Sahəni hesablayan metod.
        İstisnasız olaraq Exception qaytarır.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Dəyərin tam ədəd və müsbət olduğunu yoxlayır.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    BaseGeometry-dən miras alan Düzbucaqlı sinfi.
    """
    def __init__(self, width, height):
        """
        Yeni bir Rectangle yaradarkən en və hündürlüyü yoxlayır.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
