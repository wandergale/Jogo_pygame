import pygame, random, menu
from pygame.locals import *

lista_score = []
def game():
    pygame.init()

    pygame.display.set_caption('Game')

    WIDTH = 500
    HEIGHT = 500

    BACK = (255, 64, 64)
    BACKGROUND = pygame.image.load("C:/Users/wande/Documents/PROJECTS/Python/Jogo_pygame/Jogo_starwars/imagens/star.jpg")

    death_effect = pygame.mixer.Sound("C:/Users/wande/Documents/PROJECTS/Python/Jogo_pygame/Jogo_starwars/musica/explosão.mp3")

    player_size = 50
    player_pos = [WIDTH/2, HEIGHT-2*player_size]
    player_skin = pygame.image.load("C:/Users/wande/Documents/PROJECTS/Python/Jogo_pygame/Jogo_starwars/imagens/oie_transparent.png")

    enemy_size = 50
    enemy_pos = [random.randint(0, WIDTH - enemy_size),0]
    enemy_list = [enemy_pos]
    enemy_skin = pygame.image.load("C:/Users/wande/Documents/PROJECTS/Python/Jogo_pygame/Jogo_starwars/imagens/enemy.png")

    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    fps = pygame.time.Clock()

    SPEED = 2

    score = 0

    My_Font = pygame.font.SysFont("monospace", 35)

    game_over = False

    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/wande/Documents/PROJECTS/Python/Jogo_pygame/Jogo_starwars/musica/millennium_falcon_.mp3")
    pygame.mixer.music.play()
    def set_level(score, SPEED):
        if score < 20:
            SPEED = 5
        elif score < 50:
            SPEED = 7
        elif score < 60:
            SPEED = 9
        elif score < 100:
            SPEED = 15
        else:
            SPEED = 30
        return SPEED
    def drop_enemies(enemy_list):
        delay = random.random()

        if len(enemy_list) < 10 and delay < 0.1:
            x_pos = random.randint(0,WIDTH-enemy_size)
            y_pos = 0
            enemy_list.append([x_pos, y_pos])

    def draw_enemies(enemy_list):
        for enemy_pos in enemy_list:
            # pygame.draw.rect(screen, GREEN,(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
            screen.blit(enemy_skin, enemy_pos)


    def update_enemy_positions(enemy_list,score):
        for indice, enemy_pos in enumerate(enemy_list):
            if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
                enemy_pos[1] += SPEED
            else:
                enemy_list.pop(indice)
                score += 1
        return score

    def collision_check(enemy_list, player_pos):
        for enemy_pos in enemy_list:
            if detect_collision(enemy_pos, player_pos):
                return True
        return False


    def detect_collision(player_pos, enemy_pos):
        p_x = player_pos[0]
        p_y = player_pos[1]

        e_x = enemy_pos[0]
        e_y = enemy_pos[1]

        if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
            if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
                return True
        return False

    cont = 0
    while not game_over:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                x = player_pos[0]
                y = player_pos[1]

                if event.key == pygame.K_LEFT:
                    x -= player_size
                elif event.key == pygame.K_RIGHT:
                    x += player_size

                player_pos = (x,y)

        screen.fill(BACK)
        screen.blit(BACKGROUND,(0,0))

        if detect_collision(player_pos, enemy_pos):          
            pygame.mixer.music.stop()
            death_effect.play()
            pygame.time.wait(2000)
            game_over = True
            print(f'Score: {score}')
            menu.main_menu()


        drop_enemies(enemy_list)
        
        score = update_enemy_positions(enemy_list,score)
        
        SPEED = set_level(score, SPEED)
        
        text = "Score: " + str(score)
        label = My_Font.render(text, 1, (255,255,255))
        screen.blit(label, (WIDTH-200, HEIGHT-40))

        if collision_check(enemy_list, player_pos):
            pygame.mixer.music.stop()
            death_effect.play()
            pygame.time.wait(2000)
            game_over = True
            lista_score.append(score)
            print(f'Score: {score}')
            menu.main_menu()

            

        draw_enemies(enemy_list)

        # pygame.draw.rect(screen, RED,(player_pos[0], player_pos[1], player_size, player_size))    
        screen.blit(player_skin, player_pos)
        fps.tick(60)

        pygame.display.update()
        cont+=1