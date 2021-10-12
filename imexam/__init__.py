# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
An Astropy affiliated  package to help perform image examination through a
viewing tool, like DS9
"""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *  # noqa
# ----------------------------------------------------------------------------
from pkg_resources import get_distribution, DistributionNotFound

__all__ = ['__version__', '__githash__']


try:
    from . import imexamxpa  # noqa
    _have_xpa = True
except ImportError:
    _have_xpa = False

if not _ASTROPY_SETUP_:  # noqa
    # import high level functions into the imexam namespace
    if _have_xpa:
        from .util import list_active_ds9, find_path  # noqa
        from .util import display_help, display_xpa_help  # noqa

    from .util import set_logging  # noqa
    from . import connect as _connect
    connect = _connect.Connect

    try:
        import astropy  # noqa
    except ImportError:
        raise ImportError("astropy required but not found")


try:
    release = get_distribution('imexam').version
    __version__ = '.'.join(release.split('.')[:4])
except DistributionNotFound:
    # package is not installed
    __version__ = 'unknown'
    __githash__ = ''
