import sys
from importlib.metadata import version


def add_software_method(dt, lib, fun):
    version_py = str(sys.version)[:5]
    version_lib = version(lib)
    software = dt.software(label="Python", version_info=version_py)
    software_library = dt.software_library(label=lib, version_info=version_lib, part_of=software)
    software_method = dt.software_method(label=fun, part_of=software_library)
    return software_method
