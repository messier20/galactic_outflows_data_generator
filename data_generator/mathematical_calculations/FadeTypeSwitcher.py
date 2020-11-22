import math

import configurations.initial_galaxy_params as init


class FadeTypeSwitcher:
    def __init__(self):
        pass

    def calc_luminosity_coef(self, type, eff_time, quasar_duration, eddingtion_ratio):
        method_name = str(type.value)
        method = getattr(self, method_name, lambda: 'Invalid')
        return method(eff_time, quasar_duration, eddingtion_ratio)

    def none(self, eff_time, quasar_duration, eddingtion_ratio):
        if self.is_eff_time_less_then_quasar_duration(eff_time, quasar_duration):
            return eddingtion_ratio
        else:
            return 0

    def exponential(self, eff_time, quasar_duration, eddingtion_ratio):
        if self.is_eff_time_less_then_quasar_duration(eff_time, quasar_duration):
            return eddingtion_ratio
        else:
            return eddingtion_ratio * math.exp(-(eff_time - quasar_duration) / init.drop_timescale)

    def power_law(self, eff_time, quasar_duration, eddingtion_ratio):
        if self.is_eff_time_less_then_quasar_duration(eff_time, quasar_duration):
            return eddingtion_ratio
        else:
            return eddingtion_ratio * (eff_time / quasar_duration) ** (-1. * init.alpha_drop)

    def king(self, eff_time, quasar_duration, eddingtion_ratio):
        return eddingtion_ratio * (1 + eff_time / quasar_duration) ** (-19. / 16.)

    def is_eff_time_less_then_quasar_duration(self, eff_time, quasar_duration):
        if eff_time <= quasar_duration:
            return True
        else:
            return False
