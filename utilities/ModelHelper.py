from pulp import *
from utilities.SizeHelper import *


def add_variable_to_data(d, name):

    if (name in d):
        return True

    d[name] = LpVariable(name, lowBound=0, cat='Integer')
    return False


def reg(d, name, ia=[-1, -1], ja=[-1, -1], ka=[-1, -1], la=[-1, -1], ma=[-1, -1]):

    if (ia[0] == -1):
        has_already_added = add_variable_to_data(d, name)
        if has_already_added:
            return
    elif (ja[0] == -1):
        for i in full_range(ia[0], ia[1]):
            varname = name.replace('$1', ',' + str(i))
            has_already_added = add_variable_to_data(d, varname)
            if has_already_added:
                continue
    elif (ka[0] == -1):
        for i in full_range(ia[0], ia[1]):
            for j in full_range(ja[0], ja[1]):
                varname = name.replace(
                    '$1', ',' + str(i)).replace('$2', ',' + str(j))
                has_already_added = add_variable_to_data(d, varname)
                if has_already_added:
                    continue
    elif (la[0] == -1):
        for i in range(ia[0], ia[1] + 1):
            for j in range(ja[0], ja[1] + 1):
                for k in range(ka[0], ka[1] + 1):
                    varname = name.replace(
                        '$1', ',' + str(i)).replace('$2', ',' + str(j)).replace('$3', ',' + str(k))
                    has_already_added = add_variable_to_data(d, varname)
                    if has_already_added:
                        continue
    elif (ma[0] == -1):
        for i in range(ia[0], ia[1] + 1):
            for j in range(ja[0], ja[1] + 1):
                for k in range(ka[0], ka[1] + 1):
                    for l in range(la[0], la[1] + 1):
                        varname = name.replace('$1', ',' + str(i)).replace('$2', ',' + str(
                            j)).replace('$3', ',' + str(k)).replace('$4', ',' + str(l))
                        has_already_added = add_variable_to_data(d, varname)
                        if has_already_added:
                            continue
    else:
        for i in range(ia[0], ia[1] + 1):
            for j in range(ja[0], ja[1] + 1):
                for k in range(ka[0], ka[1] + 1):
                    for l in range(la[0], la[1] + 1):
                        for m in range(ma[0], ma[1] + 1):
                            varname = name.replace('$1', ',' + str(i)).replace('$2', ',' + str(j)).replace(
                                '$3', ',' + str(k)).replace('$4', ',' + str(l)).replace('$5', ',' + str(m))
                            has_already_added = add_variable_to_data(
                                d, varname)
                            if has_already_added:
                                continue
