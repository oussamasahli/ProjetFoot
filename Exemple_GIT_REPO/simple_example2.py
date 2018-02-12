from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy
from strategies  import FonceurplayerNV0, FonceurplayerNV1, FonceurplayerNV1optimal, GoalplayerNV0, DefenseplayerNV0


## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
fonceur = SoccerTeam(name="fonceurStratTeam")
fonceur.add("i-Fonceur",FonceurplayerNV1optimal())

pyteam.add("Goal", GoalplayerNV0())


#Creation d'une partie
simu = Simulation(pyteam,fonceur)
#Jouer et afficher la partie
show_simu(simu)
