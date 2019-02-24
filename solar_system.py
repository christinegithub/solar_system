# First we'll need a class to represent the solar system.
# Let's call it System, and give it an attribute bodies. bodies will start as
# an empty list (ie. []).


class System:

    def __init__(self):
        self.bodies = []

# Let's give System an instance method called add which will add a celestial
# body to the list. We'll also need an instance method called total_mass
# which should add up the mass of all the bodies in bodies, and return it.

    def add(self, celestial_body):
        if celestial_body not in self.bodies:
            self.bodies.append(celestial_body)
        else:
            print("{} is already in the list.".format(celestial_body.name))
        return self.bodies

    def total_mass(self):
        current_mass = 0

        for num, body in enumerate(self.bodies):
            current_mass += body.mass
        return current_mass


# We'll also need a class to represent the various celestial bodies.
# We'll call it Body. Each of them will need a name and a mass.
# We'll assign them when we create the body.


class Body(System):

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

# There are several types of bodies we're concerned about in our solar system:
# planets, stars (like our sun), and moons.

# Each of our body types needs a class: Planet, Star, and Moon.
# All of these bodies have some similarities: they all have a name and a mass.
# So, let's also make them inherit from Body. They do have some unique
# qualities though.

# Planets:

# Have a day, which is the number of hours it takes for the planet to
# rotate all the way around once.
# Have a year, which is the number of days it takes for the planet to orbit
# the sun once. Whether you want to express this in Earth days or the planet's
# days is up to you.


class Planet(Body):

    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year

# Stars:
# Have a type (ie. our Sun is a G-type star)


class Star(Body):

    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type

# Moons:
#
# Have a month, which is the number of days it takes for the moon to orbit its
# planet. Again, this can either be Earth days or the planet's days,
# your choice.
# Have a planet that they orbit. We want to store the whole Planet object here.


class Moon(Body):

    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet

# Once we have our structure defined, let's start adding some things to our
# solar system. We can start with the Sun, the Earth, and the Earth's moon.


earth = Planet("earth", 100, 24, 365)
saturn = Planet("saturn", 150, 30, 500)
sun = Star("sun", 5000, "g-type")
earth_moon = Moon("moon", 400, 27, "earth")

solar_system = System()
solar_system.add(earth)
solar_system.add(sun)
solar_system.add(earth_moon)
print(solar_system)
print(solar_system.add(earth))
print(solar_system.add(saturn))
print(solar_system.total_mass())
