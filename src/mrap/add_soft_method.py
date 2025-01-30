import sys
from importlib.metadata import version


def add_soft_method(dt, lib_fun):
    lib = lib_fun.split(",")[0]
    version_py = str(sys.version)[:5]
    version_lib = version(lib)
    software = dt.software(label="Python", versionInfo=version_py)
    soft_library = dt.software_library(label=lib, versionInfo=version_lib, part_of=software)
    soft_method = dt.software_method(label=lib_fun, part_of=soft_library)
    return soft_method
