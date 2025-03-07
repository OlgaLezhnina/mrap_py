from dtreg.load_datatype import load_datatype
from .add_target import add_target
from .write_analytic_instance import write_analytic_instance


def group_comparison(lib, code_string, input_data, test_results):
    dt = load_datatype("https://doi.org/21.T11969/b9335ce2c99ed87735a6")
    group_comp_inst = write_analytic_instance(dt, "group_comparison",
                                              lib, code_string, input_data, test_results)
    group_comp_inst.targets = add_target(dt, input_data)
    return group_comp_inst
