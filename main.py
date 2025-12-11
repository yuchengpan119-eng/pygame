
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning, message='Your system is avx2 capable but pygame was not built with support for it')
warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")

import pygame,constants,sys,player
from logger import log_state
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
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
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    player_object.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    dt = clock.tick(60)