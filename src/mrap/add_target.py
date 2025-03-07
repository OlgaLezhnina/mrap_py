from collections.abc import Mapping


def add_target(dt, input_data):
    if isinstance(input_data, Mapping):
        target_name = list(input_data.items())[0][1].name
    target_variable = dt.component(label=target_name)
    return target_variable
