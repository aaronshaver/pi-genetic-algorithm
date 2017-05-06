# pi-genetic-algorithm
Gets integer division approximation of Pi using a genetic framework

## Example output

    * 50 generations elapsed; world population: 2570
    * Fittest animal: {'fitness': Decimal('1.525956513544185161590576172E-18'),
      'numerator': 1277831682.0580788, 'age': 1, 'denominator': 406746457.27794886}
    * 3.1 415 926 535 897 93 (this animal's pi)
    * 3.1 415 926 535 897 93 (actual pi)

## Usage

While this program will work in Python 2.7.x, it runs faster and yields better
results in Python 3.x 

`python pi.py`

To set your own initial conditions for the world, edit the Config class.
