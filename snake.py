import pygame
import random

pygame.init()

font=pygame.font.SysFont(None, 55)

#Colors variable
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
screen_width=1200
screen_breath=500
snake_size=15
food_size=10

#Initilize game Window
game_window = pygame.display.set_mode((screen_width,screen_breath))
pygame.display.set_caption('Snake')
pygame.display.update()

#Plotting Snake Pos
def plot_snake(game_window,black,snake_list,snake_size) :
    for x,y in snake_list: 
        pygame.draw.rect(game_window,black,[x,y,snake_size,snake_size]) # Define Snake Pos


def Game_Loop():

    #Game Variable
   
    snake_x= random.randint(40,screen_width-20)
    snake_y=random.randint(40,screen_breath-65) 
    velocity=5
    velocity_y=0
    velocity_x=0
    food_x= random.randint(40,screen_width-5)
    food_y=random.randint(40,screen_breath-62)
    exit_game=False
    game_over=False
    snake_list=[]
    snake_len=1
    score=0
    
    #Game Loop
    while not exit_game:
        if game_over:
            game_window.fill(white)
            game_window.blit(font.render('Game Over.. !! Press Enter to Continue-->>',True,red),[200,200])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                            Game_Loop()
        else:
                # Moving Sanke
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key== 258 or event.key==pygame.K_DOWN:#down
                        velocity_y=velocity
                        velocity_x=0    
                    if event.key== 260 or event.key==pygame.K_LEFT:#left
                        velocity_y=0
                        velocity_x=-velocity
                    if event.key== 262 or event.key==pygame.K_RIGHT:#right
                        velocity_y=0
                        velocity_x=velocity
                    if event.key== 264 or event.key==pygame.K_UP:#up
                        velocity_y=-velocity
                        velocity_x=0  
                    

            game_window.fill(white)   # Define Window Color
            pygame.draw.rect(game_window,red,[ food_x,food_y,food_size,food_size]) # Define Food Pos

            # Making Snake Movable
            snake_y=snake_y+velocity_y
            snake_x=snake_x+velocity_x
            
            # Eating Food 
            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<=6:
                food_x= random.randint(40,screen_width)
                food_y=random.randint(40,screen_breath)
                snake_len +=5
                score+=10
            #Display Score
            game_window.blit(font.render('Score: ' + str(score),True,red),[10,10])
            pygame.draw.line(game_window,black,(0,60),(screen_width,60),5)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
        
            if len(snake_list)>snake_len:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_breath:
                game_over= True
                
            plot_snake(game_window,black,snake_list,snake_size)
        pygame.display.update()
        pygame.time.Clock().tick(30) #Setting Fps


if __name__ == "__main__":
    
    Game_Loop()

