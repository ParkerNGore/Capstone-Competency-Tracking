from enum import Enum


class User_Type(Enum):
    USER = 1,
    MANAGER = 2,


class Competencies(Enum):
    NONE = 0,
    BASIC = 1,
    INTERMEDIATE = 2,
    ADVANCED = 3,
    EXPERT = 4,
