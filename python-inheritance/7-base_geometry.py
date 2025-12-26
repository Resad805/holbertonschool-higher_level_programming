#!/usr/bin/python3
"""BaseGeometry sinfi üçün modul."""


class BaseGeometry:
    """Həndəsi fiqurlar üçün baza sinfi."""

    def area(self):
        """Sahəni hesablamalıdır, hələ tətbiq edilməyib."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyəri tam ədəd və müsbət olması baxımından yoxlayır."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))