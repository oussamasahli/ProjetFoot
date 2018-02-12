from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy
from footIA.strategies  import FonceurplayerNV1optimal, dribleurplayerNV0, RandomStrat


## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
pyteam.add("Nul", Strategy())
fonceur = SoccerTeam(name="fonceurStratTeam")
fonceur.add("i-Fonceur",dribleurplayerNV0())

#pyteam.add("Goal", RandomStrat())


#Creation d'une partie
simu = Simulation(pyteam,fonceur)
#Jouer et afficher la partie
show_simu(simu)
