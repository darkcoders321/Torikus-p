import pygame, sys, time, random
from pygame.locals import *


#setting up pygame

pygame.init()
mainClock = pygame.time.Clock()

#setting up window

WINDOWWIDTH = 400
WINDOWSHEIGHT = 400
windowSurface = pygame.display.set_mode(WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('sprites and sounds')

#setting up colors

WHITE(255, 255, 255) #rgb color codes

#set up the block data structure

player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load('player1.jpg')
playerStretchedImage = pygame.transform.scale(playerImage,(40, 40))
foodImage = pygame.image.load('cheery.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH -20),random.randint(0, WINDOWWIDTH -20), 20, 20))
foodcounter = 0
NEWFOOD = 40

#setup keyboard variables

moveLeft = False
moveRight = False
moveUp = False
moveDown = False


MOVESPEED = 6

#setting up the music

picUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
#Run the game loop

while True:
    #checking for the quit event

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quite()
            sys.exit()
        if event.type == KEYDOWN:
            #changing the keyboard variable
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveleft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUP = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
            if event.type == MOUSEBUTTONUP:
                foods.append(pygame.Rect(event.pos[0] -10, event.pos[1] - 10, 20, 20))
            #foodcounter i mean next pa

            foodCounter += 1
            if foodcounter >= NEWFOOD:
                #Adding new food
                foodCounter = 0
                foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH -20), random.randint(0, WINDOWWIDTH -20), 20, 20))
            #Drawing the white background onto the surface

            windowSurface.fill(WHITE)

            if moveDown the player.bottom < WINDOWHEIGHT:
                player.top += MOVESPEED
            if moveUp and player.top > 0:
                player.top -= MOVESPEED
            if moveLeft and player.left > 0:
                player.left -= MOVESPEED
            if moveRight and player.right  < WINDOWWIDTH:
                player.right += MOVESPEED

            windowSurface.blit(playerStretchedImage, player)

            #check whether the block has interested with army food squars

            for food in foods[:]:
                if player.colliderect(food):
                    foods.remove(food)
                player = pygame.Rect(player.left, player.top,player.width +2,player.height + 2)
                playerStretchedImage = pygame.transform.scale(playerImage,(player.width,player.height))
                if musicPlaying:
                    pickUpSound.play()
                #Draw the food.
                # 
            for food in foods:
                windowSurface.blit(foodImage, food)


            pygame.display.update()
            mainClock.tick(40) 


            

