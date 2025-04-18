from dtreg.load_datatype import load_datatype
from .add_level import add_level
from .add_output import add_evaluation_output
from .add_output import add_generic_output
from .add_target import add_comparison_target
from .add_target import add_generic_target
from .write_analytic_instance import write_analytic_instance


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


def multilevel_analysis(code_list, input_data, test_results):
    """
    Create a group_comparison instance

    :param code_list: a list of strings for library and code line, "N/A" is not given
    :param input_data: pd.DataFrame, a dictionary, or a list with URL, n rows, and n columns
    :param test_results: a pd.DataFrame or a list of data frames
    :return: a group_comparison instance
    """
    dt = load_datatype("https://doi.org/21.T11969/c6b413ba96ba477b5dca")
    mult_analysis_inst = write_analytic_instance(dt, "multilevel_analysis",
                                                 code_list, input_data)
    mult_analysis_inst.level = add_level(dt, code_list)
    mult_analysis_inst.targets = add_generic_target(dt, code_list, input_data)
    mult_analysis_inst.has_output = add_generic_output(dt, "multilevel_analysis",
                                                       test_results)
    return mult_analysis_inst


def correlation_analysis(code_list, input_data, test_results):
    """
    Create a correlation_analysis instance

    :param code_list: a list of strings for library and code line, "N/A" is not given
    :param input_data: pd.DataFrame, a dictionary, or a list with URL, n rows, and n columns
    :param dictionary_results: a dictionary of metrics and values
    :return: a correlation_analysis instance
    """
    dt = load_datatype("https://doi.org/21.T11969/3f64a93eef69d721518f")
    corr_analysis_inst = write_analytic_instance(dt, "correlation_analysis",
                                                 code_list, input_data)
    corr_analysis_inst.has_output = add_generic_output(dt, "correlation_analysis", test_results)
    return corr_analysis_inst


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
    group_comparison_inst.targets = add_comparison_target(dt, code_list, input_data)
    group_comparison_inst.has_output = add_generic_output(dt, "group_comparison", test_results)
    return group_comparison_inst


def class_discovery(code_list, input_data, test_results):
    """
    Create a class_discovery instance

    :param code_list: a list of strings for library and code line, "N/A" is not given
    :param input_data: pd.DataFrame, a dictionary, or a list with URL, n rows, and n columns
    :param dictionary_results: a dictionary of metrics and values
    :return: a class_discovery instance
    """
    dt = load_datatype("https://doi.org/21.T11969/c6e19df3b52ab8d855a9")
    class_discovery_inst = write_analytic_instance(dt, "class_discovery",
                                                   code_list, input_data)
    class_discovery_inst.has_output = add_generic_output(dt, "class_discovery", test_results)
    return class_discovery_inst


def factor_analysis(code_list, input_data, test_results):
    """
    Create a factor_analysis instance

    :param code_list: a list of strings for library and code line, "N/A" is not given
    :param input_data: pd.DataFrame, a dictionary, or a list with URL, n rows, and n columns
    :param dictionary_results: a dictionary of metrics and values
    :return: a factor_analysis instance
    """
    dt = load_datatype("https://doi.org/21.T11969/437807f8d1a81b5138a3")
    factor_analysis_inst = write_analytic_instance(dt, "factor_analysis",
                                                   code_list, input_data)
    factor_analysis_inst.has_output = add_generic_output(dt, "factor_analysis", test_results)
    return factor_analysis_inst
