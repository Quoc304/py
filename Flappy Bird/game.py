import pygame
import sys
import random
pygame.init()

screen = pygame.display.set_mode((432,668))

clock = pygame.time.Clock()

bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)

floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

#Bird
bird = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100,334))

#Pipe
pipe_surface =  pygame.image.load('assets/pipe-green.png').convert()
pipe_surface =  pygame.transform.scale2x(pipe_surface)
pipe_list = []
#Gravity
gravity = 0.25
bird_moment = 0
game_active = True
#Spawn
spawn_pipe = pygame.USEREVENT
#set tỉme cho pipe
pygame.time.set_timer(spawn_pipe, 1200)
pipe_height = [200,300,400]
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos + 436,650))
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos-650))
    return bottom_pipe, top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            return False
    return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_moment * 4,1)
    return new_bird
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_moment = 0
                bird_moment =-11
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100,384)
                bird_moment = 0
        if event.type == spawn_pipe:
                pipe_list.extend(create_pipe())
                
    #==Background==

    screen.blit(bg,(0,0))

    if game_active:
        bird_moment += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_moment

        #==Bird_Image==
        screen.blit(rotated_bird,bird_rect)
        game_active = check_collision(pipe_list)

        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
          
    #==Floor==
    floor_x_pos -= 1
    draw_floor()
    
    

    #==IF==
    if floor_x_pos <= -432:
        floor_x_pos = 0

   
    #==Loop==
    pygame.display.update()
    #==FPS==
    clock.tick(120)
