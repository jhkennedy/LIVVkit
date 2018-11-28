# coding=utf-8

import os
import xarray as xr

from livvkit.util import functions as fn
from livvkit.bundles.basic import Bundle, CFNameError, BundleValueError


class ModelBundle(Bundle):
    def __init__(self, name, data_dir):
        super(ModelBundle, self).__init__()

        self.name = name
        self.data_dir = data_dir

        self.bundle_dir = os.path.dirname(__file__)
        self.name = os.path.basename(self.bundle_dir)

        self.var_name_cf_translations = fn.read_json(os.path.join(self.bundle_dir, 'vars_missing_stdname.json'))
        self.var_name_cf_translations.update({value: key for key, value in self.var_name_cf_translations.items()})

        self._component_file = os.path.join(self.bundle_dir, 'components.json')
        self.compenent_defs = fn.read_json(self._component_file)


    def load_component(self, component):
        try:
            glob = self.compenent_defs[component]['glob']
        except KeyError:
            raise BundleValueError('Component {} does not exist in bundle {}. Check component definition for '
                                   'correctness: {}'.format(component, self.name, self._component_file))
        return xr.open_mfdataset(glob)


    def translate_variable_name(self, var_name):
        try:
            translation = self.var_name_cf_translations[var_name]
        except KeyError:
            err_str = "{} bundle does not have a {} variable defined."
            raise CFNameError(err_str.format(self.name, var_name))
        return translation
