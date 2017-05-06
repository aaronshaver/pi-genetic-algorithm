#!/usr/bin/python3

import random
import math
import time


class Animal():
    def __init__(self, numerator=None, denominator=None):
        self.max_int = 2147483647
        self.numerator = random.randint(1, self.max_int)
        self.denominator = random.randint(1, self.max_int)
        self.age = 0
        self.fitness = abs(math.pi - self.get_pi())  # distance from pi

    def get_pi(self):
        return self.numerator / (self.denominator * 1.0)


class Config():
    def __init__(self):
        self.max_age = 100
        self.max_generations = 4
        self.sleep_seconds = 1
        self.max_population = 50
        self.initial_population = 10
        self.max_distance_from_pi = 2.4
        self.mutation_percentage = 0.05

    def __str__(self):
        return 'World configuration: ' + str(self.__dict__) + '\n'


class World():
    def __init__(self, config):
        self.animals = []
        self.fill_world(config.initial_population)

    def fill_world(self, population):
        while len(self.animals) < population:
            animal = Animal()
            self.animals.append(animal)


if __name__ == "__main__":
    config = Config()
    print(config)
    world = World(config)

    generation = 0
    while generation < config.max_generations:
        time.sleep(config.sleep_seconds)
        generation += 1
        print("{0} generations elapsed; world population: {1}".
            format(generation, len(world.animals)))


