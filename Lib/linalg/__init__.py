#
# linalg - Linear algebra routines
#

from info import __doc__
from linalg_version import linalg_version as __version__

from basic import *
from decomp import *
from matfuncs import *
from blas import *
from iterative import *

__all__ = filter(lambda s:not s.startswith('_'),dir())

from numpy.dual import register_func
for k in ['inv', 'svd', 'solve', 'det', 'eig', 'eigvals', 'lstsq',
          'pinv', 'cholesky']:
    register_func(k, eval(k))
del k, register_func

from numpy.testing import ScipyTest
test = ScipyTest().test
