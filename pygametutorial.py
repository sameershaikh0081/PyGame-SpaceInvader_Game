#importing pygame in python
import pygame
import random
import math
from pygame import mixer 

#initilize pygame
pygame.init()
# mixer.init()
#making a window of pygame
window = pygame.display.set_mode((800,600))
#write a title for pygame window
pygame.display.set_caption("My First Game")

#making an icon in pygame
icon = pygame.image.load("calculator.png")
pygame.display.set_icon(icon)

#background
background = pygame.image.load('background.png')

#import musics
# mixer.music.load('background.wav')
# mixer.music.play(-1)

#importing a player image in pygame
#player
playerImg = pygame.image.load("player.png")
playerx = 370
playery = 480
playerx_change = 0

#Enemies
enemyImg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0,800))
    enemyy.append(random.randint(50,150))
    enemyx_change.append(1)
    enemyy_change.append(40)

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletx = 370
bullety = 480
bulletx_change = 1
bullety_change = 10
bullet_state = "ready"

#score

score_value = 0
font = pygame.font.Font('li.ttf',32 )
textX = 10
textY = 10

#Game_Over text
over_font = pygame.font.Font('li.ttf',45)

def show_score(x, y):
    score = font.render("Score : "+ str(score_value),True, (255,255,255))
    window.blit(score,(x, y))

def game_over_text():
    over_text = over_font.render("Game Over!",True, (255,255,255))
    window.blit(over_text,(200, 250))
#adding the player and enemy in pygame
def enemy(x, y, i):
    window.blit(enemyImg[i],(x, y))

def player(x, y):
    window.blit(playerImg,(x, y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bulletImg,(x+16, y+10))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx,2)) + (math.pow(enemyy - bullety,2)))
    if distance < 27:
        return True
    else:
        return False
#Game loop
running = True
while running:
    #changing the background color in pygame
    window.fill((0,255,0))
    #changing the background image
    window.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                # print("left arrow is pressed")
                playerx_change = -6
            if event.key==pygame.K_RIGHT:
                playerx_change = 6
                # print("right arrow is pressed")
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    # bullet_sound = mixer.Sound("laser.wav")
                    # bullet_sound.play()
                    bulletx = playerx
                    fire_bullet(bulletx, bullety)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change =0
    
    playerx += playerx_change
    #for boudaries in our game
    if playerx <=0:
        playerx = 0
    elif playerx>=736:
        playerx = 736

    #for boudaries in our game
    #enemy movement
    for i in range(num_of_enemies):
        #game over 
        if enemyy[i] >440:
            for j in range(num_of_enemies):
                enemyy[j] = 6000
            game_over_text()
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <=0:
            enemyx_change[i] = 4
            enemyy[i] +=enemyy_change[i]
        elif enemyx[i]>=736:
            enemyx_change[i] = -4
            enemyy[i] +=enemyy_change[i]
        collision = iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
            # explosion_sound = mixer.Sound('explosion.wav')
            # explosion_sound.play()
            bullety = 480
            bullet_state = "ready"
            score_value +=1
            print(score_value)
            enemyx[i] = random.randint(0,800)
            enemyy[i] = random.randint(50,150)
        enemy(enemyx[i], enemyy[i], i)

    #bullet movement
    if bullety <=0:
        bullety =480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change

    #function calling
    player(playerx,playery)
    show_score(textX, textY)
    #compulsary to update pygame
    pygame.display.update()