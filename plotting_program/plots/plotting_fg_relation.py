import math
import matplotlib.pyplot as plt

import numpy as np

# from model_program.input_parameters.galaxy_parameters import bulge_disc_gas_fractions, bulge_masses
# from plotting_program.plots.plots_settings import graphs_path, plots_version_folder

bulge_disc_gas_fractions_ln = [0 for x in range(len(bulge_disc_gas_fractions))]
def plotting_fg_relation(dot_radius, dot_r_ln, dot_mass, dot_m_ln):
    for ind, item in enumerate(bulge_disc_gas_fractions):
        bulge_disc_gas_fractions_ln[ind] = math.log(item)

    dot_r_ln = np.array(dot_r_ln)

    fitted_dot_radius0 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 0], 1)
    fitted_dot_radius1 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 1], 1)
    fitted_dot_radius2 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 2 ], 1)
    fitted_dot_radius3 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 3], 1)
    fitted_dot_radius4 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 4], 1)
    fitted_dot_radius5 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 5], 1)
    fitted_dot_radius6 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 6], 1)
    fitted_dot_radius7 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 7], 1)
    fitted_dot_radius8 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 8], 1)
    fitted_dot_radius9 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 9], 1)
    fitted_dot_radius10 = np.polyfit(bulge_disc_gas_fractions_ln, dot_r_ln[:, 10], 1)

    fitted_fn0 = np.poly1d(fitted_dot_radius0)
    fitted_fn1 = np.poly1d(fitted_dot_radius1)
    fitted_fn2 = np.poly1d(fitted_dot_radius2)
    fitted_fn3 = np.poly1d(fitted_dot_radius3)
    fitted_fn4 = np.poly1d(fitted_dot_radius4)
    fitted_fn5 = np.poly1d(fitted_dot_radius5)
    fitted_fn6 = np.poly1d(fitted_dot_radius6)
    fitted_fn7 = np.poly1d(fitted_dot_radius7)
    fitted_fn8 = np.poly1d(fitted_dot_radius8)
    fitted_fn9 = np.poly1d(fitted_dot_radius9)
    fitted_fn10 = np.poly1d(fitted_dot_radius10)

    print(fitted_fn10, ' dot radius')

    labels = [r'$mb$ = '+str(format(mass, '.1e')) for mass in bulge_masses]
    fig, ax = plt.subplots()
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, width=1.2, labelsize='large')
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_ylabel('velocity [km/s]', fontsize=14)
    ax.set_xlabel('Bulge gas fractions ', fontsize=14)

    ax.set_ylim(2e1, 1e3)
    ax.set_xlim(0.045, 1.1)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 0 ], label = labels[0], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 1], label = labels[2],  s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 2], label = labels[1],  s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 3], label = labels[3],  s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 4], label = labels[4],  s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 5], label = labels[5],  s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 6], label = labels[6],  s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 7], label = labels[7],  s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 8], label = labels[8],  s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 9], label = labels[9],  s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_radius[:, 10], label = labels[10],  s=7)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn0.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn0.coef[0]), '--', linewidth=1)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn1.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn1.coef[0]), '--', linewidth=1)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn2.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn2.coef[0]), '--', linewidth=1)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn3.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn3.coef[0]), '--', linewidth=1)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn4.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn4.coef[0]), '--', linewidth=1)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn5.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn5.coef[0]), '--', linewidth=1)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn6.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn6.coef[0]), '--', linewidth=1)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn7.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn7.coef[0]), '--', linewidth=1)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn8.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn8.coef[0]), '--', linewidth=1)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn9.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn9.coef[0]), '--', linewidth=1)
    ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fn10.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fn10.coef[0]), '--', linewidth=1)

    ax.legend(loc='upper right')
    # ax.legend(loc='upper left')
    fig.savefig(graphs_path + plots_version_folder + 'velocity-bulge-gas-frac' + '.png', bbox_inches='tight')
    plt.close(fig)


    fitted_dot_m0 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 0], 1)
    fitted_dot_m1 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 1], 1)
    fitted_dot_m2 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 2], 1)
    fitted_dot_m3 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 3], 1)
    fitted_dot_m4 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 4], 1)
    fitted_dot_m5 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 5], 1)
    fitted_dot_m6 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 6], 1)
    fitted_dot_m7 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 7], 1)
    fitted_dot_m8 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 8], 1)
    fitted_dot_m9 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 9], 1)
    fitted_dot_m10 = np.polyfit(bulge_disc_gas_fractions_ln, dot_m_ln[:, 10], 1)

    fitted_fn_dm0 = np.poly1d(fitted_dot_m0)
    fitted_fn_dm1 = np.poly1d(fitted_dot_m1)
    fitted_fn_dm2 = np.poly1d(fitted_dot_m2)
    fitted_fn_dm3 = np.poly1d(fitted_dot_m3)
    fitted_fn_dm4 = np.poly1d(fitted_dot_m4)
    fitted_fn_dm5 = np.poly1d(fitted_dot_m5)
    fitted_fn_dm6 = np.poly1d(fitted_dot_m6)
    fitted_fn_dm7 = np.poly1d(fitted_dot_m7)
    fitted_fn_dm8 = np.poly1d(fitted_dot_m8)
    fitted_fn_dm9 = np.poly1d(fitted_dot_m9)
    fitted_fn_dm10 = np.poly1d(fitted_dot_m10)

    print(fitted_fn_dm10, ' dot m')

    labels = [r'$mb$ = ' + str(format(mass, '.1e')) for mass in bulge_masses]
    fig, ax = plt.subplots()
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, width=1.2, labelsize='large')
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]', fontsize=14)
    ax.set_xlabel('Bulge gas fractions ', fontsize=14)

    ax.set_ylim(2e2, 8e3)
    ax.set_xlim(0.045, 1.1)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 0], label=labels[0], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 1], label=labels[2], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 2], label=labels[1], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 3], label=labels[3], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 4], label=labels[4], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 5], label=labels[5], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 6], label=labels[6], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 7], label=labels[7], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 8], label=labels[8], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 9], label=labels[9], s=7)
    ax.scatter(bulge_disc_gas_fractions, dot_mass[:, 10], label=labels[10], s=7)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm0.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm0.coef[0]), '--',
            linewidth=1)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm1.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm1.coef[0]), '--',
            linewidth=1)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm2.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm2.coef[0]), '--',
            linewidth=1)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm3.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm3.coef[0]), '--',
            linewidth=1)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm4.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm4.coef[0]), '--',
            linewidth=1)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm5.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm5.coef[0]), '--',
            linewidth=1)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm6.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm6.coef[0]), '--',
            linewidth=1)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm7.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm7.coef[0]), '--',
            linewidth=1)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm8.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm8.coef[0]), '--',
            linewidth=1)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm9.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm9.coef[0]), '--',
            linewidth=1)
    ax.plot(bulge_disc_gas_fractions,
            (math.exp(fitted_fn_dm10.coef[1]) * np.array(bulge_disc_gas_fractions) ** fitted_fn_dm10.coef[0]), '--',
            linewidth=1)

    ax.legend(loc='upper left')
    # ax.legend(loc='upper left')
    fig.savefig(graphs_path + plots_version_folder + 'dm-bulge-gas-frac' + '.png', bbox_inches='tight')
    plt.close(fig)