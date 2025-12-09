
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning, message='Your system is avx2 capable but pygame was not built with support for it')
warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")

import pygame,constants

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")


if __name__ == "__main__":
    main()
    print("Screen width:",constants.SCREEN_WIDTH)
    print("Screen height:",constants.SCREEN_HEIGHT)