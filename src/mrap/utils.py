import re
from importlib.metadata import metadata
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version


def parse_code_list(code_list):
    """
    Parse two strings from code_list to get information about the software method

    :param code_list: a list of strings for library and code line, "N/A" if not given
    :return: a dictionary with strings as keys and values
    """
    code_str = code_list[1]
    function_name = code_str.split("(")[0]
    if "~" in code_str:
        target_name = code_str.split("(")[1].split("~")[0].strip(' "\'')
    else:
        target_name = None
    result = {"fun": function_name,
              "level_name": "TODO",
              "target_name": target_name}
    return result


def get_comparison_target_name(input_dict):
    """
    Extract a target name from a dictionary

    :param input_dict: a dictionary with pd.Series
    :return: a target name or None
    """
    name_list = []
    for item in input_dict.values():
        if item.name in name_list:
            pass
        else:
            name_list.append(item.name)
    if len(name_list) == 1:
        target_name = name_list[0]
    else:
        target_name = None
    return target_name


def get_library_info(lib):
    """
    Extract a library version and documentation URL

    :param lib: a string which is a Python library
    :return: a dictionary with the library version and URL, or None if not found
    """
    try:
        version(lib)
    except PackageNotFoundError:
        version_lib = None
        url_lib = None
        print("Software library information is not available, please add manually")
    else:
        version_lib = version(lib)
        list_urls = metadata(lib).get_all('Project-URL')
        for entry in list_urls:
            if "documentation" in entry.casefold():
                url_lib = re.search("(https?://\\S+)", entry).group()
                break
        else:
            url_lib = "https://pypi.org/project/" + lib
    library_info = {"version_lib": version_lib,
                    "url_lib": url_lib}
    return library_info


def standardise_keys(old_dict):
    """
    Rewrite dictionary keys (metrics) in standard spelling

    :param old_dict: a dictionary with metrics and values
    :return: a dictionary with standardised metrics and values
    """
    new_dict = {}
    f1_matches = ["f1", "f_1"]
    uppercase = ["auc", "mae", "mse", "rmse"]
    lowercase = ["accuracy", "precision", "recall"]
    for key, value in old_dict.items():
        if any(x in key.casefold() for x in f1_matches):
            new_dict["F1"] = old_dict[key]
        elif key.casefold() in uppercase:
            new_dict[key.upper()] = old_dict[key]
        elif key.casefold() in lowercase:
            new_dict[key.lower()] = old_dict[key]
        else:
            new_dict[key] = old_dict[key]
    return (new_dict)
