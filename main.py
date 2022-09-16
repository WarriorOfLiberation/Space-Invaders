import pygame
import random
import math
#initialsie the pygame
score=0
pygame.init()

# create the screen

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("The space invaders")
icon=pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)
running = True

#score
font = pygame.font.Font('freesansbold.ttf', 30)
textX=10
textY=10

def showscore(x, y):
    score_val = font.render("Score :"+str(score), True, (0, 0, 0))
    screen.blit(score_val, (x, y))

def gameover():
    over_text=font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (300, 300))

backgroundimg = pygame.image.load('wepik-purple-space-stars-desktop-wallpaper-2022816-5229.png')
backgroundimg = pygame.transform.scale(backgroundimg, (800, 800))
#player
playerImg=pygame.image.load('ship.png')
playerX = 370
playerY=440
dx = 0
dy = 0

def player(x, y):
    screen.blit(playerImg, (x, y))
#enemy
enemyImg = []
enemyX = []
enemyY = []
dex = []
dey = []
num_enemies = 6
for i in range(num_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(0, 150))
    dex.append(4)
    dey.append(100)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

#bullet

# ready means bullet is not moving
bulletImg=pygame.image.load('bullet.png')
bulletX = playerX
bulletY = playerY
dbx=0
dby=10
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def collison(x1, x2, y1, y2):
    r=math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2, 2))
    if r<27:
        return True
    else:
        return False

# game loop, make sure the game runs infinitely
while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundimg, (0, 0))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                dx=-5
                print("Left ")
            if events.key == pygame.K_RIGHT:
                dx=5
                print("Right")
            if events.key == pygame.K_UP:
                dy=-5
            if events.key == pygame.K_DOWN:
                dy=5
            if events.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if events.type == pygame.KEYUP:
            dx=0
            dy=0


    # function called after the filling the screen since first the screen is formed then we draw something
    if playerX+dx>=800-64:
        playerX=800-64
    if playerX + dx <= 0:
        playerX=0

    playerX+=dx

    if playerY + dy >= 800-64:
        playerY = 800-64
    if playerY + dy <= 0:
        playerY = 0

    playerY+=dy

    # controlling the enemy movement
    for i in range(num_enemies):
        enemyX[i]+= dex[i]

        if enemyX[i]<= 0:
            enemyX[i]= 0
            enemyY[i] += dey[i]
            dex[i] = 4
        if enemyX[i] >= 736:
            enemyX[i] = 736
            enemyY[i] += dey[i]
            dex[i] = -4
        if  enemyY[i]>=600:
            for j in range(num_enemies):
                enemyY[i]=2000
            gameover()




        # collison

        if collison(bulletX, enemyX[i], bulletY, enemyY[i]):
            bulletY = playerY
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(0, 150)
            print(score)
        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY-=dby
        if bulletY<=0:
            bullet_state = "ready"
            bulletY=playerY
    showscore(textX, textY)
    pygame.display.update()


