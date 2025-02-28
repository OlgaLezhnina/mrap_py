from .add_soft_method import add_soft_method
from .utils import assign_result
from dtreg.load_datatype import load_datatype
import pandas as pd
from scipy.stats import f_oneway
from varname import argname


def scipy_f_oneway(*samples, jsonld=False):
    anova_object = f_oneway(*samples)
    sum_object = pd.DataFrame({'F': anova_object[0], 'p': anova_object[1]}, index=[0])
    target_name = samples[0].name
    dt = load_datatype("https://doi.org/21.T11969/b9335ce2c99ed87735a6")
    input_labels = []
    inputs = []
    for i in range(len(samples)):
        input_label = argname('samples[%d]' % i)
        input_labels.append(input_label)
        an_input = dt.data_item(label=input_label,
                                has_characteristic=dt.matrix_size(
                                    number_of_rows=len(samples[i]),
                                    number_of_columns=1))
        inputs.append(an_input)

    soft_method = add_soft_method(dt, "scipy", "f_oneway")
    soft_method.is_implemented_by = "f_oneway(" + ",".join(input_labels) + ")"
    target_variable = dt.component(label=target_name)
    output = dt.data_item(label="ANOVA results",
                          source_table=sum_object)
    instance = dt.group_comparison(
        label="Anova " + target_name,
        executes=soft_method,
        has_input=inputs,
        targets=target_variable,
        has_output=output)
    dtreg_object = assign_result(instance, jsonld)
    result = {"anova": anova_object,
              "dtreg_object": dtreg_object}
    return result
