from enum import Enum


class Transistor:
    """Transistor data structure
    """
    def __init__(self, transistor_type: 'TransistorType',
                    model: str, max_voltage: float, max_current):
        self.type = transistor_type
        self.model = model
        self.max_voltage = max_voltage
        self.max_current = max_current

    def __str__(self) -> str:
        return f"{self.type}, {self.model}, Imax = {self.max_current}, Umax = {self.max_voltage}"

    def __repr__(self) -> str:
        return self.__str__()

class TransistorType(Enum):
    """transistor types"""
    PNP = 0
    NPN = 1
