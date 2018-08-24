import os
import random
import string
from uuid import uuid4


def id_() -> str:
    return str(uuid4())


def level() -> str:
    return str(
        random.randint(int(os.environ["MIN_LEVEL"]), int(os.environ["MAX_LEVEL"]))
    )


def name():
    return "".join(
        random.choices(string.ascii_letters, k=int(os.environ["LENGTH_OBJECT_NAME"]))
    )


def objects_count() -> int:
    return random.randint(
        int(os.environ["MIN_OBJECTS_COUNT"]), int(os.environ["MAX_OBJECTS_COUNT"])
    )
