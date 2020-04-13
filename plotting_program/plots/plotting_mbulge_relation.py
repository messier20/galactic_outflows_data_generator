import math

import matplotlib.pyplot as plt
import numpy as np
from sympy import S, symbols, printing
from scipy.interpolate import UnivariateSpline
# from model_program.input_parameters.galaxy_parameters import bulge_masses, bulge_disc_gas_fractions
# from plotting_program.plots.plots_settings import graphs_path, plots_version_folder
# from plotting_program.turning_plots_on_off import dm_bm_on, average_dm_bm_on

dot_mass_ln = []
bulge_masses_ln = [0 for x in range(len(bulge_masses))]
bulge_disc_gas_fractions_ln = [0 for x in range(len(bulge_disc_gas_fractions))]
def plotting_mbulge_relation(dot_mass, dot_radius, dot_mass_ln, dot_r_ln, additional_name):
    colors = ['black', 'b', 'g', 'r', 'orange']
  ###############################################################################################
    # print(np.array(dot_mass[:, 0]).shape)
    # dot_mass_ln = math.log(dot_mass)
    # for massArr in dot_mass:
    #     for massArr in range
    #     dot_mass_ln = math.log(dot_mass)

    if average_dm_bm_on:

        for ind, item in enumerate(bulge_masses):
            bulge_masses_ln[ind] = math.log(item)


        fitted_dot_mass0 = np.polyfit(bulge_masses_ln, dot_mass_ln[0], 1)
        fitted_dot_mass1 = np.polyfit(bulge_masses_ln, dot_mass_ln[1], 1)
        fitted_dot_mass2 = np.polyfit(bulge_masses_ln, dot_mass_ln[2], 1)
        fitted_dot_mass3 = np.polyfit(bulge_masses_ln, dot_mass_ln[3], 1)
        fitted_dot_mass4 = np.polyfit(bulge_masses_ln, dot_mass_ln[4], 1)

        # fitted_dot_mass0_n = np.polyfit(bulge_masses, dot_mass[0], 1)
        # fitted_dot_mass1_n = np.polyfit(bulge_masses, dot_mass[1], 1)
        # fitted_dot_mass2_n = np.polyfit(bulge_masses, dot_mass[2], 1)
        # fitted_dot_mass3_n = np.polyfit(bulge_masses, dot_mass[3], 1)
        # fitted_dot_mass4_n = np.polyfit(bulge_masses, dot_mass[4], 1)


        fitted_fn = np.poly1d(fitted_dot_mass0)
        fitted_fn1 = np.poly1d(fitted_dot_mass1)
        fitted_fn2 = np.poly1d(fitted_dot_mass2)
        fitted_fn3 = np.poly1d(fitted_dot_mass3)
        fitted_fn4 = np.poly1d(fitted_dot_mass4)
        fitavg = (fitted_dot_mass0[0] + fitted_dot_mass1[0] +fitted_dot_mass2[0]+fitted_dot_mass3[0]+fitted_dot_mass4[0])/5


        fitted_dot_radius0 = np.polyfit(bulge_masses_ln, dot_r_ln[0], 1)
        fitted_dot_radius1 = np.polyfit(bulge_masses_ln, dot_r_ln[1], 1)
        fitted_dot_radius2 = np.polyfit(bulge_masses_ln, dot_r_ln[2], 1)
        fitted_dot_radius3 = np.polyfit(bulge_masses_ln, dot_r_ln[3], 1)
        fitted_dot_radius4 = np.polyfit(bulge_masses_ln, dot_r_ln[4], 1)


        fitted_fn_r = np.poly1d(fitted_dot_radius0)
        fitted_fn_r1 = np.poly1d(fitted_dot_radius1)
        fitted_fn_r2 = np.poly1d(fitted_dot_radius2)
        fitted_fn_r3 = np.poly1d(fitted_dot_radius3)
        fitted_fn_r4 = np.poly1d(fitted_dot_radius4)


        fitting_bulge = np.array(bulge_masses)**fitavg
        # print(dot_mass[0], ' d')
        # print(fitting_bulge)


        labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
        # fit_labels = [r'$\dot{M}$ =' + str(fitted_dot_mass0[0]) + '*M_{bulge}^2']

        colors = ['black', 'b', 'g', 'r', 'orange']
        fig, ax = plt.subplots()

        dot_mass = np.array(dot_mass)
        ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, width=1.2, labelsize='large')
        ax.set_yscale('log')
        ax.set_xscale('log')
        ax.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]', fontsize=14)
        ax.set_xlabel('Bulge mass [$M_{sun}$]', fontsize=14)
        ax.set_ylim(700, 10000)
        ax.set_xlim(1.8e10, 8.e11)
        # ax.plot([bulge_masses,bulge_masses,bulge_masses,bulge_masses,bulge_masses], [dot_mass[0,], dot_mass[1,], dot_mass[2,], dot_mass[3,], dot_mass[4,]])
        ax.scatter(bulge_masses, dot_mass[0,], label = labels[0], color = colors[0], s=7)
        ax.scatter(bulge_masses, dot_mass[1,], label = labels[1], color = colors[1], s=7)
        ax.scatter(bulge_masses, dot_mass[2,], label = labels[2], color = colors[2], s=7)
        ax.scatter(bulge_masses, dot_mass[3,], label = labels[3], color = colors[3], s=7)
        ax.scatter(bulge_masses, dot_mass[4,], label = labels[4], color = colors[4], s=7)

        ax.plot(bulge_masses, (math.exp(fitted_fn.coef[1])*np.array(bulge_masses)**fitted_fn.coef[0]), '--', color=colors[0], linewidth=1, label='sąryšis 1')
        ax.plot(bulge_masses, (math.exp(fitted_fn1.coef[1])*np.array(bulge_masses)**fitted_fn1.coef[0]), '--', color=colors[1], linewidth=1, label='sąryšis 2')
        ax.plot(bulge_masses, (math.exp(fitted_fn2.coef[1])*np.array(bulge_masses)**fitted_fn2.coef[0]), '--', color=colors[2], linewidth=1, label='sąryšis 3')
        ax.plot(bulge_masses, (math.exp(fitted_fn3.coef[1])*np.array(bulge_masses)**fitted_fn3.coef[0]), '--', color=colors[3], linewidth=1, label='sąryšis 3')
        ax.plot(bulge_masses, (math.exp(fitted_fn4.coef[1])*np.array(bulge_masses)**fitted_fn4.coef[0]), '--', color=colors[4], linewidth=1, label='sąryšis 3')
        # ax.plot(bulge_masses, fitted_fn1(bulge_masses), '--', color=colors[1], linewidth=1, label='sąryšis 2')
        # ax.plot(bulge_masses, fitted_fn2(bulge_masses), '--', color=colors[2], linewidth=1, label='sąryšis 3')
        # ax.plot(bulge_masses, fitted_fn3(bulge_masses), '--', color=colors[3], linewidth=1, label='sąryšis 4')
        # ax.plot(bulge_masses, fitted_fn4(bulge_masses), '--', color=colors[4], linewidth=1, label='sąryšis 5')
        # ax.plot(bulge_masses, y, 'o', color='red', linewidth=0.7)

        # ax.plot(bulge_masses, dot_mass[2,], '--', color=colors[2], linewidth=1)
        # ax.plot(bulge_masses, dot_mass[3,], '--', color=colors[3], linewidth=1)
        # ax.plot(bulge_masses, dot_mass[4,], '--', color=colors[4], linewidth=1)
        ax.legend(loc='upper right')
        # ax.legend(loc='upper left')
        fig.savefig(graphs_path + plots_version_folder + 'dot-mass-bulge-mass-' + additional_name + '-fix-fit-ln.png', bbox_inches='tight')
        plt.close(fig)



        l1 = math.exp(fitted_fn_r.coef[1])*np.array(bulge_masses)**fitted_fn_r.coef[0]
        l2 = math.exp(fitted_fn_r1.coef[1])*np.array(bulge_masses)**fitted_fn_r1.coef[0]
        l3 = math.exp(fitted_fn_r2.coef[1])*np.array(bulge_masses)**fitted_fn_r2.coef[0]
        l4 = math.exp(fitted_fn_r3.coef[1])*np.array(bulge_masses)**fitted_fn_r3.coef[0]
        l5 = math.exp(fitted_fn_r4.coef[1])*np.array(bulge_masses)**fitted_fn_r4.coef[0]

        fig, ax = plt.subplots()
        dot_radius = np.array(dot_radius)
        ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, width=1.2, labelsize='large')
        ax.set_yscale('log')
        ax.set_xscale('log')

        ax.set_xlim(1.9e10, 9e11)
        ax.set_ylim(200, 1600)
        ax.set_ylabel('Velocity [km/s]', fontsize=14)
        ax.set_xlabel('Bulge mass [$M_{sun}$]', fontsize=14)
        ax.scatter(bulge_masses, dot_radius[0,], label = labels[0], color = colors[0], s=7)
        ax.scatter(bulge_masses, dot_radius[1,], label = labels[1], color = colors[1], s=7)
        ax.scatter(bulge_masses, dot_radius[2,], label = labels[2], color = colors[2], s=7)
        ax.scatter(bulge_masses, dot_radius[3,], label = labels[3], color = colors[3], s=7)
        ax.scatter(bulge_masses, dot_radius[4,], label = labels[4], color = colors[4], s=7)

        ax.plot(bulge_masses, l1, '--', color=colors[0], linewidth=1, label='sąryšis 1')
        ax.plot(bulge_masses, l2, '--', color=colors[1], linewidth=1, label='sąryšis 2')
        ax.plot(bulge_masses, l3, '--', color=colors[2], linewidth=1, label='sąryšis 3')
        ax.plot(bulge_masses, l4, '--', color=colors[3], linewidth=1, label='sąryšis 4')
        ax.plot(bulge_masses, l5, '--', color=colors[4], linewidth=1, label='sąryšis 5')

        # ax.plot(bulge_masses, dot_radius[0,], '--', color=colors[0], linewidth=1)
        # ax.plot(bulge_masses, dot_radius[1,], '--', color=colors[1], linewidth=1)
        # ax.plot(bulge_masses, dot_radius[2,], '--', color=colors[2], linewidth=1)
        # ax.plot(bulge_masses, dot_radius[3,], '--', color=colors[3], linewidth=1)
        # ax.plot(bulge_masses, dot_radius[4,], '--', color=colors[4], linewidth=1)
        ax.legend(loc='upper right')

        fig.savefig(graphs_path + plots_version_folder + 'dot-radius-bulge-mass-' + additional_name + '-fix-fit-ln.png',
                    bbox_inches='tight')
        plt.close(fig)


