# Parent Class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self._origin = origin        # protected attribute
        self.__secret_identity = "Unknown"  # private attribute

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def get_origin(self):
        return self._origin

    def set_secret_identity(self, identity):
        self.__secret_identity = identity

    def reveal_identity(self):
        print(f"{self.name}'s secret identity is {self.__secret_identity}")

# Child Class using Inheritance & Polymorphism
class Speedster(Superhero):
    def use_power(self):
        print(f"{self.name} runs at lightning speed! ⚡")

# Another Child Class
class Flyer(Superhero):
    def use_power(self):
        print(f"{self.name} takes to the skies! 🦅")

# Creating objects
hero1 = Speedster("Flashbolt", "Super Speed", "Lab Accident")
hero2 = Flyer("Skywing", "Flight", "Alien World")

hero1.use_power()
hero2.use_power()

hero1.set_secret_identity("Barry Allen")
hero1.reveal_identity()
