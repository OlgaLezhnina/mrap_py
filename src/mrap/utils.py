from dtreg.to_jsonld import to_jsonld


def parse_code_string(code_string):
    result = {"fun": code_string.split("(")[0]}
    return result


def assign_result(instance, jsonld):
    if jsonld:
        instance = to_jsonld(instance)
    return instance
