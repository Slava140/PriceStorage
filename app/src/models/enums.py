from enum import Enum


class Unit(str, Enum):
    kg = 'кг'
    pcs = 'шт'


class Status:
    success: "success"
    error: "error"
