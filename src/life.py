from typing import *
from .baddie import Baddie

class Life:
    def __init__(self) -> None:
        self.baddies: List[Baddie] = []
    
    def configure_life(self) -> None:
        print("baddies r an important part of life")
        # take all the data from data.baddies.txt and initialize a list of baddies here.f
        # get list of baddies from data.baddies.txt
        for line in open("data/baddies.txt"):
            params = line.split(",")
            self.baddies.append(Baddie(params[0], params[1], params[2]))
        print(self.baddies)

    def main():
        print("YISHAW")

    if __name__ == "__main__":
        main()