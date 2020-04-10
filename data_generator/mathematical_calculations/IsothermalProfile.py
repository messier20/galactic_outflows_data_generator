import math


class IsothermalProfile:
    def __init__(self):
        pass

    def calculate_profile(self, total_mass, radius_current, dot_radius_current, dotdot_radius_current, scale_radius, phi_coef):
        """
        :rtype: list
        :param total_mass:
        :param radius_current:
        :param dot_radius_current:
        :param dotdot_radius_current:
        :param scale_radius:
        :param phi_coef:
        :return: mt, mdt, mddt, rho, rho2, phi, phigrad
        """

        mass = total_mass * radius_current / scale_radius
        dot_mass = total_mass * dot_radius_current / scale_radius
        dotdot_mass = total_mass * dotdot_radius_current / scale_radius
        density = total_mass / (4 * math.pi * (radius_current ** 3))
        density2 = total_mass / (4 * math.pi * ((4. * radius_current / 3.) ** 3))
        phi = mass / radius_current * math.log(radius_current / (2.718281828 * phi_coef * scale_radius))
        phigrad = mass / (radius_current ** 2)

        if mass > total_mass:
            mass = total_mass
            dot_mass = 0
            dotdot_mass = 0
            density = 0
            phi = -total_mass / radius_current
            phigrad = total_mass / (radius_current ** 2)

        return mass, dot_mass, dotdot_mass, density, density2, phi, phigrad