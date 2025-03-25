from .add_input import add_input
from .add_software_method import add_software_method
from .utils import parse_code_string


def write_analytic_instance(dt, schema_name,
                            lib, code_string,
                            input_data):
    schema = getattr(dt, schema_name)
    parts = parse_code_string(code_string)
    software_method = add_software_method(dt, lib, parts["fun"])
    software_method.is_implemented_by = code_string
    inputs = add_input(dt, input_data)
    instance = schema(
        label=schema_name,
        executes=software_method,
        has_input=inputs
    )
    return instance
