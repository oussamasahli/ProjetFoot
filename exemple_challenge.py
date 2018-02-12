from soccersimulator import ChallengeFonceurButeur, SoccerTeam,show_simu
from strategies import FonceurplayerNV1optimal

team = SoccerTeam("RandomEquipe")
team.add("RandomJoueur",FonceurplayerNV1optimal())

challenge = ChallengeFonceurButeur(team,max_but=20)
show_simu(challenge)
print("temps moyen : ",challenge.stats_score, "\nliste des temps",challenge.resultats)
