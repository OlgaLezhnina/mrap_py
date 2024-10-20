import sys
from importlib.metadata import version

dt = None


def add_soft_method(pack, fun):
    global dt
    version_Py = str(sys.version)[:5]
    version_pack = version(pack)
    software = dt.software(label="Python", versionInfo=version_Py)
    soft_library = dt.software_library(label=pack, versionInfo=version_pack, part_of=software)
    soft_method = dt.software_method(label=fun, uses_software=soft_library)
    return soft_method
