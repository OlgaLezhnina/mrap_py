from .add_input import add_input
from .add_software_method import add_software_method
from .add_output import add_output
from .utils import parse_code_string


def write_analytic_instance(dt, schema_name,
                            lib, code_string,
                            input_data, test_results):
    schema = getattr(dt, schema_name)
    parts = parse_code_string(code_string)
    software_method = add_software_method(dt, lib, parts["fun"])
    software_method.is_implemented_by = code_string
    inputs = add_input(dt, input_data)
    output = add_output(dt, schema_name, test_results)
    instance = schema(
        label=schema_name,
        executes=software_method,
        has_input=inputs,
        has_output=output
    )
    return instance
