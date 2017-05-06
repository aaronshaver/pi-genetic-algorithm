#!/usr/bin/python3

import random
import math
import time

MAX_INT = 2147483647

class Animal():
    def __init__(self, numerator=None, denominator=None):
        self.numerator = numerator if(numerator) else random.randint(
            1, MAX_INT)
        self.denominator = denominator if(denominator) else random.randint(
            1, MAX_INT)
        self.age = 0
        self.fitness = abs(math.pi - self.get_pi())  # distance from pi

    def get_pi(self):
        return self.numerator / (self.denominator * 1.0)


class Config():
    def __init__(self):
        self.max_age = 100
        self.max_generations = 30
        self.sleep_seconds = 0
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
        self.sort_animals()

    def fill_world(self, population):
        while len(self.animals) < population:
            animal = Animal()
            self.animals.append(animal)

    def sort_animals(self):
        self.animals.sort(key=lambda x: x.fitness)

    def get_parents(self, l):
        for i in range(0, len(l), 2):
            to_yield = l[i:i + 2]
            if len(to_yield) % 2 == 0:
                yield to_yield

    def reproduce_animals(self):
        parent_pairs = list(self.get_parents(self.animals))
        for pair in parent_pairs:
            child = self.new_child(pair[0], pair[1])
            self.animals.append(child)

    def new_child(self, father, mother):
        num = (father.numerator + mother.numerator) / 2
        den = (father.denominator + mother.denominator) / 2
        return Animal(num, den)

def print_world_status(generation, world):
    print('* {0} generations elapsed; world population: {1}'.
        format(generation, len(world.animals)))
    fittest = world.animals[0]
    print('* Fittest animal: ' + str(fittest.__dict__))
    print('* Pi approximation: ' + str(fittest.get_pi()))
    print('')

if __name__ == '__main__':
    config = Config()
    print(config)
    world = World(config)

    generation = 0
    print_world_status(generation, world)

    while generation < config.max_generations:
        time.sleep(config.sleep_seconds)
        world.reproduce_animals()
        world.sort_animals()
        generation += 1
        print_world_status(generation, world)


