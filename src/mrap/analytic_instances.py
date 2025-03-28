from dtreg.load_datatype import load_datatype
from .add_output import add_evaluation_output
from .add_output import add_generic_output
from .add_target import add_target
from .write_analytic_instance import write_analytic_instance


def group_comparison(code_list, input_data, test_results):
    """
    Create a group_comparison instance

    :param code_list: a list of strings for library and code line, "N/A" is not given
    :param input_data: pd.DataFrame, a dictionary, or a list with URL, n rows, and n columns
    :param test_results: a pd.DataFrame or a list of data frames
    :return: a group_comparison instance
    """
    dt = load_datatype("https://doi.org/21.T11969/b9335ce2c99ed87735a6")
    group_comparison_inst = write_analytic_instance(dt, "group_comparison",
                                                    code_list, input_data)
    group_comparison_inst.targets = add_target(dt, input_data)
    group_comparison_inst.has_output = add_generic_output(dt, "group_comparison", test_results)
    return group_comparison_inst


def algorithm_evaluation(code_list, input_data, dictionary_results):
    """
    Create an algorithm_evaluation instance

    :param code_list: a list of strings for library and code line, "N/A" is not given
    :param input_data: pd.DataFrame, a dictionary, or a list with URL, n rows, and n columns
    :param dictionary_results: a dictionary of metrics and values
    :return: an algorithm_evaluation instance
    """
    dt = load_datatype("https://doi.org/21.T11969/5e782e67e70d0b2a022a")
    algorithm_evaluation_inst = write_analytic_instance(dt, "algorithm_evaluation",
                                                        code_list, input_data)
    algorithm_evaluation_inst.has_output = add_evaluation_output(dt, dictionary_results)
    return algorithm_evaluation_inst
