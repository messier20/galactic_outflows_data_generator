import matplotlib.pyplot as plt
class PlotSetup:
    def __init__(self):
        pass

    def setup_time_rel(self):
        # fig, ax = plt.subplots()
        # ax.tick_params(axis='both', which='both', direction='in', top=True, right=True)
        fig, ax = self.setup_common_properties()

        ax.set_xlim(1e3, 1e8)
        ax.set_yscale('log')
        ax.set_xscale('log')
        ax.set_xlabel('time [$yr$]', fontsize=14)

        return fig, ax
    def setup_LAGN_rel(self):
        # fig, ax = plt.subplots()
        # ax.tick_params(axis='both', which='both', direction='in', top=True, right=True)
        fig, ax = self.setup_common_properties()

        # ax.set_xlim(3800, 4400)
        # ax.set_xlabel('time [$yr$]')

        return fig, ax

    def setup_histogram(self, model_name):
        fig, ax = self.setup_common_properties()
        ax.set_ylabel('count')
        ax.set_title(model_name + '$x10^{9}$')

        return fig, ax

    def add_legend_gas_fractions(self, ax, *lines):
        return ax.legend(lines,
                   (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'),
                   markerscale=7)

    def setup_common_properties(self):
        fig, ax = plt.subplots()
        ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, width=1.2, labelsize='large')

        return fig, ax

    def plotting(self, ax, arr1, arr2, colors, labels):
        ax.plot(arr1[:, 0], arr2[:, 0], color=colors[0], label=labels[0])
        ax.plot(arr1[:, 1], arr2[:, 1], color=colors[1], label=labels[1])
        ax.plot(arr1[:, 2], arr2[:, 2], color=colors[2], label=labels[2])
        ax.plot(arr1[:, 3], arr2[:, 3], color=colors[3], label=labels[3])
        ax.plot(arr1[:, 4], arr2[:, 4], color=colors[4], label=labels[4])

    # def advanced_plotting(self, ax, arr1, arr2, range):
        # for i in range(arr1):
        #     ax.plot()


