import math

from data_generator.configurations.constants import GRAVITATIONAL

unit_length = 3.086e21
unit_mass = 5e9 * 1.989e33
unit_velocity = math.sqrt(GRAVITATIONAL * unit_mass / unit_length)  # unitvel = sqrt(gg*unitmass/unitlength)

unit_time = unit_length/unit_velocity
unit_surfden = unit_mass/(unit_length**2)
unit_energy = unit_mass*(unit_velocity**2)
unit_density = unit_mass/(unit_length**3)
#
unit_kpc = unit_length / 3.086e21
unit_year = unit_time/3.15e7
unit_sunmass = unit_mass / 1.989e33