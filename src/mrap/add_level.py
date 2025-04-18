from .utils import parse_code_list


def add_level(dt, code_list):
    """
    Write a level instance

    :param dt: an analytical schema datatype
    :param code_list: a list of strings for library and code line, "N/A" if not given
    :return: a level instance
    """
    level_name = parse_code_list(code_list)["level_name"]
    level_variable = dt.component(label=level_name)
    return level_variable
