import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    print(type(current_time))
    score_surface = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)
    print(current_time)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("UltimatePygameIntro-main/font/Pixeltype.ttf", 50)
game_active = False
start_time = 0

sky_surface = pygame.image.load("Sky.png").convert_alpha()
ground_surface = pygame.image.load("UltimatePygameIntro-main/graphics/ground.png").convert_alpha()


#score_surface = test_font.render("Score", False, "Black").convert_alpha()
#score_rect = score_surface.get_rect(midbottom = (400, 75))

snail_surface = pygame.image.load("UltimatePygameIntro-main/graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 800
snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, 300))


player_surface = pygame.image.load("UltimatePygameIntro-main/graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load("UltimatePygameIntro-main/graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))
game_title_surface = test_font.render("I'M COMING FOR YOU", False, (64,64,64))
game_title_rect = game_title_surface.get_rect(center = (400,80))
game_instructions_surface = test_font.render("PRESS THE SPACE-BAR TO PLAY", False, (64,64,64))
game_instructions_rect = game_instructions_surface.get_rect(center = (400, 350))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.x = snail_x_pos
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        #pygame.draw.rect(screen, "pink", score_rect)
        #pygame.draw.rect(screen, "pink", score_rect, 10)
        #screen.blit(score_surface, score_rect)
        display_score()

        snail_rect.left += -4

        if snail_rect.left < -100:
            snail_rect.left = snail_x_pos

        screen.blit(snail_surface, snail_rect)

        # Player
        screen.blit(player_surface, player_rect)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300


        # Collisions
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title_surface, game_title_rect)
        screen.blit(game_instructions_surface, game_instructions_rect)








    pygame.display.update()
    clock.tick(60)