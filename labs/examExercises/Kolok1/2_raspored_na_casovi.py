from constraint import *


def masinsko_ucenje(*predavanja):
    vezbi = ml[-1]
    vreme_pred = []
    vreme_vezbi = str(vezbi[-2:])
    for cas in predavanja[:-1]:
        vreme_pred.append(str(cas[-2:]))
    return vreme_vezbi not in vreme_pred


def diff_hours(*predavanja):
    for i in range(len(predavanja)):
        temp = str(predavanja[i]).split("_")
        day_i = temp[0]
        hours_i = temp[1]
        for j in range(i + 1, len(predavanja)):
            temp = str(predavanja[j]).split("_")
            day_j = temp[0]
            hours_j = temp[1]
            if day_i == day_j and abs(int(hours_j) - int(hours_i)) < 2:
                return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    variables = []

    # ---Tuka dodadete gi promenlivite--------------------
    # ai
    for cas in range(int(casovi_AI)):
        problem.addVariable("AI_cas_" + str(cas + 1), AI_predavanja_domain)
        variables.append("AI_cas_" + str(cas + 1))

    # ml
    ml = []
    for cas in range(int(casovi_ML)):
        problem.addVariable("ML_cas_" + str(cas + 1), ML_predavanja_domain)
        ml.append("ML_cas_" + str(cas + 1))
        variables.append("ML_cas_" + str(cas + 1))



    # R
    for cas in range(int(casovi_R)):
        problem.addVariable("R_cas_" + str(cas + 1), R_predavanja_domain)
        variables.append("R_cas_" + str(cas + 1))

    # BI
    for cas in range(int(casovi_BI)):
        problem.addVariable("BI_cas_" + str(cas + 1), BI_predavanja_domain)
        variables.append("BI_cas_" + str(cas + 1))


    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    variables.append("AI_vezbi")
    variables.append("ML_vezbi")
    variables.append("BI_vezbi")
    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint())
    ml.append("ML_vezbi")
    problem.addConstraint(masinsko_ucenje, (tuple(ml)))
    problem.addConstraint(diff_hours, tuple(variables))

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)