###############################################################################################

    # # fitted_dot_radius0 = np.polyfit(bulge_masses, dot_radius[0], 2)
    # # fitted_dot_radius1 = np.polyfit(bulge_masses, dot_radius[1], 2)
    # # fitted_dot_radius2 = np.polyfit(bulge_masses, dot_radius[2], 2)
    # # fitted_dot_radius3 = np.polyfit(bulge_masses, dot_radius[3], 2)
    # # fitted_dot_radius4 = np.polyfit(bulge_masses, dot_radius[4], 2)
    # #
    # # fitted_fn_r = np.poly1d(fitted_dot_radius0)
    # # fitted_fn_r1 = np.poly1d(fitted_dot_radius1)
    # # fitted_fn_r2 = np.poly1d(fitted_dot_radius2)
    # # fitted_fn_r3 = np.poly1d(fitted_dot_radius3)
    # # fitted_fn_r4 = np.poly1d(fitted_dot_radius4)
    # # print(fitted_fn_r)
    # # print(fitted_fn_r1)
    # # print(fitted_fn_r2)
    # # print(fitted_fn_r3)
    # # print(fitted_fn_r4)
    #
    # # ###################
    # for ind, item in enumerate(bulge_disc_gas_fractions):
    #     bulge_disc_gas_fractions_ln[ind] = math.log(item)
    #
    # # fitted_dot_mass0 = np.polyfit(bulge_masses_ln, dot_mass_ln[0], 1)
    # # fitted_dot_mass1 = np.polyfit(bulge_masses_ln, dot_mass_ln[1], 1)
    # # fitted_dot_mass2 = np.polyfit(bulge_masses_ln, dot_mass_ln[2], 1)
    # # fitted_dot_mass3 = np.polyfit(bulge_masses_ln, dot_mass_ln[3], 1)
    # # fitted_dot_mass4 = np.polyfit(bulge_masses_ln, dot_mass_ln[4], 1)
    #
    # print(bulge_disc_gas_fractions_ln)
    # print(dot_radius[0])
    # fg_fitted_dot_radius0 = np.polyfit(bulge_disc_gas_fractions_ln, dot_radius[0], 1)
    # fg_fitted_dot_radius1 = np.polyfit(bulge_disc_gas_fractions_ln, dot_radius[1], 1)
    # fg_fitted_dot_radius2 = np.polyfit(bulge_disc_gas_fractions_ln, dot_radius[2], 1)
    # fg_fitted_dot_radius3 = np.polyfit(bulge_disc_gas_fractions_ln, dot_radius[3], 1)
    # fg_fitted_dot_radius4 = np.polyfit(bulge_disc_gas_fractions_ln, dot_radius[4], 1)
    #
    # fitted_fg0 = np.poly1d(fg_fitted_dot_radius0)
    # fitted_fg1 = np.poly1d(fg_fitted_dot_radius1)
    # fitted_fg2 = np.poly1d(fg_fitted_dot_radius2)
    # fitted_fg3 = np.poly1d(fg_fitted_dot_radius3)
    # fitted_fg4 = np.poly1d(fg_fitted_dot_radius4)
    # print(fitted_fg4, ' fit')
    #
    # # fg_fitted0 = np.polyfit1s(fg_fitted_dot_radius0)
    # # fg_fitted1 = np.polyfit1s(fg_fitted_dot_radius1)
    # # fg_fitted2 = np.polyfit1s(fg_fitted_dot_radius2)
    # # fg_fitted3 = np.polyfit1s(fg_fitted_dot_radius3)
    # # fg_fitted4 = np.polyfit1s(fg_fitted_dot_radius4)
    #
    # # fitavg = (fitted_dot_mass0[0] + fitted_dot_mass1[0] + fitted_dot_mass2[0] + fitted_dot_mass3[0] + fitted_dot_mass4[
    # #     0]) / 5
    # # print(fitted_fn)
    # # print(fitted_fn1)
    # # print(fitted_fn2)
    # # print(fitted_fn3)
    # # print(fitted_fn4)
    # # print(fitavg, ' fitavg')
    #
    # # fitted_dot_radius0 = np.polyfit(bulge_masses_ln, dot_r_ln[0], 1)
    # # fitted_dot_radius1 = np.polyfit(bulge_masses_ln, dot_r_ln[1], 1)
    # # fitted_dot_radius2 = np.polyfit(bulge_masses_ln, dot_r_ln[2], 1)
    # # fitted_dot_radius3 = np.polyfit(bulge_masses_ln, dot_r_ln[3], 1)
    # # fitted_dot_radius4 = np.polyfit(bulge_masses_ln, dot_r_ln[4], 1)
    # #
    # # fitted_fn_r = np.poly1d(fitted_dot_radius0)
    # # fitted_fn_r1 = np.poly1d(fitted_dot_radius1)
    # # fitted_fn_r2 = np.poly1d(fitted_dot_radius2)
    # # fitted_fn_r3 = np.poly1d(fitted_dot_radius3)
    # # fitted_fn_r4 = np.poly1d(fitted_dot_radius4)
    # # fitavg_R = (fitted_dot_radius0[0] + fitted_dot_radius1[0] + fitted_dot_radius2[0] + fitted_dot_radius3[0] +
    # #             fitted_dot_radius4[
    # #                 0]) / 5
    # # print(fitavg_R, ' avg r')
    # # # print(fitted_fn_r)
    # # # print(fitted_fn_r1)
    # # # print(fitted_fn_r2)
    # # # print(fitted_fn_r3)
    # # # print(fitted_fn_r4)
    # # 333##################################
    #
    #
    #
    #
    #
    # labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    # # fit_labels = [r'$\dot{M}$ =' + str(fitted_dot_mass0[0]) + '*M_{bulge}^2']
    # colors = ['black', 'b', 'g', 'r', 'orange']
    # fig, ax = plt.subplots()
    # # print()
    # dot_mass = np.array(dot_mass)
    # ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, width=1.2, labelsize='large')
    # ax.set_yscale('log')
    # ax.set_xscale('log')
    # ax.set_ylabel('velocity [km/s]', fontsize=14)
    # ax.set_xlabel('Bulge gas fractions ', fontsize=14)
    # # print(dot_mass)
    # # ax.set_ylim(4e2, 1e3)
    # # ax.set_xlim(0.03, 1.1)
    # # ax.plot([bulge_masses,bulge_masses,bulge_masses,bulge_masses,bulge_masses], [dot_mass[0,], dot_mass[1,], dot_mass[2,], dot_mass[3,], dot_mass[4,]])
    # print(bulge_disc_gas_fractions)
    # # print(dot_radius.shape)
    # ax.scatter(bulge_disc_gas_fractions, dot_radius[0, ], label = labels[0], color = colors[0], s=7)
    # ax.scatter(bulge_disc_gas_fractions, dot_radius[1,], label = labels[2], color = colors[2], s=7)
    # ax.scatter(bulge_disc_gas_fractions, dot_radius[2,], label = labels[1], color = colors[1], s=7)
    # ax.scatter(bulge_disc_gas_fractions, dot_radius[3,], label = labels[3], color = colors[3], s=7)
    # ax.scatter(bulge_disc_gas_fractions, dot_radius[4,], label = labels[4], color = colors[4], s=7)
    # ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fg0.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fg0.coef[0]), '--', color=colors[0], linewidth=1, label='sąryšis 1')
    # ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fg1.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fg1.coef[0]), '--', color=colors[1], linewidth=1, label='sąryšis 2')
    # ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fg2.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fg2.coef[0]), '--', color=colors[2], linewidth=1, label='sąryšis 3')
    # ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fg3.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fg3.coef[0]), '--', color=colors[3], linewidth=1, label='sąryšis 4')
    # ax.plot(bulge_disc_gas_fractions, (math.exp(fitted_fg4.coef[1])*np.array(bulge_disc_gas_fractions)**fitted_fg4.coef[0]), '--', color=colors[4], linewidth=1, label='sąryšis 5')
    # # ax.plot(bulge_masses, y, 'o', color='red', linewidth=0.7)
    #
    # # ax.plot(bulge_masses, dot_mass[2,], '--', color=colors[2], linewidth=1)
    # # ax.plot(bulge_masses, dot_mass[3,], '--', color=colors[3], linewidth=1)
    # # ax.plot(bulge_masses, dot_mass[4,], '--', color=colors[4], linewidth=1)
    # ax.legend(loc='upper right')
    # # ax.legend(loc='upper left')
    # fig.savefig(graphs_path + plots_version_folder + 'velocity-bulge-gas-frac' + additional_name + '.png', bbox_inches='tight')
    # plt.close(fig)