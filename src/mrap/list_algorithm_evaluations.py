from .analytic_instances import algorithm_evaluation


def list_algorithm_evaluations(code_list, input_data, task, sum_dictionary):
    """
    Create a list of lgorithm_evaluation instances

    :param code_list: a list of strings for library and code line, "N/A" is not given
    :param input_data: pd.DataFrame, a dictionary, or a string
    :param sum_dictionary: a nested dictionary of algorithms as strings and results
    :return: a list of instances
    """
    algorithms_instances = []
    for key, value in sum_dictionary.items():
        instance = algorithm_evaluation(code_list, input_data, value)
        instance.label = key + " evaluation"
        instance.evaluates = key
        instance.evaluates_for = task
        algorithms_instances.append(instance)
    return algorithms_instances
