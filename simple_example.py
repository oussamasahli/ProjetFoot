from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy
from footIA.strategies  import FonceurplayerNV1optimal, dribleurplayerNV0, RandomStrat, GoalplayerNV0


## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
fonceur = SoccerTeam(name="fonceurStratTeam")
fonceur.add("Dribleur",dribleurplayerNV0())
pyteam.add("fonceur",GoalplayerNV0())

#pyteam.add("Goal", RandomStrat())


#Creation d'une partie
simu = Simulation(pyteam,fonceur)
#Jouer et afficher la partie
show_simu(simu)
