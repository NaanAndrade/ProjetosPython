import pygame
pygame.font.init()
pygame.mixer.init()

# Tela
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

BORDER = pygame.Rect(WIDTH // 2, 0, 2, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# Variáveis
FPS = 60
VEL = 5
BULLET_VEL = 15
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 99, 76

# Sessão
DOWN_HIT = pygame.USEREVENT + 1
UP_HIT = pygame.USEREVENT + 2


# Sessão de recolher as imagens & configurar elas
DOWN_SPACESHIP_IMAGE = pygame.image.load('Assets/naveDown.png')
DOWN_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    DOWN_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

UP_SPACESHIP_IMAGE = pygame.image.load('Assets/naveUp.png')
UP_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    UP_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

BACKGROUND = pygame.image.load('Assets/space.png')

# Sessão de criação de imagem
def draw_window(up, down, up_bullets, down_bullets, up_health, down_health):
    # Colocando as imagens com a função Blit
    # A ordem da criação de imagem importa, porque uma sobrepõe a outra
    WINDOW.fill(('black'))
    WINDOW.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WINDOW, 'white', BORDER)

    up_health_text = HEALTH_FONT.render("Health: " + str(up_health), 1, 'white')
    down_health_text = HEALTH_FONT.render("Health: " + str(down_health), 1, 'white')
    WINDOW.blit(up_health_text, (WIDTH - up_health_text.get_width() - 10, 10))
    WINDOW.blit(down_health_text, (10, 10))


    WINDOW.blit(DOWN_SPACESHIP, (down.x, down.y))
    WINDOW.blit(UP_SPACESHIP, (up.x, up.y))



    for bullet in up_bullets:
        pygame.draw.rect(WINDOW, 'green', bullet)
    for bullet in down_bullets:
        pygame.draw.rect(WINDOW, 'red', bullet)


    pygame.display.update()

# Sessão de movimento dos jogadores
def up_handle_movement(keys_pressed, up):
    if keys_pressed[pygame.K_a] and up.x - VEL > BORDER.x:  # LEFT
        up.x -= VEL
    if keys_pressed[pygame.K_d] and up.x + VEL + up.width - 20 < 900:  # RIGHT
        up.x += VEL
    if keys_pressed[pygame.K_s] and up.y + VEL + up.width < 500:  # DOWN
        up.y += VEL
    if keys_pressed[pygame.K_w] and up.y - VEL > 0:  # UP
        up.y -= VEL

def down_handle_movement(keys_pressed, down):
    if keys_pressed[pygame.K_LEFT] and down.x - VEL > 0:  # LEFT
        down.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and down.x + VEL + down.width - 20 < BORDER.x:  # RIGHT
        down.x += VEL
    if keys_pressed[pygame.K_DOWN] and down.y + VEL + down.width < 500:  # DOWN
        down.y += VEL
    if keys_pressed[pygame.K_UP] and down.y - VEL > 0:  # UP
        down.y -= VEL

def handle_bullets(down_bullets, up_bullets, down, up): # Mover, colisão e remover o projetil e resetar os projeteis
    for bullet in down_bullets:
        bullet.x += BULLET_VEL
        if up.colliderect(bullet):
            pygame.event.post(pygame.event.Event(UP_HIT))
            down_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            down_bullets.remove(bullet)

    for bullet in up_bullets:
        bullet.x -= BULLET_VEL
        if down.colliderect(bullet):
            pygame.event.post(pygame.event.Event(DOWN_HIT))
            up_bullets.remove(bullet)
        elif bullet.x < 0:
            up_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, 'white')
    WINDOW.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2,
                            HEIGHT/2 - draw_text.get_height()/2))

    # Por 5 segundos vai mostrar a mensagem
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    # Definindo um retangulo que representem a posição das naves
    up = pygame.Rect(800, 180, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    down = pygame.Rect(20, 180, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    up_bullets = []
    down_bullets = []

    up_health = 10
    down_health = 10

    clock = pygame.time.Clock()  # Auxiliador do FPS
    # run = True, enquanto isso for, rode o jogo
    run = True
    while run:
        # For loops acontecem de acordo com a capacidade do computador
        # Portanto se cria um limitador de frames por segundo
        clock.tick(FPS) # Nunca será mais que 60fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL and len(down_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        down.x + down.width, down.y + down.height // 2 - 2, 10, 5)
                    down_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_LCTRL and len(up_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        up.x, up.y + up.height // 2 - 2, 10, 5)
                    up_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == UP_HIT:
                up_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == DOWN_HIT:
                down_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if up_health <= 0:
            winner_text = "Red Wins"

        if down_health <= 0:
            winner_text = "Blue Wins"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()  # Verifica as teclas pressionadas
        down_handle_movement(keys_pressed, down)
        up_handle_movement(keys_pressed, up)
        handle_bullets(down_bullets, up_bullets, down, up)

        draw_window(up, down, up_bullets, down_bullets, up_health, down_health)

    main()

# Só vai rodar o jogo quando chamar o arquivo main diretamente
if __name__ == "__main__":
    main()


# Sessão de bugs:
# Lado esquerdo quando aperta BAIXO + DIREITA/ESQUERDA não consegue atirar
# Os lados do teclado está invertido, deve ser: AWSD - ESQUERDA / < ^ > v - DIREITA
# Melhorar os sprites