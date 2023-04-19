from pygame import *

WIDTH = 800
HEIGHT = 600
screen = display.set_mode((WIDTH,HEIGHT))
clock = time.Clock()
display.set_caption("Retro Pong 84'")

black = (0,0,0)
white = (255,255,255)

paddle_width = 15
paddle_height = 100
paddle_speed = 5

player1_pos = [50,(HEIGHT-paddle_height)/2]
player2_pos = [WIDTH-50-paddle_width,(HEIGHT-paddle_height)/2]

ball_pos = [(WIDTH/2),(HEIGHT/2)]
ball_speed = [7,7]

def draw_paddle(pos):
    draw.rect(screen,white,(pos[0],pos[1],paddle_width,paddle_height))

def draw_ball(pos):
    draw.circle(screen,white,pos,15)
    
def update_ball():
    global ball_pos, ball_speed, player1_score,player2_score
    
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]
    
    if ball_pos[1] <= 10 or ball_pos[1] >= HEIGHT-10:
        ball_speed[1] = -ball_speed[1]
        
    if ball_pos[0] <player1_pos[0] + paddle_width and player1_pos[1] <= ball_pos[1] <= player1_pos[1]+ paddle_height:
        ball_speed[0] = -ball_speed[0]
        
    elif ball_pos[0] >= player2_pos[0] and player2_pos[1] <= ball_pos[1] <= player2_pos[1] + paddle_height:
        ball_speed[0] = -ball_speed[0]
        
    if ball_pos[0] <= 0:
        player2_score += 1
        reset()
    if ball_pos[0] >= WIDTH:
        player1_score += 1
        reset()
    

def reset():
    global ball_pos, ball_speed
    ball_pos = [(WIDTH/2),(HEIGHT/2)]
    ball_speed = [7,7]




player1_score = 0
player2_score = 0
font.init()
score_font = font.Font(None,45)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            quit()
            run = False
    
    keys = key.get_pressed()
    if keys[K_w] and player1_pos[1]>0:
        player1_pos = (player1_pos[0],player1_pos[1]-paddle_speed)
    elif keys[K_s] and player1_pos[1]<HEIGHT-paddle_height:
        player1_pos = (player1_pos[0],player1_pos[1]+paddle_speed)
        
    if keys[K_UP] and player2_pos[1]>0:
        player2_pos = (player2_pos[0],player2_pos[1]-paddle_speed)
    elif keys[K_DOWN] and player2_pos[1]<HEIGHT-paddle_height:
        player2_pos = (player2_pos[0],player2_pos[1]+paddle_speed)
        
    update_ball()
    screen.fill(black)
    
    draw_paddle(player1_pos)
    draw_paddle(player2_pos)
    draw_ball(ball_pos)
    
    player1_text = score_font.render(str(player1_score),True,white)
    player2_text = score_font.render(str(player2_score),True,white)
    screen.blit(player1_text,(WIDTH/4,20))
    screen.blit(player2_text,(WIDTH*3/4,20))

    if player1_score >= 5 or player2_score >=5:
        run = False
    
            
    display.update()
    clock.tick(40)