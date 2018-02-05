from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy
from strategies  import RandomStrat


## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
random = SoccerTeam(name="randomTeam")
pyteam.add("PyPlayer",Strategy()) #Strategie qui ne fait rien
random.add("RandomStrat",RandomStrat())   #Strategie aleatoire
random.add("RandomStrat",RandomStrat())
random.add("RandomStrat",RandomStrat())

#Creation d'une partie
simu = Simulation(pyteam,random)
#Jouer et afficher la partie
show_simu(simu)
