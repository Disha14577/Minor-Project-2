import pygame, sys, random, math, time
pygame.init()

# Screen setup
WIDTH, HEIGHT = 798, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racing Beast')
pygame.display.set_icon(pygame.image.load('logo.jpeg'))

# Fonts and Music
font_large = pygame.font.Font("freesansbold.ttf", 38)
font_small = pygame.font.Font("freesansbold.ttf", 25)
pygame.mixer.init()

# Images
bg = pygame.image.load('bg.png')
maincar_img = pygame.image.load('car.png')
enemy_imgs = [pygame.image.load(f'car{i}.png') for i in range(1, 4)]
intro_img = pygame.image.load("intro.png")
about_img = pygame.image.load("About.png")
instruction_img = pygame.image.load("instruction.png")
gameover_img = pygame.image.load("gameover.png")

# Load Sounds
crash_sound = pygame.mixer.Sound('game_over.wav')

def show_text(text, x, y, font, color=(255, 0, 0)):
    rendered = font.render(text, True, color)
    screen.blit(rendered, (x, y))

def show_score(score, highscore):
    show_text(f"SCORE: {score}", 570, 280, font_small)
    show_text(f"HISCORE: {highscore}", 0, 0, font_small)

def is_collision(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2) < 50

def countdown():
    pygame.mixer.music.load('countdown.mp3')
    pygame.mixer.music.play()
    numbers = ['3', '2', '1', 'GO!!!']
    for i, num in enumerate(numbers):
        screen.blit(bg, (0, 0))
        show_text(num, 350 if num != "GO!!!" else 300, 250, pygame.font.Font('freesansbold.ttf', 85), (0, 255, 0))
        pygame.display.update()
        time.sleep(1)
    game_loop()
def intro_screen():
    click = False
    run = True
    pygame.mixer.music.load('background_music.mp3')
    pygame.mixer.music.play()
    while True:
        screen.fill((0, 0, 0))
        screen.blit(intro_img, (0, 0))
        buttons = [
            pygame.Rect(60, 440, 175, 50),    # Play
            pygame.Rect(265, 440, 300, 50),   # Instruction
            pygame.Rect(600, 440, 165, 50)    # About
        ]
        texts = ["PLAY", "INSTRUCTION", "ABOUT"]
        for i, rect in enumerate(buttons):
            pygame.draw.rect(screen, (255, 255, 255), rect, 6)
            show_text(texts[i], rect.x + 10, rect.y + 5, font_large)
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (155, 0, 0), rect, 6)
                if click:
                    if i == 0: countdown()
                    elif i == 1: display_image(instruction_img)
                    elif i == 2: display_image(about_img)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        pygame.display.update()

def display_image(img):
    while True:
        screen.blit(img, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return

def game_loop():
    pygame.mixer.music.load('BackgroundMusic.mp3')
    pygame.mixer.music.play()

    main_x, main_y = 350, 495
    dx, dy = 0, 0
    speed = 5
    enemies = [{'img': img, 'x': random.randint(178, 490), 'y': -i * 150} for i, img in enumerate(enemy_imgs)]
    enemy_speed = 10

    with open("highscore.txt", "r") as f:
        highscore = int(f.read())

    score = 0
    clock = pygame.time.Clock()

    while True:
        screen.blit(bg, (0, 0))
        screen.blit(maincar_img, (main_x, main_y))
        for enemy in enemies:
            screen.blit(enemy['img'], (enemy['x'], enemy['y']))
            enemy['y'] += enemy_speed
            if enemy['y'] > HEIGHT:
                enemy['y'] = random.randint(-300, -100)
                enemy['x'] = random.randint(178, 490)
                score += 1

        if score > highscore:
            highscore = score

        show_score(score, highscore)
        main_x += dx
        main_y += dy
        main_x = max(178, min(490, main_x))
        main_y = max(0, min(495, main_y))

        for enemy in enemies:
            if is_collision(main_x, main_y, enemy['x'], enemy['y']):
                pygame.mixer.music.stop()
                crash_sound.play()
                time.sleep(1)
                with open("highscore.txt", "w") as f:
                    f.write(str(highscore))
                return game_over(score, highscore)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: dx = speed
                if event.key == pygame.K_LEFT: dx = -speed
                if event.key == pygame.K_UP: dy = -speed
                if event.key == pygame.K_DOWN: dy = speed
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT]: dx = 0
                if event.key in [pygame.K_UP, pygame.K_DOWN]: dy = 0

        pygame.display.update()
        clock.tick(60)

def game_over(score, highscore):
    while True:
        screen.blit(gameover_img, (0, 0))
        show_text(f"SCORE: {score}", 330, 400, font_small)
        show_text(f"HISCORE: {highscore}", 330, 450, font_small)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: countdown()
                if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()

# Run the game
intro_screen()
