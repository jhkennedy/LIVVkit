# coding=utf-8

from __future__ import absolute_import, print_function, unicode_literals

import pytest

from livvkit.bundles import basic
from livvkit.bundles.e3sm_mali import ModelBundle


def test_basic_standard_name_with_alias_lookup():
    standard_alias = 'lwe_large_scale_precipitation_rate'
    entry = basic.Variable.locate_cf_standard_name_entry(standard_alias)

    assert entry.attrib['id'] == 'lwe_stratiform_precipitation_rate'


def test_basic_variable_creation():
    name = 'vx'
    bundle = ModelBundle()

    vx = basic.Variable(name, bundle)

    assert vx.standard_units == 'm s-1'


def test_basic_variable_creation_failure():
    name = 'boogers'
    bundle = ModelBundle()

    with pytest.raises(basic.CFNameError) as boogers:
        basic.Variable(name, bundle)

