from plotting_program.plots.PlotSetup import PlotSetup
import matplotlib.pyplot as plt
import numpy as np


def generic_time_relation_plot(outflow_props_table):
    Plot = PlotSetup()
    #
    fig1, ax1 = Plot.setup_time_rel()
    colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
    for i, outflow_props in enumerate(outflow_props_table):
        ax1.set_ylim(1.e-2, 1.e2)
        ax1.set_ylabel('radius [$kpc$]', fontsize=14)
        ax1.plot(outflow_props.time_arr.values, outflow_props.radius_arr.values, c=colors[i])
    plt.show()