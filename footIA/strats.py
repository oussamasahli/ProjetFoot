from soccersimulator  import Strategy, SoccerAction, Vector2D
from .tools import ToolBox, Comportement
from .sousStrats import Comportements,ConditionAttaque,ConditionGoal,fonceur, goal, ConditionDribleur,dribleur


class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return get_random_SoccerAction()

class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Fonceur")
    def compute_strategy(self,state,id_team,id_player):
        I = ConditionAttaque(Comportements(ToolBox(state,id_team,id_player)))
        return fonceur(I)

class GoalStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Goal")
    def compute_strategy(self,state,id_team,id_player):
        I = ConditionGoal(Comportements(ToolBox(state,id_team,id_player)))
        return goal(I)

class DribleStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Dribleur")
    def compute_strategy(self,state,id_team,id_player):
        I = ConditionDribleur(Comportements(ToolBox(state,id_team,id_player)))
        return dribleur(I)

class FonceurTestStrategy(Strategy):
    def __init__(self, strength=None):
        Strategy.__init__(self,"Fonceur")
        self.strength = strength
    def compute_strategy(self,state,id_team,id_player):
        C = Comportements(ToolBox(state,id_team,id_player))
        if self.strength:
            C.SHOOT_COEF = self.strength
        I = ConditionAttaque(C)
        return fonceur(I)
