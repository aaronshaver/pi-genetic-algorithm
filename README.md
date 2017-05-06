# pi-genetic-algorithm
Gets integer division approximation of Pi using a genetic framework

## Example output

    * 94 generations elapsed; world population: 5142
    * Fittest animal: {'fitness': Decimal('2.579492745515441851615905762E-16'),
    'denominator': 591918485, 'age': 5, 'numerator': 1859566764}
    * 3.1 415 926 535 897 93 (this animal's pi)
    * 3.1 415 926 535 897 93 (actual pi)

## Usage

Install Python 3.x, then:

`python pi.py` (or `python3 pi.py` on Ubuntu)

(It bombs out at the 18th or 19th generation in Python 2.7.x; I couldn't get round() to work in both.)

To set your own initial conditions for the world, edit the member variables of
the Config class. Try it; it's fun!
