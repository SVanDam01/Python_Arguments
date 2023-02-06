# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# PART 1


def greet(name, template='Hello, <name>!'):
    return template.replace("<name>", name)


print(greet("Stefan"))
print(greet("Mark"))

# PART 2
gravity_factor = {
    "sun": 274,
    "jupiter": 24.9,
    "neptune": 11.2,
    "saturn": 10.4,
    "earth": 9.8,
    "uranus": 8.9,
    "venus": 8.9,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.6
}


def force(mass, body="earth"):
    return mass * gravity_factor[body]


print(force(0.1))
print(force(0.5, "pluto"))

# PART 3


def pull(m1, m2, d):
    g = 6.674*(10**-11)
    result = g * ( m1 * m2) / (d**2)
    return result


print(pull(0.1, 5.972*10**24, 6.371*10**6))
