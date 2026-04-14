import threading
import time
import random


class Environment:
    """Class representing a environment of available food and the general population"""

    def __init__(self, food: int) -> None:
        """Initialize food, population and creating lock for secure access"""

        self.food: int = food
        self.lock: threading.Lock = threading.Lock()
        self.population: int = 0

    def consume_food(self) -> bool:
        """Safe attempt to eat 1 unit of food."""

        with self.lock:
            if self.food > 0:
                self.food -= 1
                return True
            return False

    def add_food(self, ammount: int) -> None:
        """Resource recovery in the environment."""
        with self.lock:
            if ammount > 0:
                self.food += ammount

    def change_poplation(self, ammount: int) -> None:
        """Changing the counter of living organisms."""
        with self.lock:
            self.population += ammount


class Organism(threading.Thread):
    """Class reprresenting a live organism"""

    def __init__(self, env: Environment, name):
        """Initialize a new organism"""

        super().__init__(name=name)
        self.env: Environment = env
        self.energy: int = 5
        self.alive: bool = True

    def run(self):
        """The main life cycle of an organism."""

        self.env.change_poplation(1)

        while self.alive:
            self.energy -= 1

            if self.env.consume_food():
                self.energy += 3

            if self.energy >= 10:
                self.energy -= 4
                new_name: str = f"{self.name}_child_{random.randint(10,99)}"
                new_org: Organism = Organism(self.env, name=new_name)
                new_org.start()
            
            if self.energy <= 0:
                self.alive = False
                self.env.change_poplation(-1)
                break

            time.sleep(0.1)


if __name__ == "__main__":
    env: Environment = Environment(50)

    organisms: list = []

    for i in range(5):
        org: Organism = Organism(env, name=f"Organism_{i}")
        organisms.append(org)
        org.start()

    try:
        for _ in range(20):
            time.sleep(0.5)

            env.add_food(15)

            with env.lock:
                print(f"Population: {env.population}. Food on location: {env.food}")

            if env.population == 0:
                print("All organisms are died.")
                break
        
    except KeyboardInterrupt:
        print("\nThe simulation was stopped manually by the user.")