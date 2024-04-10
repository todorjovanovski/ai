from constraint import *


def meeting(simona, marija, petar, time):
    return (simona == 1 and time in [13, 14, 16, 19]) and \
        ((marija == 1 and time in [14, 15, 18] and petar == 0)
         or (petar == 1 and time in [12, 13, 16, 17, 18, 19] and marija == 0))


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----

    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [13, 14, 16, 19, 18, 12, 15, 17])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(meeting, ("Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"))

    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]
