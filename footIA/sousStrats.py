from soccersimulator import Vector2D, SoccerState, SoccerAction, Ball
from soccersimulator import Strategy
from soccersimulator.settings import *
from .tools import ToolBox, Comportement, ProxyObj

class Comportements(Comportement):

    RUN_COEF = maxPlayerAcceleration
    GO_COEF = maxPlayerAcceleration/3.
    COEF_DRIBLE= 0.4
    SHOOT_COEF = maxPlayerShoot/3.
    THROW_COEF = maxPlayerShoot

    def __init__(self,state):
        super(Comportements,self).__init__(state)
    
    def run(self,p):
        return SoccerAction(acceleration=(p-self.playerPos))
    
    def go(self,p):
        return SoccerAction(acceleration=(p-self.playerPos).normalize()*self.GO_COEF)
    
    def shoot(self, acc=0.64):
        if self.canShoot:
            return SoccerAction(shoot=(self.vecTheirGoal -self.ballPos).normalize()*acc)
        return SoccerAction()

    def degage(self):
        if self.canShoot:
            return SoccerAction(shoot=(self.vecTheirGoal -self.ballPos)*self.THROW_COEF)
        return SoccerAction()

    def drible (self):
        if self.canShoot:
            return SoccerAction(shoot=(self.vecTheirGoal -self.ballPos).normalize()*self.COEF_DRIBLE)
        return SoccerAction()

    def returnToGoal(self):
        return SoccerAction(self.vecMyGoal - self.playerPos) 

    def runBallPredicted(self, n=0):
        pos_ball = self.ballPos
        speed_ball = self.ballSpeed
        ball_predict = Ball(pos_ball, speed_ball)
        
        while(n > 0):
            ball_predict.next(Vector2D(0,0))
            pos_ball = ball_predict.position
            n = n - 1
    
        vec_ball = pos_ball - self.playerPos
        
        return SoccerAction(acceleration=vec_ball)

    
class ConditionGoal(ProxyObj):
    def __init__(self,state):
        super(ConditionGoal,self).__init__(state)

    def inGoalZone(self):
        return (self.myGoalBall_distance<40)

    def inGoal(self):
        coordx= self.playerPos.x
        coordy= self.playerPos.y
        target = 0 if self.id_team == 1 else 1

        return ((((target == 0)and (coordx<=10))|
                ((target == 1) and(coordx>140))) 
                and (coordy<=50 and coordy>=40))


class ConditionDribleur(ProxyObj):
    COEF_DISTMIN=45
    COEF_BALL = 0.1
    def __init__(self,state):
        super(ConditionDribleur,self).__init__(state)

    def close_opp(self):
        opp = self.get_opponent
        for players in opp:
            if (self.playerPos.distance(players)<30):
                return True
        return False
    def close_ball(self):
        return self.playerPos.distance(self.ballPos)<self.COEF_BALL*self.width

    def close_goal(self):
        return self.playerPos.distance(self.vecTheirGoal)<self.COEF_DISTMIN

class ConditionAttaque(ProxyObj):
    COEF_SHOOT = 0.3
    def __init__(self,state):
        super(ConditionAttaque,self).__init__(state)
    def close_goal(self):
        return self.playerPos.distance(self.vecTheirGoal)<self.COEF_SHOOT*self.width


def fonceur(I):
    if not I.canShoot:
        return I.run(I.ballPos)
    else:
        if I.close_goal():
            return I.shoot(6)
        return I.shoot(0.64)


def dribleur(I):

    if  I.close_opp():
        if I.canShoot:
            return I.shoot(2)
        else: 
            return I.runBallPredicted(10)
    else:
        if I.canShoot:
            if I.close_goal():
                return I.shoot(7)
            else:
                return I.drible() 

        else:
            return I.runBallPredicted(10)


def goal(I):
    if I.inGoalZone():
        if I.canShoot:
            return I.degage()
        else:
            return I.run(I.ballPos)
    else:
        if not I.inGoal():
            return I.returnToGoal()
        else:
            return None