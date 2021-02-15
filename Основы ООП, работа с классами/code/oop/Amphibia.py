from Auto import *
from Boat import *


class Amphibian(Auto, Boat):
    pass


amb = Amphibian()
amb.ride()
amb.swim()

