from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy
from strategies  import FonceurplayerNV0, FonceurplayerNV1, FonceurplayerNV1optimal


## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
fonceur = SoccerTeam(name="fonceurStratTeam")
fonceur.add("FonceurStrat2",Strategy())
fonceur.add("FonceurStrat2",FonceurplayerNV1optimal())
pyteam.add("FonceurStrat1",Strategy())

#Creation d'une partie
simu = Simulation(pyteam,fonceur)
#Jouer et afficher la partie
show_simu(simu)
