import pygame
pygame.init()

grey = (119,118,110)

width = 800
height = 600
gamedisplay = pygame.display.set_mode((width,height))

pygame.display.set_caption("Car Game")
carimage = pygame.image.load("car1.png")
clock = pygame.time.Clock()

def car(x,y):
    gamedisplay.blit(carimage,(x,y))

def game_loop():
    x = (width*0.45)
    y = (height*0.8)
    x_change = 0
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                bumped=True
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change = -5
            if event.key==pygame.K_RIGHT:
                x_change = 5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_change=0
        x+=x_change
        gamedisplay.fill(grey)
        car(x,y)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

game_loop()
pygame.quit()
quit()