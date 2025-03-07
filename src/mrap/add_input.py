import pandas as pd
from collections.abc import Mapping
from varname import argname

inputs = None


def add_input(dt, input_data):
    global inputs
    if isinstance(input_data, Mapping):
        inputs = []
        for key in input_data:
            inp_inst = dt.data_item(label=key,
                                    has_characteristic=dt.matrix_size(
                                        number_of_rows="TODO1",
                                        number_of_columns='TODO2'))
            inputs.append(inp_inst)
    elif isinstance(input_data, pd.DataFrame):
        input_label = argname('input_data')
        inputs = dt.data_item(label=input_label,
                              has_characteristic=dt.matrix_size(
                                  number_of_rows="TODO1",
                                  number_of_columns='TODO2'))
    return inputs
