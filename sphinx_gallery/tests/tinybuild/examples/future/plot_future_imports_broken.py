"""
Test without __future__ imports
-------------------------------

Test that __future__ imports inside sphinx_gallery modules does not affect the
parsing of this script.
"""


import sys
# SyntaxError on Python 2
print(3/2, end='')

if PY3_OR_LATER := sys.version_info[0] >= 3:
    raise RuntimeError('Forcing this example to fail on Python 3')
