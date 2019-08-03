
import pygame 	
pygame.init()	
screen = pygame.display.set_mode((400, 400))
done = False	
x = 0
y = 0
width = 20
height = 20
speed = 23

while not done:

    pygame.time.delay(20) 
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (255, 255, 0), ( x, y, width, height))
    
    key = pygame.key.get_pressed() 

    if key[pygame.K_LEFT]:
        if x - speed >=  0 :    
            x -= speed
        else :
            x = 0
    if key[pygame.K_RIGHT]:
        if x + speed <=  400 - width :    
            x += speed
        else :
            x = 400 - width
    if key[pygame.K_UP]:
        if y - speed >=  0 :    
            y -= speed
        else :
            y = 0
    if key[pygame.K_DOWN]:
        if y + speed <= 400 - height :    
            y += speed
        else :
            y = 400 - height
    pygame.display.flip()
