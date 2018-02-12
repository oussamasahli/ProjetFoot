from soccersimulator import SoccerTeam
from .strategies import *
from .tools import *

def get_team(nb_players):
	myteam = SoccerTeam(name="MaTeam")
	if nb_players == 1:
		myteam.add("Joueur " ,dribleurplayerNV0())
	if nb_players == 2:
		myteam.add("Joueur 1", dribleurplayerNV0())
		myteam.add("Joueur 2", GoalplayerNV0())
	if nb_players == 4:
		myteam.add("Joueur 1",dribleurplayerNV0())
		myteam.add("Joueur 2",GoalplayerNV0())
		myteam.add("Joueur 3",DefenseplayerNV0())
		myteam.add("Joueur 4",FonceurPlayerNV1optimal())
	return myteam	

def get_team_challenge(num):
	myteam = SoccerTeam(name="MaTeamChallenge")
	if num == 1:
		myteam.add("Joueur Chal "+str(num),RandomStrategy())
	return myteam
