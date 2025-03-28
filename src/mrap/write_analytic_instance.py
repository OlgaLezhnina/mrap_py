from .add_input import add_input
from .add_software_method import add_software_method


def write_analytic_instance(dt, schema_name,
                            code_list, input_data):
    """
    Write a generic instance to be used by analytic schemata instances

    :param dt: an analytical schema datatype
    :param schema_name: an analytical schema name as a string
    :param code_list: a list of strings for library and code line, "N/A" if not given
    :param input_data: pd.DataFrame, a dictionary, or a list with URL, n rows, and n columns
    :return: a generic instance to be used by analytic schemata instances
    """
    schema = getattr(dt, schema_name)
    software_method = add_software_method(dt, code_list)
    inputs = add_input(dt, input_data)
    instance = schema(
        label=schema_name,
        executes=software_method,
        has_input=inputs
    )
    return instance
