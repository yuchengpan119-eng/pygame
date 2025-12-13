
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning, message='Your system is avx2 capable but pygame was not built with support for it')
warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")

import pygame,constants,sys,player,asteroid
import asteroidfield,shot
from logger import log_state,log_event
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()


asteroidfield.AsteroidField.containers = (updatable)
asteroid.Asteroid.containers = (asteroids,updatable,drawable)
player.Player.containers = (updatable,drawable)
shot.Shot.containers = (shots,drawable,updatable)

asteroid_field = asteroidfield.AsteroidField()
player_object = player.Player(x = constants.SCREEN_WIDTH / 2,
y = constants.SCREEN_HEIGHT / 2)

clock = pygame.time.Clock()
dt = 0
if __name__ == "__main__":
    main()
    print("Screen width:",constants.SCREEN_WIDTH)
    print("Screen height:",constants.SCREEN_HEIGHT)
while True:
    log_state()
    dt = clock.tick(60)/1000
    updatable.update(dt)
    
    for asteriod in asteroids:
        if player_object.collides_with(asteriod):
            log_event("player_hit")
            print("Game Over!")
            sys.exit()
    for shot_ in shots:
        for asteriod in asteroids:
            if shot_.collides_with(asteriod):
                log_event("asteroid_shot")
                shot_.kill()
                asteriod.split()
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for draws in drawable:
        draws.draw(screen)
    pygame.display.flip()