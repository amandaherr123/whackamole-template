import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        x =0
        y =0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a, b = event.pos
                    row = a // 32
                    col = b // 32

                    if x // 32 == row and y // 32 == col:
                        x = random.randrange(0, 20)*32
                        y = random.randrange(0, 16)*32

            #resets screen
            screen.fill("light green")

            #vertical lines
            for i in range(1,20):
                pygame.draw.line(screen, (0,0,0), (i *32, 0), (i*32, 512))
            #horizontal lines
            for i in range(1,16):
                pygame.draw.line(screen, (0,0,0), (0,i*32), (640, i*32))
            #mole position
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
