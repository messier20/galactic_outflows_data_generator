import math

from data_generator.configurations.physics_constants import LIGHT_SPEED
from data_generator.configurations.constants import DRIVING_FORCE, GAMMA
from data_generator.configurations.units import unit_length, unit_mass


class DrivingForceIntegrator:
    def __init__(self):
        pass

    def driving_force_calc(self, driving_force, mass_gas, radius, eta_drive, integration_method, luminosity, dot_mass_gas, dot_radius,
                           dotdot_radius, mass_potential, dot_mass_potential, dotdot_mass_gas, dotdotdot_radius_arr, radius_arr, dot_radius_arr, dotdot_radius_arr,
                           index, dt):
        mg_mp_term = mass_gas * mass_potential + (mass_gas ** 2) / 2.
        mass_term = (dot_mass_gas * mass_potential + mass_gas * dot_mass_potential + mass_gas * dot_mass_gas) / radius

        # if index == 73:
            # print('t')
        if driving_force == DRIVING_FORCE.ENERGY_DRIVING:
            # TODO vienu atveju, kad butu visas sitas vidus ifo, o kitu atveju, tik kad eta drive 0.05,
            # (
            optical_depth = 0.348 / (unit_length ** 2) * unit_mass * mass_gas / (4 * math.pi * (radius ** 2))
            if optical_depth < 1:
                eta_drive = eta_drive * optical_depth
            if eta_drive < 0.05:
                eta_drive = 0.05  # transition to energy-driven wind
            # )
            # Sitai daliai apskliaustai

            dotdotdot_radius = self.dot_rt_initial_calc(mass_gas, radius, eta_drive, luminosity, dot_mass_gas, dot_radius,
                                              dotdot_radius, mg_mp_term, mass_term, dotdot_mass_gas)

            method_name = str(integration_method.value)
            method = getattr(self, method_name, lambda: 'Invalid')
            return method(dotdotdot_radius, dotdotdot_radius_arr, radius_arr, dot_radius_arr, dotdot_radius_arr, index, dt, radius,
                          dot_radius,
                          dotdot_radius, eta_drive)
        elif driving_force == DRIVING_FORCE.MOMENTUM_DRIVING:
            # TODO implement momentum driving case
            print(driving_force)

    def simple_integration(self, dot_rt, dot_rt_arr, radius_arr, dot_radius_arr, dotdot_radius_arr, index, dt,
                           radius, dot_radius,
                           dotdot_radius, eta_drive):
        dot_rt_arr[index] = dot_rt
        dotdot_radius_arr[index + 1] = dotdot_radius + dot_rt * dt
        dot_radius_arr[index + 1] = dot_radius + dotdot_radius * dt + 0.5 * dot_rt * (dt ** 2.)
        artificial_cap = 2 * eta_drive * LIGHT_SPEED
        if dot_radius_arr[index + 1] > artificial_cap:
            dot_radius_arr[index + 1] = artificial_cap
            if dotdot_radius_arr[index + 1] > 0:
                dotdot_radius_arr[index + 1] = 0
            if dot_rt_arr[index] > 0:
                dot_rt_arr[index] = 0

        # if dot_radius < 0.00000000:
        #     print('t')
        #     print(radius_arr[index - 1])

        # if index == 2175:
        #     print('index ping')
        if dot_radius > artificial_cap:
            radius_arr[index + 1] = radius + dot_radius * dt
        else:
            radius_arr[index + 1] = radius + dot_radius * dt + 0.5 * dotdot_radius * dt ** 2. + (1. / 6.) * dot_rt * dt ** 3.

        return radius_arr, dot_radius_arr, dotdot_radius_arr, dot_rt_arr

    def leap_frog_dkd(self, dot_rt, dot_rt_arr, radius_arr, dot_radius_arr, dotdot_radius_arr, index, dt, radius,
                      dot_radius,
                      dotdot_radius, eta_drive):
        # TODO implement leap_frog_dkd
        pass

    def leap_frog_kdk(self, dot_rt, dot_rt_arr, radius_arr, dot_radius_arr, dotdot_radius_arr, index, dt, radius,
                      dot_radius,
                      dotdot_radius, eta_drive):
        # TODO implement leap_frog_kdk
        pass

    def dot_rt_initial_calc(self, mg, radius, eta_drive, luminosity, mdg, dot_radius,
                            dotdot_radius, mg_mp_term, mass_term, mddg):
        # TODO figure which ones of these have physical meaning
        mg_r = mg * radius
        mdg_rd_squared = mdg * (dot_radius ** 2)
        rd_r_squared = dot_radius / (radius ** 2)
        add_term_1 = eta_drive * luminosity - mdg_rd_squared - mg * dot_radius * dotdot_radius
        add_term_2 = - 2 * rd_r_squared * mg_mp_term
        add_term = 3. * (GAMMA - 1.) / mg_r * (add_term_1 + add_term_2 + mass_term)
        mg_md_term = mddg * dot_radius / mg + mdg_rd_squared / mg_r
        mg_rdd_term = 2 * mdg * dotdot_radius / mg + dot_radius * dotdot_radius / radius
        add_term_3 = mg_md_term + mg_rdd_term
        add_term_4 = (mass_term - rd_r_squared * mg_mp_term)/mg_r
        sum_terms = add_term - add_term_3 - add_term_4

        return sum_terms
