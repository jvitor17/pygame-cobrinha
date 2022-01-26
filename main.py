import pygame, random

from pygame.locals import *


def on_grid_random():
    x = random.randint(2,58)
    y = random.randint(2,58)
    return(x * 10, y * 10)

def collision(c1,c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])

#Customize game here
background_color = (20,20,20) #Default: 20, 20, 20
apple_color = (191,38,38) #Default: 191, 38, 38
snake_color = (180,180,180) #Default: 180, 180, 180
tick_speed = 13 #Default: 10
draw_grid = False #Default: False

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

rgb_red = 180
rgb_green = 180
rgb_blue = 180

pygame.init()

pygame.mixer.music.set_volume(0.3)
musica_de_fundo = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((600,700))
pygame.display.set_caption("Cobrinha")

#Snake creation
snake = [(200,200),(210,200),(220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((180,180,180))

#Apple creation
apple = pygame.Surface((10,10))
apple.fill(apple_color)
apple_pos = on_grid_random()

my_direction = LEFT

score = 0

clock = pygame.time.Clock()

game_over = False

fonte = pygame.font.SysFont('arial', 80, True, False)

while not game_over:

    rgb_red = random.randint(30,180)
    rgb_green = random.randint(30,180)
    rgb_blue = random.randint(30,180)

    clock.tick(tick_speed)
    mensagem = f'{score}'
    texto_formatado = fonte.render(mensagem, True, (180,180,180))

    #Verifica os eventos do jogo
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True

        #Keyboard input to snake movement
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    #Snake collision on apple
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score += 1
        apple.fill((rgb_red, rgb_green, rgb_blue))

    #Snake collision on boundaries
    if snake[0][0] == 600 or snake[0][1] == 600:
        game_over = True
        break
    if snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    #Snake direction control
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range(len(snake) - 1, 0, -1,):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #Main section
    pygame.draw.rect(screen, (180,180,180), (0, 0,600,600))
    pygame.draw.rect(screen, (20,20,20), (2, 2,596,600))

    screen.blit(apple, apple_pos)

    #Draw grid on screen
    if draw_grid == True:
        for x in range(0, 600, 10):
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
        for y in range(0, 600, 10):
            pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

    #Lower section
    pygame.draw.rect(screen, (180,180,180), (0,600,600,100))
    pygame.draw.rect(screen, (20,20,20), (2,602,596,96))
    screen.blit(texto_formatado, (20,605))

    #pygame.draw.line(screen, (40, 40, 40), (600/2, 0), (600/2, 700))

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()
pygame.quit()
