# coding=utf-8

import os

from livvkit.util import functions as fn
from livvkit.bundles.basic import Bundle, CFNameError


class ModelBundle(Bundle):
    def __init__(self):
        super(ModelBundle, self).__init__()
        self.data_dir = os.path.dirname(__file__)
        self.name = os.path.basename(self.data_dir)

        self.var_name_cf_translations = fn.read_json(os.path.join(self.data_dir, 'var_cf_standard_names.json'))
        self.var_name_cf_translations.update({value: key for key, value in self.var_name_cf_translations.items()})


    def translate_variable_name(self, var_name):
        try:
            translation = self.var_name_cf_translations[var_name]
        except KeyError:
            err_str = "{} bundle does not have a {} variable defined."
            raise CFNameError(err_str.format(self.name, var_name))
        return translation
