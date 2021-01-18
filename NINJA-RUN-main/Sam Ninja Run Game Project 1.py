'''
Project Title: Ninja Run
Class-Section: XI-G
Developed by : Saksham Virmani & Yash Jain
'''

#importing pygame
import pygame
from pygame.locals import *

#initialize pygame module
pygame.init()
#screen height and width
screen = pygame.display.set_mode((600, 400))

#screen title
pygame.display.set_caption('Ninja Run')

#font
font = pygame.font.Font('freesansbold.ttf', 20)

#background
bg = pygame.image.load('background.png')


#player 
player = pygame.image.load('dra1.png')
player = pygame.transform.scale(player, (50 ,50))
player1= pygame.image.load('dra2.png')
player1= pygame.transform.scale(player1, (50 ,50))
player2= pygame.image.load('dra3.png')
player2= pygame.transform.scale(player2, (50 ,50))
player3= pygame.image.load('dra4.png')
player3= pygame.transform.scale(player3, (50 ,50))
player4= pygame.image.load('dra5.png')
player4= pygame.transform.scale(player4, (50 ,50))



walk = [player, player,player,player, player, player,player,player,player, player,player,player,player1, player1,player1,player1,player1, player1,player1,player1,player1, player1,player1,player1,player2, player2,player2,player2,player2, player2,player2,player2,player2, player2,player2,player2,player3,player3,player3,player3,player3,player3,player3,player3,player3,player3,player3,player3, player4, player4, player4, player4 ,player4, player4, player4, player4, player4, player4, player4, player4]


#obstacles

obstacle = pygame.image.load('hurdle1.png')
obstacle = pygame.transform.scale(obstacle, (70, 70))
obstacle1 = pygame.image.load('hurdle2.png')
obstacle1 = pygame.transform.scale(obstacle1, (90, 90))
obstacle2 = pygame.image.load('hurdle3.png')
obstacle2 = pygame.transform.scale(obstacle2, (90, 90))
obstacle3 = pygame.image.load('hurdle5.png')
obstacle3 = pygame.transform.scale(obstacle3, (150, 150))
obstacle4 = pygame.image.load('hurdle4.png')
obstacle4 = pygame.transform.scale(obstacle4, (90, 90))

def gameloop():
    bg_velocity = 0
    bg_x = 0
    bg_y = 0
    white = (255,255,255)
    black = (0, 0, 0)
    gravity = 4.15
    walkpoint = 0
    score = 0
    hscore = 0
    game = False
    jump = False
    gameover = False
    obstacle_x = 650
    obstacle_y = 280
    player_x = 50
    player_y = 275
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
              pygame.quit()
            if event.type == KEYDOWN:
               if event.key == K_UP or event.key == K_SPACE:
                   if player_y == 275:
                     jump = True
                     game = True
                     bg_velocity = 3
               if gameover == True:
                   if event.key == K_UP or event.key == K_SPACE:
                       gameloop()
            
        

    #infinite scrollong background
        if bg_x == -600:
            bg_x = 0
        if obstacle_x < -1600:
            obstacle_x = 550
    
    #jump function
        if  276 > player_y > 125:
            if jump == True:
                player_y -= gravity
        else:
            jump = False

            
        if player_y <275:
            if jump == False:
                player_y += gravity
    
    #collision
        if obstacle_x < player_x + 50 < obstacle_x + 70 and obstacle_y < player_y+50 < obstacle_y+50:
            bg_velocity = 0
            walkpoint = 0
            game = False
            gameover = True
        if obstacle_x +400< player_x + 50 < obstacle_x + 470 and obstacle_y < player_y+50 < obstacle_y+50:
            bg_velocity = 0
            walkpoint = 0
            game = False
            gameover = True
        if obstacle_x +800< player_x + 50 < obstacle_x + 870 and obstacle_y < player_y+50 < obstacle_y+50:
            bg_velocity = 0
            walkpoint = 0
            game = False
            gameover = True
        if obstacle_x +1200< player_x + 50 < obstacle_x + 1270 and obstacle_y < player_y+50 < obstacle_y+50:
            bg_velocity = 0
            walkpoint = 0
            game = False
            gameover = True
        if obstacle_x +1610< player_x + 50 < obstacle_x + 1660 and obstacle_y < player_y+50 < obstacle_y+50:
            bg_velocity = 0
            walkpoint = 0
            game = False
            gameover = True
            
        if game == True:
         score+=1

        if gameover == True:
            if hscore<score:
                hscore=score

        bg_x -= bg_velocity
        obstacle_x -= bg_velocity
        screen.fill(white)

    #game over text
        text = font.render('SCORE : '+ str(score), True, black)
        text1 = font.render('Game Over !!', True, black)
        text2 = font.render('Press SPACE or UP key to Continue', True, black)
        text3 = font.render(' HIGH SCORE : ' + str(hscore),True, black)
        screen.blit(bg, [bg_x, bg_y]) #position of background
        screen.blit(bg, [bg_x + 600, bg_y])

    #animation of player
        screen.blit(walk[walkpoint], [player_x, player_y]) #position of player
        walkpoint += 1
        if walkpoint > len(walk)-1:
            walkpoint = 0
    
        screen.blit(text3,[400,50])
        screen.blit(text, [460, 100])
        if gameover == True:
            screen.blit(text1, [243, 150])
            screen.blit(text2, [140, 180])

    #obstacle repetition
        screen.blit(obstacle, [obstacle_x, obstacle_y-10])
        screen.blit(obstacle1,[obstacle_x + 400, obstacle_y-35])
        screen.blit(obstacle2,[obstacle_x + 800, obstacle_y-40 ])
        screen.blit(obstacle3,[obstacle_x + 1200, obstacle_y -75])
        screen.blit(obstacle4,[obstacle_x + 1600, obstacle_y-40 ])

        pygame.display.update()
        
gameloop()
