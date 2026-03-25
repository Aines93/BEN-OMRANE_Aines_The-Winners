import numpy as np
import random
from .steering import Steering

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

class Agent7(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "BEN-OMRANE Aines" 
        self.steering=Steering()

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []
        self.steering.reset()

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        points = obs.get("paths_start",[]) # On récupère la liste des points
        
        if len(points) <= 2: # Si la longueur de la liste est inferieur à 2, on accèlère à fond (ligne d'arrivée proche)
            return {
                "acceleration": 1.0,
                "steer": 0.0,
                "brake": False,
                "drift": False,
                "nitro": True,
                "rescue":False,
                "fire": False,
            }
        
        target = points[2] # On récupère le x-ème point de la liste defini par la variable de classe
        gx = target[0] # On récupère x, le décalage latéral
        gz = target[2] # On récupère z, la profondeur

        steering =self.steering.manage_pure_pursuit(gx,gz,2)
        action = {
            "acceleration": 1,
            "steer": steering,
            "brake": False, # bool(random.getrandbits(1)),
            "drift": False,
            "nitro": bool(random.getrandbits(1)),
            "rescue":bool(random.getrandbits(1)),
            "fire": bool(random.getrandbits(1)),
        }
        return action
