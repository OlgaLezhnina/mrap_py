# mrap
<!-- badges: start -->
<!-- badges: end -->

The goal of mrap is to provide wrapper functions to reduce the user's effort 
in writing machine-reusable data with the dtreg library. The growing set of wrappers covers 
functions from scipy and other widely used libraries. 
The mrap.analytic_instances module contains wrappers for analytical schemata used in 
the ORKG-reborn approach (see the [help page](https://reborn.orkg.org/pages/help)).

To write the results of your data analysis into JSON-LD:
* Select a wrapper from mrap, check the types of arguments it requires, and create an instance.
* Modify the instance by setting or correcting its fields manually.
* Write the finalised instance as a machine-readable JSON-LD file with dtreg.        

## Installation

```sh
## install from PyPi:
pip install mrap
```

## Example
Let us assume you intend to report the classification performance of your_fancy_algorithm. 
From the [help page](https://reborn.orkg.org/pages/help) you know that the wrapper of choice is 
algorithm_evaluation(). The required arguments are:    

* code_list: a string "N/A" if not given, or a list of two strings, 
the library and the line of code used for implementing the analysis.
* input_data: a pd.DataFrame, a dictionary of pd.Series with names, or a list 
containing the data URL as a string, the number of rows, and the number of columns. 
* dictionary_results: metrics as keys with values.

The wrapper writes information about the data, your results, your Python version, 
the library version, etc. After adding the information about the algorithm and the task manually, 
and correcting any fields you wish, you can convert the instance 
into machine-readable JSON-LD string. 
  
```python
## import the selected wrapper from mrap
from mrap.analytic_instances import algorithm_evaluation
## import to_jsonld from dtreg to convert the result into JSON-LD
from dtreg.to_jsonld import to_jsonld
## run you analysis and write the results as a dictionary
results_dict = {"F1": 0.46, "recall": 0.51}
## create your instance with the wrapper
my_instance = algorithm_evaluation(["the_library", "the_line_of_code"], 
                                   ["my_URL", 5000, 12], results_dict)
## modify the instance by setting parameters manually
my_instance.evaluates = "my_fancy_algorithm"
my_instance.evaluates_for = "Classification"
## write the instance in JSON-LD format as a string
my_json = to_jsonld(my_instance)
## the result can be saved as a JSON file
with open('my_file.json', 'w') as f:
    f.write(my_json)

```
For more information, please see the [help page](https://reborn.orkg.org/pages/help).