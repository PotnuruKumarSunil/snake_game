import pygame
import random
pygame.init()
white=(255,255,255)
yellow=(255,255,0)
red=(255,0,0)
black=(0,0,0)
gameWind=pygame.display.set_mode((900,500))
pygame.display.set_caption("SnakeGame")
pygame.display.update()
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,40)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWind.blit(screen_text,[x,y])
def plot_snake(gameWind,color,snk_list,snake_size):
    for  x,y in snk_list:
        pygame.draw.rect(gameWind,color,[x,y,snake_size,snake_size])
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 450
    snake_y = 250
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    foodx = random.randint(0, 800)
    foody = random.randint(0, 400)
    fps = 30
    score = 0
    snk_list = []
    snk_len = 1
    while exit_game==False:
        if game_over:
            gameWind.fill(red)
            text_screen("Game Over! , Press ENTER to continue",yellow,200,100)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=5
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-5
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-5
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=5
                        velocity_x=0
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            if abs(snake_x-foodx)<6 and abs(snake_y-foody)<6:
                score+=1
                foodx = random.randint(0, 800)
                foody = random.randint(0, 400)
                snk_len+=5
            gameWind.fill(white)
            text_screen("Score:" + str(score * 10), red, 5, 5)
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_len:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>500:
                game_over=True
            pygame.draw.rect(gameWind,yellow,[foodx,foody,snake_size,snake_size])
            plot_snake(gameWind,black,snk_list,snake_size)
        clock.tick(fps)
        pygame.display.update()
    pygame.quit()
    quit()
gameloop()