import pygame

def main(screen, clock):
    print(screen)
    print(clock)
    run = True
    bike = pygame.image.load("res/bike.png").convert()
    bike.set_colorkey((255, 255, 255))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                run = False
        screen.fill((0, 255, 0))
        screen.blit(bike, (0, 0))
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    sc = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Fietsen")
    cl = pygame.time.Clock()
    main(sc, cl)