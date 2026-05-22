from pathlib import Path

from aiidalab_qe.common.panel import PluginOutline

from .model import Wannier90ConfigurationSettingsModel
from .resources import Wannier90ResourceSettingsModel, Wannier90ResourceSettingsPanel
from .result import Wannier90ResultsModel, Wannier90ResultsPanel
from .setting import Wannier90ConfigurationSettingPanel
from .workchain import workchain_and_builder


class PluginOutline(PluginOutline):
    title = 'Wannier functions'


wannier90 = {
    'outline': PluginOutline,
    'configuration': {
        'panel': Wannier90ConfigurationSettingPanel,
        'model': Wannier90ConfigurationSettingsModel,
    },
    'resources': {
        'panel': Wannier90ResourceSettingsPanel,
        'model': Wannier90ResourceSettingsModel,
    },
    'workchain': workchain_and_builder,
    'result': {
        'panel': Wannier90ResultsPanel,
        'model': Wannier90ResultsModel,
    },
    'guides': {
        'title': 'Wannier functions',
        'path': Path(__file__).resolve().parent / 'guides',
    },
}
