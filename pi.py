#!/usr/bin/python3

import random
import time
from decimal import *

MAX_INT = 2147483647
PI = Decimal(3.141592653589793)

def fitness(pi_approx):
    """ Gets the absolute distance between animal's approximation of pi
    and actual value of pi """
    return abs(Decimal(PI) -
               Decimal(pi_approx))  # distance from pi (to 30 digits)


class Animal():
    def __init__(self, numerator=None, denominator=None):
        self.numerator = numerator if(numerator) else random.randint(
            1, MAX_INT)
        self.denominator = denominator if(denominator) else random.randint(
            1, MAX_INT)
        self.age = 0
        self.fitness = fitness(self.get_pi())

    def get_pi(self):
        return Decimal(self.numerator) / Decimal(self.denominator)


class Config():
    def __init__(self):
        self.max_age = 5
        self.max_generations = 100
        self.sleep_seconds = 0  # to control screen output speed if needed
        self.max_population = 100000  # for killing off by overcrowding
        self.initial_population = 100
        self.max_distance_from_pi = 1  # for killing 'weak' animals
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

    def kill_old_animals(self, age):
        remaining_animals = [i for i in self.animals if i.age < age]
        self.animals = remaining_animals

    def age_animals(self):
        for animal in self.animals:
            animal.age += 1

    def kill_weak_animals(self, max_dist):
        remaining_animals = [i for i in self.animals
                             if i.fitness < max_dist]
        self.animals = remaining_animals

    def kill_overcrowded(self, max_pop):
        if len(self.animals) > max_pop:
            self.animals = self.animals[:len(self.animals)/2] 


def print_world_status(generation, world):
    print('* {0} generations elapsed; world population: {1}'.
        format(generation, len(world.animals)))
    if len(world.animals) > 0:
        fittest = world.animals[0]
        print('* Fittest animal: ' + str(fittest.__dict__))
        print('* {0:.15f} (this animal\'s pi)'.format(fittest.get_pi()))
    else:
        print('Sorry, no animals are alive')
    print('* {0:.15f} (actual pi)'.format(Decimal(PI)))
    print('')

if __name__ == '__main__':
    config = Config()
    print(config)
    world = World(config)

    generation = 0
    print_world_status(generation, world)

    while generation < config.max_generations:
        time.sleep(config.sleep_seconds)
        world.kill_old_animals(config.max_age)
        world.kill_weak_animals(config.max_distance_from_pi)
        world.reproduce_animals()
        world.sort_animals()
        world.kill_overcrowded(config.max_population)
        generation += 1
        world.age_animals()
        print_world_status(generation, world)

