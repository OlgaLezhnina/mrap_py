import sys
from importlib.metadata import version
from .utils import parse_code_list


def add_software_method(dt, code_list):
    version_py = str(sys.version)[:5]
    software = dt.software(label="Python", version_info=version_py)
    if code_list == "N/A":
        software_method = dt.software_method(part_of=software)
    elif isinstance(code_list, list):
        lib = code_list[0]
        fun = parse_code_list(code_list)["fun"]
        version_lib = version(lib)
        software_library = dt.software_library(label=lib, version_info=version_lib,
                                               part_of=software)
        software_method = dt.software_method(label=fun, part_of=software_library,
                                             is_implemented_by=code_list[1])
    else:
        raise TypeError("Argument code_list is of a wrong type, see Readme")
    return software_method
