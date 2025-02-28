import sys
from importlib.metadata import version


def add_soft_method(dt, lib, fun):
    version_py = str(sys.version)[:5]
    version_lib = version(lib)
    software = dt.software(label="Python", version_info=version_py)
    soft_library = dt.software_library(label=lib, version_info=version_lib, part_of=software)
    soft_method = dt.software_method(label=fun, part_of=soft_library)
    return soft_method
