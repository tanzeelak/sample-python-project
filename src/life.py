from typing import *
from .baddie import Baddie

class Life:
    def __init__(self) -> None:
        self.baddies: List[Baddie] = []
        