import sys
from dtreg.load_datatype import load_datatype


def add_soft_method(method_name):
    version = str(sys.version)[:5]
    soft_all = load_datatype("https://doi.org/21.T11969/abef9f1c0d48853f3e51")
    software = soft_all.software(label="Python", versioninfo=version)
    soft_library = soft_all.software_library(label=method_name, part_of=software)
    soft_method = soft_all.software_method(label=method_name, uses_software=soft_library)
    return soft_method
