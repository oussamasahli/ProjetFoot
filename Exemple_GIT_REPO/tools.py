from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import SoccerTeam, Strategy, Player, Ball
from soccersimulator.settings import *

import math

class ToolBox(object):
    
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player

            
    def PosJoueur(self):
        return self.state.player_state(self.id_team, self.id_player).position
          
    def PosBall(self):
        return self.state.ball.position
        

    " retourne le vecteur du joueur vers le but" 
        
    def VecPosGoal(self, norm_acc = None):

        target = 0 if self.id_team == 2 else 1
        pos_goal = Vector2D((target)*GAME_WIDTH, GAME_HEIGHT/2)
        vec_goal = pos_goal - self.PosJoueur()
        
        if norm_acc != None:
            vec_goal.norm = norm_acc
            
        return vec_goal


    " retourne le vecteur du joueur a la position prevu du ballon au bout de n pas."

    def VecPosBall(self, n = 0, norm_acc = None):

        pos_ball = self.state.ball.position
        vitesse_ball = self.state.ball.vitesse
        ball_temporaire = Ball(pos_ball, vitesse_ball)
        
        while(n > 0):
            ball_temporaire.next(Vector2D(0,0))
            pos_ball = ball_temporaire.position         
            n = n - 1
    
        vec_ball = pos_ball - self.state.player_state(self.id_team, self.id_player).position
        if norm_acc != None:
            vec_ball.norm = norm_acc
        return vec_ball
    	

    " retourne le vecteur ballon vers cage"
        
    def VecGoal_to_Ball(self, norm_acc = None):
        #target definie quelle est la cage correspondante

        target = 0 if self.id_team == 1 else 1
        pos_goal = Vector2D((target)*GAME_WIDTH, GAME_HEIGHT/2)
        vec_goalball = pos_goal - self.PosBall()

        if norm_acc != None:
            vec_goalball.norm = norm_acc
        return vec_goalball        
        
    " distance courante du milieu des cages au ballon "
    
    def distance_cages_ballon(self, acceleration):
    	return self.PosBall().distance(v = self.VecGoal_to_Ball(acceleration))



    def PeutTirer(self):

        pos_player = self.PosJoueur()
        pos_ball = self.PosBall()
   
        return pos_ball.distance(pos_player) < PLAYER_RADIUS + BALL_RADIUS

    
    def Retour_aux_cages(self, norm_acc = None):
        target = 0 if self.id_team == 1 else 2
        pos_goal = Vector2D((target)*GAME_WIDTH, GAME_HEIGHT/2)
        return pos_goal - self.PosJoueur()
    
    
    def estAuxCages(self, norm_acc = None):
    
    	coordx= self.PosJoueur().x
    	coordy= self.PosJoueur().y
    
    	target = 0 if self.id_team == 1 else 2
    	if((((target == 0)and (coordx<=5))|
    	((target == 1) and(coordx>145))) 
    	and (coordy<=50 and coordy>=40)):
    	
    		return True
    	else:
    		return False        
        
        
    "  retourne un vecteur d'acceleration."
    "  Si norm_acc n'est pas donnée la norme du vecteur est definie comme maxBallAcceleration."

    def VecTire(self,norm_acc = maxBallAcceleration):
        
        return  Vector2D(angle = (1 - self.id_team) * math.pi, norm = norm_acc)
    
