#!/usr/bin/python3

import unittest
import pi

class TestPi(unittest.TestCase):
    def test_bare_init(self):
        animal = pi.Animal()
        self.assertTrue(isinstance(animal.numerator, int))
        self.assertTrue(isinstance(animal.denominator, int))
        self.assertTrue(isinstance(animal.age, int))
        self.assertTrue(isinstance(animal.fitness, float))

    def test_get_pi_datatype(self):
        animal = pi.Animal()
        self.assertTrue(not float.is_integer(animal.get_pi()))

    def test_animal_optional_params(self):
        animal = pi.Animal(3, 6)

    def test_animal_age_starts_at_zero(self):
        animal = pi.Animal()
        self.assertEqual(0, animal.age)

    def test_config_print(self):
        config = pi.Config()
        assert('World configuration: {' in config.__str__())

    def test_initial_population_count(self):
        config = pi.Config()
        world = pi.World(config)
        self.assertEqual(len(world.animals), config.initial_population)

    def test_fittest_member_sorting(self):
        config = pi.Config()
        world = pi.World(config)
        world.animals[-1].fitness = 0  # make last animal maximally fit
        world.sort_animals()
        self.assertEqual(world.animals[0].fitness, 0)

    def test_get_parents_even_pairs(self):
        config = pi.Config()
        config.initial_population = 11
        world = pi.World(config)
        self.assertTrue(len(list(
            world.get_parents(world.animals))[-1]) % 2 == 0,
            "Length of last parent pair wasn't even but should have been")

