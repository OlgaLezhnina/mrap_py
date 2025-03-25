import pandas as pd
from dtreg.load_datatype import load_datatype
from .utils import standardise_keys


def add_generic_output(dt, schema_name, test_results):
    output = dt.data_item(label=str(schema_name) + " results",
                          source_table=test_results)
    return output


def add_evaluation_output(dt, dictionary_results):
    dt = load_datatype("https://doi.org/21.T11969/5e782e67e70d0b2a022a")
    new_dictionary = standardise_keys(dictionary_results)
    df_results = pd.DataFrame([new_dictionary])
    df_named = df_results.rename(index={0: 'value'})
    output = dt.data_item(label="algorithm evaluation results",
                          source_table=df_named)
    return output
