from dtreg.to_jsonld import to_jsonld


def assign_result(instance, jsonld):
    if jsonld:
        instance = to_jsonld(instance)
    return instance
