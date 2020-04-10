import math


class NFW:
    def __init__(self, radius_scaled, concentration):
        self.radius_scaled = radius_scaled
        self.concentration = concentration
        self.radius_scaled_member = self.radius_scaled / (1 + self.radius_scaled)
        self.radius_scaled_squared_member = self.radius_scaled / ((1 + self.radius_scaled) ** 2)
        self.concentration_member = (math.log(1 + self.concentration) - self.concentration / (1 + self.concentration))

    def calculate_halo_profile(self, total_mass, radius, dot_radius, dotdot_radius, halo_scale):
        """
        :rtype: list
        :param total_mass:
        :param radius:
        :param dot_radius:
        :param dotdot_radius:
        :param halo_scale:
        :return: mt, mdt, mddt, rho, rho2, phi, phigrad
        """
        mass = total_mass / self.concentration_member * (
                    math.log(1 + self.radius_scaled) - self.radius_scaled_member)
        dot_mass = total_mass / self.concentration_member * (
                (dot_radius / halo_scale) * self.radius_scaled_squared_member)

        dotdot_mass = total_mass / self.concentration_member * (dotdot_radius / halo_scale * self.radius_scaled_squared_member + (dot_radius ** 2) / (
                halo_scale ** 2) * (1. - self.radius_scaled) / ((1 + self.radius_scaled) ** 3))

        density = total_mass / (
                4 * math.pi * (halo_scale ** 3) * self.radius_scaled_squared_member) / self.concentration_member
        radius_scaled_with_coef = (4. * self.radius_scaled / 3.) / (1. + (4. * self.radius_scaled / 3.) ** 2)
        density2 = total_mass / (
                    4 * math.pi * (halo_scale ** 3) * radius_scaled_with_coef) / self.concentration_member

        phi = -total_mass / halo_scale / self.concentration_member * (math.log(1. + self.radius_scaled) / self.radius_scaled)
        phigrad = total_mass / (halo_scale ** 2) / self.concentration_member * ((math.log(1. + self.radius_scaled) -
                                                                                  self.radius_scaled_member) / (
                                                                                             self.radius_scaled ** 2))

        mass_five_times = 5. * total_mass
        if mass > mass_five_times:
            mass = mass_five_times
            dot_mass = 0
            dotdot_mass = 0
            density = 0
            phi = -mass_five_times / radius
            phigrad = mass_five_times / (radius ** 2)

        return mass, dot_mass, dotdot_mass, density, density2, phi, phigrad
