import pygame
import time
import serial

def main(screen, clock):
    run = True
    
    bike = pygame.image.load("res/bike.png").convert()
    bike = pygame.transform.scale(bike, (75, 150))
    bike.set_colorkey((255, 255, 255))
    
    crash = pygame.image.load("res/bike fall.png").convert()
    print(crash.get_size())
    crash = pygame.transform.scale(crash, (150, 150))
    crash.set_colorkey((255, 255, 255))
    
    background = pygame.image.load("res/background.png").convert()
    background = pygame.transform.scale(background, (int((screen.get_height() / background.get_height() - 1) * background.get_width()), screen.get_height()))
    
    ser = serial.Serial(2)
    
    pos = 0 
    posb = 100
    vel = 0
    time1 = 0
    fall = False
    go = True
    while run:
        ############################################################################################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                vel += 0.5
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                fall = True
                go = False
                vel = 0
                time1 = time.time()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSLASH and time.time() - time1 >= 5:
                fall = False
                go = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                pos = 1000
        ######################################################################################################################
        if ser.inWaiting()>0:
            data = ser.read()
            data = data.decode("utf-8") 
            if data == "t" and go:
                vel += 0.20
            elif data == "f":
                fall = True
                go = False
                vel = 0
                time1 = time.time()
            elif data == "g" and time.time() - time1 >= 5:
                fall = False
                go = True
        ########################################################################################################################
        if go:
            pos += vel
            vel *= 0.995
            
        if pos > background.get_width()-screen.get_width() :
            go = False
            if posb < screen.get_width() -20:
                posb += 0.5
        
        screen.blit(background, (0, 0), pygame.Rect(pos, 0, screen.get_width(), screen.get_height()))
        if not fall:
            screen.blit(bike, (100, 150))
        else:
            screen.blit(crash, (100,150))
        pygame.display.update()
        

if __name__ == "__main__":
    pygame.init()
    sc = pygame.display.set_mode((0,400), pygame.FULLSCREEN)
    pygame.display.set_caption("Fietsen")
    cl = pygame.time.Clock()
    main(sc, cl)