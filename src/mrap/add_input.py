import pandas as pd
from collections.abc import Mapping
from varname import argname


def add_input(dt, input_data):
    if isinstance(input_data, Mapping):
        inputs = []
        for key in input_data:
            inp_inst = dt.data_item(
                label=key,
                has_characteristic=dt.matrix_size(
                    number_of_rows=len(input_data[key]),
                    number_of_columns=1
                )
            )
            inputs.append(inp_inst)
    elif isinstance(input_data, pd.DataFrame):
        nrows, ncols = input_data.shape
        input_label = argname('input_data')
        inputs = dt.data_item(
            label=input_label,
            has_characteristic=dt.matrix_size(
                number_of_rows=nrows,
                number_of_columns=ncols
            )
        )
    else:
        inputs = "TODO"
    return inputs
