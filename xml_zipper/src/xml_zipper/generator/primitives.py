import random
import string
from uuid import uuid4


def id_() -> str:
    return str(uuid4())


MIN_LEVEL = 1
MAX_LEVEL = 100


def level() -> str:
    return str(random.randint(MIN_LEVEL, MAX_LEVEL))


NAME_LENGTH = 5


def name():
    return "".join(random.choices(string.ascii_letters, k=NAME_LENGTH))


MIN_OBJECTS_COUNT = 1
MAX_OBJECTS_COUNT = 10


def objects_count() -> int:
    return random.randint(MIN_OBJECTS_COUNT, MAX_OBJECTS_COUNT)
