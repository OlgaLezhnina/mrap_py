def parse_code_list(code_list):
    result = {"fun": code_list[1].split("(")[0]}
    return result


def standardise_keys(old_dict):
    new_dict = {}
    f1_matches = ["f1", "f_1"]
    uppercase = ["auc", "mae", "mse", "rmse"]
    lowercase = ["accuracy", "precision", "recall"]
    for key, value in old_dict.items():
        if any(x in key.casefold() for x in f1_matches):
            new_dict["F1"] = old_dict[key]
        elif key.casefold() in uppercase:
            new_dict[key.upper()] = old_dict[key]
        elif key.casefold() in lowercase:
            new_dict[key.lower()] = old_dict[key]
        else:
            new_dict[key] = old_dict[key]
    return (new_dict)
