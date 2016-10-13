def test_primes():
    from ..example_mod import primes
    assert primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_deprecation():
    import warnings
    warnings.warn(
        "This is deprecated, but shouldn't raise an exception, unless "
        "enable_deprecations_as_exceptions() called from conftest.py",
        DeprecationWarning)

'''
def test_hselect_basic():
    from ..hselect import Hselect
    from astropy.table import Table
    import numpy as np

    test_dir = "/eng/ssb/iraf_transition/test_data/"

    data_rows = [('/eng/ssb/iraf_transition/test_data/iczgs3y5q_flt.fits', 1, 'ELECTRONS/S'),
                 ('/eng/ssb/iraf_transition/test_data/iczgs3y5q_flt.fits', 2, 'ELECTRONS/S')]
    correct_table = Table(rows=data_rows, names=('Filename', 'ExtNumber', 'BUNIT'),
                          dtype=('S80', 'int64', 'S68'))
    hobj = Hselect(test_dir+'iczgs3y5q_flt.fits', 'BUNIT', extension='1,2')

    for colname in correct_table.colnames:
        assert np.all(correct_table[colname] == hobj.table[colname])



def test_hselect_wildcard():
    from ..hselect import Hselect
    from astropy.table import Table
    import numpy as np

    test_dir = "/eng/ssb/iraf_transition/test_data/"

    data_rows = [('/eng/ssb/iraf_transition/test_data/iczgs3y5q_flt.fits', 0,
                  'iczgs3y5q_flt.fits', 'SCI')]
    correct_table = Table(rows=data_rows, names=('Filename', 'ExtNumber', 'FILENAME', 'FILETYPE'),
                          dtype=('S80', 'int64', 'S68', 'S68'))
    hobj = Hselect(test_dir+'iczgs3y5q_*.fits', 'FILE*', extension='0')

    for colname in correct_table.colnames:
        assert np.all(correct_table[colname] == hobj.table[colname])


def test_eval_keyword_greaterthen_equal():
    from ..hselect import Hselect
    from astropy.table import Table
    import numpy as np

    test_dir = "/eng/ssb/iraf_transition/test_data/"

    data_rows = [('/eng/ssb/iraf_transition/test_data/iczgs3y5q_flt.fits', 0,
                  652.937744)]
    correct_table = Table(rows=data_rows, names=('Filename', 'ExtNumber', 'EXPTIME'),
                          dtype=('S80', 'int64', 'float64'))
    hobj = Hselect(test_dir + 'icz*', 'BUNIT,EXPTIME', expr="EXPTIME >= 620")

    for colname in correct_table.colnames:
        assert np.all(correct_table[colname] == hobj.table[colname])

    # array values - numpy.allclose(), might want to use
'''
