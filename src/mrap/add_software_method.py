import sys
from importlib.metadata import version
from .utils import parse_code_list


def add_software_method(dt, code_list):
    lib = code_list[0]
    fun = parse_code_list(code_list)["fun"]
    version_py = str(sys.version)[:5]
    version_lib = version(lib)
    software = dt.software(label="Python", version_info=version_py)
    software_library = dt.software_library(label=lib, version_info=version_lib,
                                           part_of=software)
    software_method = dt.software_method(label=fun, part_of=software_library,
                                         is_implemented_by=code_list[1])
    return software_method
