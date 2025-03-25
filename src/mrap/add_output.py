def add_generic_output(dt, schema_name, test_results):
    output = dt.data_item(label=str(schema_name) + " results",
                          source_table=test_results)
    return output


def add_evaluation_output(dt, dictionary_results):
    pass
