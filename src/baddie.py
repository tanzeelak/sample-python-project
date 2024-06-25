from dataclasses import dataclass

@dataclass
class Baddie:
    name: str
    age: int
    vibe: str #TODO: use an enum

    def main():
        print("YEEHAW")

    if __name__ == "__main__":
        main()