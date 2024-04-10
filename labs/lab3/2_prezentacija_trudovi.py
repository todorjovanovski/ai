from constraint import *


def max_3_trudovi(*termini):
    li = list(termini)
    return li.count("T1") <= 4 and li.count("T2") <= 4 and li.count("T3") <= 4


def max_4_trudovi(*termini):
    li = list(termini)
    return li.count("T1") <= 4 and li.count("T2") <= 4 and li.count("T3") <= 4 and li.count("T4") <= 4


def check_termin(*termini):
    for ind in range(1, len(termini)):
        if termini[ind] != termini[ind - 1]:
            return False
    else:
        return True


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    ai = []
    ml = []
    nlp = []
    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = []
    for key in papers:
        name = key + " (" + papers[key] + ")"
        variables.append(name)
        if papers[key] == "AI":
            ai.append(name)
        elif papers[key] == "ML":
            ml.append(name)
        elif papers[key] == "NLP":
            nlp.append(name)

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    tup = tuple(variables)
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    if num == 3:
        problem.addConstraint(max_3_trudovi, variables)
    else:
        problem.addConstraint(max_4_trudovi, variables)

    if len(ai) <= 4:
        problem.addConstraint(check_termin, ai)
    if len(ml) <= 4:
        problem.addConstraint(check_termin, ml)
    if len(nlp) <= 4:
        problem.addConstraint(check_termin, nlp)

    # Tuka dodadete go kodot za pechatenje
    # result = problem.getSolution()
    # print(result)
    # [print(solution) for solution in problem.getSolution()]

    result = problem.getSolution()
    for key in sorted(result.keys()):
        print(key + ": " + result[key])
