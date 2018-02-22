from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy
from footIA.strats  import GoalStrategy, DribleStrategy, FonceurStrategy


## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
fonceur = SoccerTeam(name="fonceurStratTeam")
pyteam.add("Goal",GoalStrategy())
fonceur.add("Dribleur",DribleStrategy())

#Creation d'une partie
simu = Simulation(pyteam,fonceur)
#Jouer et afficher la partie
show_simu(simu)
