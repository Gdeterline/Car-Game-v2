from CollisionManager import CollisionManager
from car import Car

class DRLEnvironment():
    
    def __init__(self, xinit, yinit, CAR_IMAGE, racetrack):
        # Starting line
        self.xinit = xinit
        self.yinit = yinit
        
        self.reward = 0
        
        self.racetrack = racetrack
        self.car = Car(self.xinit, self.xinit, CAR_IMAGE)
        self.collision_manager = CollisionManager(self.car, self.racetrack)
        
    def reset(self):
        self.car.set_state(self.xinit, self.yinit, velocity=0, angle=0)
        return self.car.get_state()
        
    def step(self, action):
        self.car.apply_action(action)
        collision = self.collision_manager.check_boundary_collision(self.car, self.racetrack)
        
        if collision:
            self.reward -= 100
        else:
            self.reward += 1
        
        next_state = self.car.get_state()
        
        return next_state, self.reward, collision