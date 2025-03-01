from .add_input import add_input
from .add_soft_method import add_soft_method
from .utils import parse_code_string


def write_analytic_instance(dt, schema_name,
                            lib, code_string,
                            input_data, test_results):
    schema = getattr(dt, schema_name)
    parts = parse_code_string(code_string)
    soft_method = add_soft_method(dt, lib, parts["fun"])
    soft_method.is_implemented_by = code_string
    input = add_input(dt, input_data)
    output = dt.data_item(label=str(schema_name) + " results",
                          source_table=test_results)
    instance = schema(
        label=schema_name,
        executes=soft_method,
        has_input=input,
        has_output=output
    )
    return instance
