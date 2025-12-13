from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
import pygame,random
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self,dt):
        self.position = self.position+self.velocity*dt
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            first_rotate = self.velocity.rotate(random_angle)
            second_rotate = self.velocity.rotate(-random_angle)
            first_asteroid = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
            second_asteroid  = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
            first_asteroid.velocity=first_rotate
            second_asteroid.velocity =second_rotate