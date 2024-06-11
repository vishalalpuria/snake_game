import pygame
import random
import time
pygame.init()
# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
purp = (106, 21, 106)
blue= (51, 51, 255)

# Creating window (CANVAS)
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update() #jab kabhi screen ko update krege tab ke liye ye function hai



clock_ = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
def screen_score(text, clr, x, y):
    screen_text = font.render(text, True, clr) #text , anti alaising, and color of text
    gameWindow.blit(screen_text, [x,y]) #location of score

font1 = pygame.font.SysFont(None, 55)
def Open_scr_text(text, clr, x, y):
    screen_text = font1.render(text, True, clr) #text , anti alaising, and color of text
    gameWindow.blit(screen_text, [x,y]) #opening screen text

font2 = pygame.font.SysFont(None, 65)
def GameOver_On_Screen(text, clr, x, y):
    screen_text = font2.render(text, True, clr) #text , anti alaising, and color of text
    gameWindow.blit(screen_text, [x,y]) #location of game over

def plot_snake(gameWindow, color,snk_list,size):
    for x,y in snk_list:     
        pygame.draw.rect(gameWindow, color, [x, y, size, size])
        pygame.draw.rect(gameWindow, black, [0, 0, 3, 600]) #Top Border 
        pygame.draw.rect(gameWindow, black, [0, 0, 900, 3]) 
        pygame.draw.rect(gameWindow, black, [897,0, 3, 600])
        pygame.draw.rect(gameWindow, black, [0, 597, 900, 3])
        

def Welcome_Screen():
    flag = True
    while flag:
        gameWindow.fill(white)
        Open_scr_text("Welcome to the Snake Game", purp, 80, 240)
        Open_scr_text("Press Enter to Play", blue, 80, 300)
        screen_score("(Created By Vishal)", black, 699,570)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # jab cross button dabayege tb true ho jayega
                exit_game = True
                flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Game_Loop()
                    flag = False


def gameoverEFFECT(): # for game over sound effect
    pygame.mixer.init()
    pygame.mixer.music.load('mario.mp3')
    pygame.mixer.music.play()
    time.sleep(3)
    pygame.mixer.stop()


def Game_Loop():

    # Game specific variables
    exit_game = False #ye isliye h kyuki agr koi band krta h pygame ko tb ye true hoga/ya koi quit ka button type
    game_over = False # ye true tab hoga jab game over ho jayega    
    snake_x = 45
    velocity_x = 4
    snake_y = 45
    velocity_y = 0
    snake_size = 20
    score = 0 
    apple_x = (random.randint(40,screen_width/10) *10) -20
    apple_y = (random.randint(40,screen_height/10)*10) -20
    # print(apple_x, apple_y)
    fps = 60
    snk_list = []
    snk_length = 1


    # Game loop 
    while not exit_game:
        if game_over == True:
            gameWindow.fill(white)
            GameOver_On_Screen("Game Over! Press Enter to Continue",red,50,280)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # jab cross button dabayege tb true ho jayega
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Game_Loop()
        else: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # jab cross button dabayege tb true ho jayega
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and (velocity_y==-4 or velocity_y==4):
                        velocity_x = 4
                        velocity_y = 0
                    if event.key == pygame.K_LEFT and (velocity_y==-4 or velocity_y==4):
                        velocity_x = -4
                        velocity_y = 0
                    if event.key == pygame.K_UP and (velocity_x==-4 or velocity_x==4):
                        velocity_x = 0
                        velocity_y = -4
                    if event.key == pygame.K_DOWN and (velocity_x==-4 or velocity_x==4):
                        velocity_x = 0
                        velocity_y = 4

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - apple_x) < 8 and abs(snake_y - apple_y) < 8:
                score += 10
                apple_x = (random.randint(40,screen_width/10) *10) - 20
                apple_y = (random.randint(40,screen_height/10)*10) - 20
                snk_length = snk_length + 5 #5 bcoz we are taking the coordinates
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            gameWindow.fill(white)
            screen_score("Score: "+str(score), green, 5, 5)

            if len(snk_list)>snk_length:
                del snk_list[0]
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y,snake_size, snake_size])
            if snake_x<0 or snake_x>screen_width-20 or snake_y<0 or snake_y>screen_height-20:
                game_over = True
                gameoverEFFECT()
            if head in snk_list[:-1]:
                game_over = True
                gameoverEFFECT()
            plot_snake(gameWindow, black, snk_list,snake_size)
            pygame.draw.rect(gameWindow, red, [apple_x, apple_y,snake_size, snake_size])
        clock_.tick(fps)
        pygame.display.update()
        
    pygame.quit()
    quit()


Welcome_Screen()
# Game_Loop() #will start by the welcomescreen function





