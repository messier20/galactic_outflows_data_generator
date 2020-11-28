import math
from configurations.units import unit_sunmass
from mathematical_calculations.IsothermalProfile import IsothermalProfile
from mathematical_calculations.NFWProfile import NFW


def mass_calculation(radius, dot_radius, dotdot_radius, total_mass, virial_radius,
                     halo_concentration_parameter, bulge_scale,
                     bulge_disc_to_totalmass_fraction, halo_gas_fraction, bulge_disc_gas_fraction, bulge_totalmass):
    """

    :param radius:
    :param dot_radius:
    :param dotdot_radius:
    :param total_mass:
    :param virial_radius:
    :param halo_concentration_parameter:
    :param bulge_scale:
    :param bulge_disc_to_totalmass_fraction:
    :param halo_gas_fraction:
    :param bulge_disc_gas_fraction:
    :param bulge_totalmass:
    :return: mp, mdp, mg, mdg, mddg, rhogas, sigma, deltaphi, phi, phigrad, rhogas2
    """

    # TODO fix variables names
    halo_scale = virial_radius / halo_concentration_parameter
    radius_scaled = radius / halo_scale
    fraction_of_galaxy_in_halo = 1 - bulge_disc_to_totalmass_fraction
    # halo_mass = fraction_of_galaxy_in_halo * total_mass

    NFW_halo_profile = NFW(radius_scaled, halo_concentration_parameter)
    (mass_halo, dot_mass_halo, dotdot_mass_halo, rho_halo, rho2_halo, phi_halo, phigrad_halo) = \
        NFW_halo_profile.calculate_halo_profile(total_mass, radius, dot_radius, dotdot_radius, halo_scale)

    # fraction_of_galaxy_in_halo = 1 - bulge_disc_to_totalmass_fraction
    halo_non_gass_fraction = 1 - halo_gas_fraction
    dark_matter_fraction_in_halo = fraction_of_galaxy_in_halo * halo_non_gass_fraction

    # p-potential, tai kas ne dujos
    potential_mass_halo = mass_halo * dark_matter_fraction_in_halo
    # darkmattermass = potential_mass_halo * unit_sunmass
    dot_potential_mass_halo = dot_mass_halo * dark_matter_fraction_in_halo
    # dotdot_mass_halo_potential = dotdot_mass_halo * dark_matter_fraction_in_halo
    potential_phi_halo = phi_halo * dark_matter_fraction_in_halo  # gravitacinis potencialas
    potential_phigrad_halo = phigrad_halo * dark_matter_fraction_in_halo

    gas_mass_halo = mass_halo * fraction_of_galaxy_in_halo * halo_gas_fraction
    dot_gas_mass_halo = dot_mass_halo * fraction_of_galaxy_in_halo * halo_gas_fraction
    dotdot_gas_mass_halo = dotdot_mass_halo * fraction_of_galaxy_in_halo * halo_gas_fraction
    gas_phi_halo = phi_halo * fraction_of_galaxy_in_halo * halo_gas_fraction / 2
    gas_phigrad_halo = phigrad_halo * fraction_of_galaxy_in_halo * halo_gas_fraction / 2

    phih = potential_phi_halo + gas_phi_halo
    phigradh = potential_phigrad_halo + gas_phigrad_halo

    rhohgas = rho_halo * fraction_of_galaxy_in_halo * halo_gas_fraction
    rhohgas2 = rho2_halo * fraction_of_galaxy_in_halo * halo_gas_fraction

    whole_bulge_mass = bulge_totalmass * bulge_disc_to_totalmass_fraction * total_mass
    # bulge_scaled = radius / bulge_scale

    isothermal_profile = IsothermalProfile()
    (mass_bulge, dot_mass_bulge, dotdot_mass_bulge, rho_bulge, rho2_bulge, phi_bulge, phi_grad_bulge) = \
        isothermal_profile.calculate_profile(whole_bulge_mass, radius, dot_radius, dotdot_radius, bulge_scale, 10)

    # mb bulgo mases dalis nuo centro iki dabartinio r
    # TODO fix this name
    fraction_of_bulge_mass_within_r = 1 - bulge_disc_gas_fraction

    mass_bulge_potential = mass_bulge * fraction_of_bulge_mass_within_r
    dot_mass_bulge_potential = dot_mass_bulge * fraction_of_bulge_mass_within_r
    # dotdot_mass_bulge_potential = dotdot_mass_bulge * fraction_of_bulge_mass_within_r
    phi_bulge_potential = phi_bulge * fraction_of_bulge_mass_within_r
    phigrad_bulge_potential = phi_grad_bulge * fraction_of_bulge_mass_within_r

    mass_bulge_gas = mass_bulge * bulge_disc_gas_fraction
    dot_mass_bulge_gas = dot_mass_bulge * bulge_disc_gas_fraction
    dotdot_mass_bulge_gas = dotdot_mass_bulge * bulge_disc_gas_fraction
    phi_bulge_gas = phi_bulge * bulge_disc_gas_fraction / 2.
    phigrad_bulge_gas = phi_grad_bulge * bulge_disc_gas_fraction / 2.

    phib = phi_bulge_potential + phi_bulge_gas
    phigradb = phigrad_bulge_potential + phigrad_bulge_gas

    rhobgas = rho_bulge * bulge_disc_gas_fraction
    rhobgas2 = rho2_bulge * bulge_disc_gas_fraction

    # gravitacinio potencialo pokytis
    # deltaphi = 4 * math.pi * (radius ** 2) * (rhohgas + rhobgas) * delta_radius * (
    #         1 + delta_radius / radius + (delta_radius ** 2) / (3. * radius ** 2)) * (phih + phib)

    # sigma = math.sqrt(mass_halo * fraction_of_galaxy_in_halo + mass_bulge / 2 / radius)

    return potential_mass_halo + mass_bulge_potential, dot_potential_mass_halo + dot_mass_bulge_potential, \
           gas_mass_halo + mass_bulge_gas, dot_gas_mass_halo + dot_mass_bulge_gas, \
           dotdot_gas_mass_halo + dotdot_mass_bulge_gas, rhohgas + rhobgas, phih + phib, \
           phigradh + phigradb, rhohgas2 + rhobgas2, mass_bulge
