from collections.abc import Mapping


def add_target(dt, input_data):
    if isinstance(input_data, Mapping):
        for item in input_data.values():
            target_name = item.name
            break
    target_variable = dt.component(label=target_name)
    return target_variable
