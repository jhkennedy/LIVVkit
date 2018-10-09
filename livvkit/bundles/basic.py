# coding=utf-8

import os

import xml.etree.ElementTree as xmlTree

from livvkit import data


class CFNameError(ValueError):
    """Raise this when a standard name cannot be found in the CF Standard Name Table.
    """


class Variable(object):
    def __init__(self, name, bundle):
        self.name = name
        self.standard_name = bundle.translate_variable_name(self.name)

        entry = self.locate_cf_standard_name_entry(self.standard_name)

        self.standard_units = entry.find('canonical_units').text
        self.description = entry.find('description').text


    @classmethod
    def locate_cf_standard_name_entry(cls, standard_name):
        cf_dir = os.path.dirname(data.__file__)
        cf_xml = xmlTree.parse(os.path.join(cf_dir, 'cf-standard-name-table.xml'))
        entry = cf_xml.find('entry[@id="{}"]'.format(standard_name))
        if entry is None:
            try:
                alias = cf_xml.find('alias[@id="{}"]'.format(standard_name))
                entry = cf_xml.find('entry[@id="{}"]'.format(alias.find('entry_id').text))
            except AttributeError:
                cf_version = cf_xml.find('version_number').text
                err_str = "Standard name {} could not be found in the " \
                          "CF Standard Name Table version {}"
                raise CFNameError(err_str.format(standard_name, cf_version))
        return entry


class Bundle:
    """
    A basic bundle class.
    """
    def __init__(self):
        """
        init...
        """

    def translate_variable_name(self, name):
        raise NotImplementedError
