# mrap
<!-- badges: start -->
<!-- badges: end -->

**100% AI-free: we did not use any AI technologies in developing this package.**

The goal of mrap is to provide wrapper functions to reduce the user's effort 
in writing machine-readable data with the [dtreg library](https://pypi.org/project/dtreg/).
The growing set of wrappers covers functions from scipy and other widely used libraries.
The mrap.analytic_instances module contains wrappers for analytical schemata used by [TIB Knowledge Loom](https://knowledgeloom.tib.eu/).

To write the results of your data analysis as JSON-LD:
* Select a wrapper from mrap, check the types of arguments it requires, and create an instance.
* Modify the instance by setting or correcting its fields manually.
* Write the finalised instance as a machine-readable JSON-LD file.        

## Installation

```sh
## activate a virtual environment (optional)
python3 -m venv .venv
source .venv/bin/activate
## install from PyPi:
pip install mrap
```

## Example
Let us assume you intend to report the classification performance of your_fancy_algorithm. 
From the [help page](https://reborn.orkg.org/pages/help) you know that the wrapper of choice is 
``algorithm_evaluation()``. The required arguments are:

* ``code_list``: a string "N/A" if not given or a list of two strings -
the library and the line of code used for implementing the analysis.
* ``input_data``: a pd.DataFrame, a dictionary of pd.Series with names, or a string which is
either the data URL or the file name. 
* ``dictionary_results``: metrics as keys with values.

The wrapper writes information about the data, your results, your Python version, 
the library version, etc. After adding the information about the algorithm and the task manually, 
and correcting any fields you wish, you can convert the instance 
into a machine-readable JSON-LD string. 
  
```python
from mrap.analytic_instances import algorithm_evaluation
from dtreg.to_jsonld import to_jsonld
## run your analysis and write the results as a dictionary
results_dict = {"F1": 0.46, "recall": 0.51}
## create your instance with the wrapper
my_instance = algorithm_evaluation(["the_library", "the_line_of_code"], 
                                   "my_URL", results_dict)
## modify the instance by writing fields manually
my_instance.evaluates = "my_fancy_algorithm"
my_instance.evaluates_for = "Classification"
## write the instance in JSON-LD format as a string
my_json = to_jsonld(my_instance)
## the result can be saved as a JSON file
with open('my_file.json', 'w') as f:
    f.write(my_json)

```
It is also possible to write the results of a few algorithms evaluated on the same data
for the same task and include these into the data_analysis datatype:

```python
from mrap.list_algorithm_evaluations import list_algorithm_evaluations
from dtreg.load_datatype import load_datatype
from dtreg.to_jsonld import to_jsonld
## run your analysis and write a nested dictionary
my_results = {"ABC": {"F1": 0.46, "recall": 0.64},
             "KLM": {"F1": 0.55, "recall": 0.38},
             "XYZ": {"F1": 0.87, "recall": 0.78}}
## create the list of instances
all_results = list_algorithm_evaluations("N/A", "my URL", "Classification", my_results)
## modify any instance manually
all_results[0].label = "ABC evaluation on XXX data"
## load the data_analysis datatype and create the final instance
dt_final = load_datatype("https://doi.org/21.T11969/feeb33ad3e4440682a4d")
final_instance = dt_final.data_analysis(has_part=all_results)
## make any changes to the final instance
final_instance.is_implemented_by = "code_URL"
## write the final instance in JSON-LD format as a string
final_json = to_jsonld(final_instance)
## the result can be saved as a JSON file
with open('final_file.json', 'w') as f:
    f.write(final_json)

```

For more information, please see the [help page](https://knowledgeloom.tib.eu/pages/help).