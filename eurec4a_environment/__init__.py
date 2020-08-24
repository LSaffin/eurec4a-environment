from ._version import get_versions
from .nomenclature import get_field_by_name
from .units import convert_units

__version__ = get_versions()["version"]
del get_versions


def get_field(ds, field_name, units=None):
    """
    Get field described by `field_name` in dataset `ds` and ensure it is in the
    units defined by `units` (if `units` != None). The units definition is any
    unit definition supported by
    [UDUNITS](https://www.unidata.ucar.edu/software/udunits/)
    """
    da = get_field_by_name(ds, field_name)

    if units is None:
        return da
    else:
        return convert_units(da, units)
