from dtreg.to_jsonld import to_jsonld


def assign_result(instance, jsonld):
    if jsonld is False:
        result = instance
    else:
        result = to_jsonld(instance)
    return result
