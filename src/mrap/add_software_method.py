import sys
from importlib.metadata import version
from .utils import parse_code_list


def add_software_method(dt, code_list):
    """
    Write a software_method instance to be used by other instances

    :param dt: an analytical schema datatype
    :param code_list: a list of strings for library and code line, "N/A" if not given
    :return: a software_method instance
    """
    vers = sys.version_info
    version_py = str(vers[0]) + "." + str(vers[1]) + "." + str(vers[2])
    software = dt.software(label="Python",
                           version_info=version_py,
                           has_support_url="https://www.python.org")
    if code_list == "N/A":
        software_method = dt.software_method(part_of=software)
    elif isinstance(code_list, list):
        lib = code_list[0]
        fun = parse_code_list(code_list)["fun"]
        version_lib = version(lib)
        url_lib = "https://pypi.org/project/" + lib + "/#documentation"
        software_library = dt.software_library(label=lib,
                                               version_info=version_lib,
                                               has_support_url=url_lib,
                                               part_of=software)
        software_method = dt.software_method(label=fun, part_of=software_library,
                                             is_implemented_by=code_list[1])
    else:
        raise TypeError("Argument code_list is of a wrong type, see Readme")
    return software_method
