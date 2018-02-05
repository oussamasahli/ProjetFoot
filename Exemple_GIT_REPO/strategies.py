from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import SoccerTeam, Player
from soccersimulator import Strategy
from soccersimulator.settings import *
from tools import ToolBox

class RandomStrat(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-0.5,0.5))



class FonceurplayerNV0(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Fonceur")
        
    def compute_strategy(self,state,id_team,id_player):
        target = 0 if id_team == 2 else 1
        return SoccerAction(state.ball.position - state.player_state(id_team, id_player).position, Vector2D(target * GAME_WIDTH, GAME_HEIGHT/2)- state.ball.position)
        
       
              
class FonceurplayerNV1(Strategy):

	# Version amelioré du joueur fonceur." 
	# S'il peut tirer il le fait, sinon il se rapproche de la balle

    def __init__(self, acceleration):
        Strategy.__init__(self,"JFnv1")
        self.acceleration = acceleration
        
    def compute_strategy(self,state,id_team,id_player):
        
        tools = ToolBox(state,id_team,id_player)   
        
        if tools.PeutTirer(): 
            return SoccerAction(shoot = tools.VecPosGoal(maxBallAcceleration*self.acceleration))
 		    #Quand il peut on retourne le soccer action prenant"
 		    #le vecteur de sa postion courante au but"
        else:
            return SoccerAction(tools.VecPosBall(30, maxPlayerAcceleration))
            #vecteur joueur -> ballon predit"
            
        
class FonceurplayerNV1optimal(FonceurplayerNV1):
	
	def __init__(self):
		super().__init__(0.65)
