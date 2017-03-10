import os
import numpy as np
from ..hselect import Hselect
from astropy.table import Table, MaskedColumn


def test_hselect_basic():

    test_dir = "/eng/ssb/iraf_transition/test_data/"

    data_rows = [('/eng/ssb/iraf_transition/test_data/hselect_test.fits',
                  0, 4.5),
                 ('/eng/ssb/iraf_transition/test_data/hselect_test.fits',
                  1, 10.55),
                 ('/eng/ssb/iraf_transition/test_data/hselect_test.fits',
                  2, 200.0)]
    correct_table = Table(rows=data_rows, names=('Filename', 'Ext', 'A_FLOAT'),
                          dtype=('S80', 'int64', 'float64'))
    add_col = MaskedColumn(np.ma.masked_array(['string', 'string', 'nope'],
                                              mask=[0, 0, 1]), dtype='S68')
    correct_table['A_STRING'] = add_col

    hobj = Hselect(os.path.join(test_dir, 'hselect_test.fits'),
                   'A_FLOAT,A_STRING')

    assert correct_table.colnames == hobj.table.colnames, \
        "Expected Table Cols: {} \n Hselect Returned: {}".format(
            correct_table.colnames, hobj.table.colnames)

    for colname in correct_table.colnames:
        assert np.all(correct_table[colname] == hobj.table[colname])


def test_hselect_expression():

    test_dir = "/eng/ssb/iraf_transition/test_data/"

    data_rows = [('/eng/ssb/iraf_transition/test_data/hselect_test.fits', 0,
                  4.5)]
    correct_table = Table(rows=data_rows, names=('Filename', 'Ext', 'A_FLOAT'),
                          dtype=('S80', 'int64', 'float64'))
    add_col = MaskedColumn(np.ma.masked_array(['string'], mask=[0]),
                           dtype='S68')
    correct_table['A_STRING'] = add_col

    hobj = Hselect(os.path.join(test_dir, 'hselect_test.fits'),
                   'A_FLOAT,A_STRING', extension=(0, 1),
                   expression="A_FLOAT<10")

    assert correct_table.colnames == hobj.table.colnames, \
        "Expected Table Cols: {} \n Hselect Returned: {}".format(
            correct_table.colnames, hobj.table.colnames)

    for colname in correct_table.colnames:
        assert np.all(correct_table[colname] == hobj.table[colname])


def test_hselect_equality():

    test_dir = "/eng/ssb/iraf_transition/test_data/"

    data_rows = [('/eng/ssb/iraf_transition/test_data/hselect_test.fits',
                  0, 4.5),
                 ('/eng/ssb/iraf_transition/test_data/hselect_test.fits',
                  1, 10.55)]
    correct_table = Table(rows=data_rows, names=('Filename', 'Ext', 'A_FLOAT'),
                          dtype=('S80', 'int64', 'float64'))
    add_col = MaskedColumn(np.ma.masked_array(['string', 'string'],
                                              mask=[0, 0]), dtype='S68')
    correct_table['A_STRING'] = add_col

    hobj = Hselect(os.path.join(test_dir, 'hselect_test.fits'),
                   'A_FLOAT,A_STRING',
                   expression='A_STRING="string" AND A_FLOAT > 0')

    assert correct_table.colnames == hobj.table.colnames, \
        "Expected Table Cols: {} \n Hselect Returned: {}".format(
            correct_table.colnames, hobj.table.colnames)

    for colname in correct_table.colnames:
        assert np.all(correct_table[colname] == hobj.table[colname])
