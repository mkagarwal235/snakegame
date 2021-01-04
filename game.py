

import pygame
import random
import os
pygame.mixer.init()



pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
# background image
bgimage=pygame.image.load('snake.jfif')
bgimage=pygame.transform.scale(bgimage,(screen_width,screen_height)).convert_alpha()

# welcome image

welimage=pygame.image.load('wel1.jfif')
welimage=pygame.transform.scale(welimage,(screen_width,screen_height)).convert_alpha()
# game over image

gameimg=pygame.image.load('gameover.jfif')
gameimg=pygame.transform.scale(gameimg,(screen_width,screen_height)).convert_alpha()
# Game Title
pygame.display.set_caption("SnakesWithMonu")
pygame.display.update()



clock = pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    scren_text=font.render(text,True,color)
    gameWindow.blit(scren_text,[x,y])
def plot_snake(gameWindow,black,snk_list,snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((230,235,245))
        gameWindow.blit(welimage,(0,0))
        # text_screen("Welcome to Snakes",red,250,200)
        # text_screen("Press Space Bar to Play",black,230,250)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    pygame.mixer.music.load('bground.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snk_list = []
    snk_length = 1
    velocity_x = 0
    velocity_y = 0
    if not os.path.exists('hiscore.txt'):
        with open('hiscore.txt','w') as f:
            f.write("0")
    with open("hiscore.txt",'r') as f:
        hiscore=f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 15
    fps = 30
    while not exit_game:
        if game_over:
            with open("hiscore.txt",'w') as f:
                f.write(str(hiscore))
            gameWindow.fill((200,245,220))
            gameWindow.blit(gameimg,(0,0))
            text_screen("Press Space bar to Continue! ",(250,210,200),150,380)
            text_screen(f"Score: {score}",(230,150,180),300,430)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key==pygame.K_q:
                        score+=10
                    if event.key==pygame.K_u:
                        init_velocity+=5
                    if event.key==pygame.K_d:
                        init_velocity-=5


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                pygame.mixer.music.load('eatig.mp3')
                pygame.mixer.music.play()
                # pygame.mixer.music.rewind()

                # pygame.mixer.music.pause()
                score +=10
                # print("Score: ", score * 10)
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length+=5
                if score>int(hiscore):
                    hiscore=score

            gameWindow.fill((200,150,230))
            gameWindow.blit(bgimage,(0,0))
            text_screen(" Score:"+ str(score) + " Hiscore:"+ str(hiscore),red,5,5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                # print("game over")

            plot_snake(gameWindow,black,snk_list,snake_size)

        # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()


