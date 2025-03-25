from .add_input import add_input
from .add_software_method import add_software_method


def write_analytic_instance(dt, schema_name,
                            code_list, input_data):
    schema = getattr(dt, schema_name)
    software_method = add_software_method(dt, code_list)
    inputs = add_input(dt, input_data)
    instance = schema(
        label=schema_name,
        executes=software_method,
        has_input=inputs
    )
    return instance
