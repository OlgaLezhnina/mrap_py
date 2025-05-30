import pandas as pd
from collections.abc import Mapping
from .utils import parse_code_list


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


def add_comparison_target(dt, code_list, input_data):
    """
    Write a target instance for group_comparison

    :param dt: an analytical schema datatype
    :param code_list: a list of strings for library and code line, "N/A" if not given
    :param input_data: pd.DataFrame, a dictionary, or a list with URL, n rows, and n columns
    :return: a target instance
    """
    if isinstance(input_data, Mapping):
        target_name = get_comparison_target_name(input_data)
    elif isinstance(input_data, pd.DataFrame):
        target_name = parse_code_list(code_list)["target_name"]
    else:
        target_name = None
    target_variable = dt.component(label=target_name)
    return target_variable


def add_generic_target(dt, code_list, input_data):
    """
    Write a target instance

    :param dt: an analytical schema datatype
    :param code_list: a list of strings for library and code line, "N/A" if not given
    :param input_data: pd.DataFrame, a dictionary, or a list with URL, n rows, and n columns
    :return: a target instance
    """
    target_name = parse_code_list(code_list)["target_name"]
    target_variable = dt.component(label=target_name)
    return target_variable
