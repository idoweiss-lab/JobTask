import pygame
import sys
import random
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")



x = 300
y = 20
width = 10
height = 10
vel = 10
right = False
left = False
up = False
down = False
headtail = [[x, y]]
class apple:
    def __init__(self):
        self.x = 200
        self.y = 200

    def createapplex(self):
        x = random.randint(1, 45)*10
        num = 0
        while (num == 0):
            for frame in headtail:
                if frame[0] == x:
                    num = 1
            if num == 1:
                num = 0
                x = random.randint(1, 45)*10
            else:
                num = 2
        self.x = x
    def createappley(self):
        y = random.randint(1, 45)*10
        num = 0
        while (num == 0):
            for frame in headtail:
                if frame[1] == y:
                    num = 1
            if num == 1:
                num = 0
                y = random.randint(1, 45)*10
            else:
                num = 2
        self.y = y

def redrawGameWindow():
    win.fill((0, 0, 0))
    if len(headtail) > 1:
        for i in headtail:
            pygame.draw.rect(win, (255, 0, 0), (i[0], i[1], width, height))
    else:
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.draw.rect(win, (255, 255, 0), (gameapple.x, gameapple.y, width, height))
    pygame.display.update()


run = True
gameapple = apple()
while run:
    pygame.time.delay(100)
    if headtail[0] == [gameapple.x, gameapple.y]:
         headtail.append([gameapple.x, gameapple.y])
         del gameapple
         gameapple = apple()
         gameapple.createapplex()
         gameapple.createappley()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == 768:
        if event.key == 1073741904 and not right:
            left = True
            right = False
            up = False
            down = False
        # #elif keys[pygame.K_LEFT] and x < vel:
        #     run = False
        #     print("you lose")
        if event.key == 1073741903 and not left:
            left = False
            right = True
            up = False
            down = False
        # #elif keys[pygame.K_RIGHT] and x >= 500 - width:
        #     run = False
        #     print("you lose")
        if event.key == 1073741906 and not down:
            left = False
            right = False
            up = True
            down = False
        # #elif keys[pygame.K_UP] and y < vel:
        #     run = False
        #     print("you lose")
        if event.key == 1073741905 and not up:
            left = False
            right = False
            up = False
            down = True
        # #elif keys[pygame.K_DOWN] and y >= 500 - height:
        #     run = False
        #     print("you lose")
    if left:
        if (x > vel):
            x -= vel
        else:
            run =False
    if right:
        if (x < 500 - vel -width):
            x += vel
        else:
            run = False
    if down:
        if(y < 500 - height - vel):
            y += vel
        else:
            run = False
    if up:
        if(y > vel):
            y -= vel
        else:
            run = False

    if len(headtail) > 1:
        for i in range(len(headtail)):
            if i < len(headtail):
                if i > 0:
                    headtail[-i] = headtail[-i-1]

    headtail[0] = [x, y]
    for i in range((len(headtail))-1):
        if i > 0:
            if headtail[0] == headtail[i]:
                run = False
    redrawGameWindow()
pygame.quit()




