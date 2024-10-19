from dtreg.load_datatype import load_datatype


def select_stat_test_diff(dtr):
    stat_test_diff = None
    if dtr == "epic":
        stat_test_diff = load_datatype("https://doi.org/21.T11969/ff5e3f857788d20dd1aa")
    elif dtr == "orkg":
        stat_test_diff = load_datatype("https://incubating.orkg.org/template/R836000")
    else:
        print("The dtr can be only epic or orkg")
    return stat_test_diff
