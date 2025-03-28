from collections.abc import Mapping


def add_target(dt, input_data):
    """
    Write a target instance to be used by other instances

    :param dt: an analytical schema datatype
    :param input_data: pd.DataFrame, a dictionary, or a list with URL, n rows, and n columns
    :return: a target instance
    """
    if isinstance(input_data, Mapping):
        for item in input_data.values():
            target_name = item.name
            break
    else:
        target_name = "TODO"
    target_variable = dt.component(label=target_name)
    return target_variable
