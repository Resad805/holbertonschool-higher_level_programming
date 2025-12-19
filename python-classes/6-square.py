#!/usr/bin/python3
"""salam"""


class Square:
    """s"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(self.__size):
            print('#' * self.__size)

    @property
    def position(self):
        """Position değerini döndürür"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position değerini doğrular: 2 pozitif tam sayıdan oluşan bir tuple mı?"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Alanı döndürür"""
        return self.__size ** 2

    def my_print(self):
        """Kareyi ekrana basar. Position[1] kadar dikey, 
        position[0] kadar yatay boşluk bırakır."""
        if self.__size == 0:
            print("")
            return

        # Üstten dikey boşluk (Y ekseni)
        for _ in range(self.__position[1]):
            print("")

        # Karenin her bir satırı
        for _ in range(self.__size):
            # Soldan yatay boşluk (X ekseni) + Kare karakterleri
            print(" " * self.__position[0] + "#" * self.__size)