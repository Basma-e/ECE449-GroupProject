\"\"\"
PERSON B – Game Logic, Math Utilities, and actions() Integration
\"\"\"

import math

class GameLogic:
    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    @staticmethod
    def angle_difference(ship_heading_deg, target_angle_rad):
        ship_heading_rad = math.radians(ship_heading_deg)
        diff = target_angle_rad - ship_heading_rad
        return (diff + math.pi) % (2*math.pi) - math.pi

    def find_nearest_asteroid(self, ship_state, game_state):
        ship_pos = ship_state["position"]
        nearest = None
        best_dist = float("inf")

        for asteroid in game_state["asteroids"]:
            dist = self.distance(ship_pos, asteroid["position"])
            if dist < best_dist:
                best_dist = dist
                nearest = asteroid

        return nearest, best_dist
