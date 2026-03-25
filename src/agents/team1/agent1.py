import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent


class Agent1(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "BEN-OMRANE Aines" # replace with your chosen name
        self.time=20
        self.b=True

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []
        self.time=20
        self.b=True

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        #faire le demi tour
        if(self.b):
            acceleration = 0.1 
            steering =1 # pour pouvoir faire le tour (ou -1)
            action = {
                "acceleration": acceleration,
                "steer": steering,
                "brake": False, # bool(random.getrandbits(1)),
                "drift": bool(random.getrandbits(1)),
                "nitro": bool(random.getrandbits(1)),
                "rescue":bool(random.getrandbits(1)),
                "fire": bool(random.getrandbits(1)),
            }
            self.b=False
            return action
        #rouler en marche arriere
        points = obs.get("paths_start",[]) # On récupère la liste des points
        target = points[2] # On récupère le x-ème point de la liste defini par la variable de classe
        
        gx = target[0] # On récupère x, le décalage latéral
        gz = target[2] # On récupère z, la profondeur

        steering =self.steering.manage_pure_pursuit(gx,gz,2)
        action = {
            "acceleration": 0.0,
            "steer": steering,
            "brake": True,
            "drift": False,
            "nitro": False,
            "rescue":False,
            "fire":False,
        }
        
        return action