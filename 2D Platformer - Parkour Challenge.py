import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer - Parkour Challenge")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
YELLOW = (255, 220, 50)
DARK = (30, 30, 40)
CYAN = (0, 255, 255)

# Physics
gravity = 0.6
jump_power = -14
move_speed = 5.5
flight_speed = 6

# Font
font = pygame.font.SysFont("Arial", 24)
small_font = pygame.font.SysFont("Arial", 18)

# Game variables
current_level = 0
lives = 12
game_over = False
victory = False

class Player(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 60)
        self.vel_y = 0
        self.on_ground = False
        self.start_x = x
        self.start_y = y
        self.flight_end_time = 0
        self.last_flight_use = 0
        self.is_flying = False

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.vel_y = 0
        self.is_flying = False

player = Player(80, 400)

# 5 разных уровней
def create_levels():
    return [
        # Level 1 - Tutorial
        {
            "platforms": [pygame.Rect(0,560,800,40), pygame.Rect(150,460,200,20), pygame.Rect(450,380,180,20), pygame.Rect(100,280,150,20)],
            "hazards": [pygame.Rect(280,540,100,20)],
            "goal": pygame.Rect(720,220,50,60),
            "start": (80,400)
        },
        # Level 2
        {
            "platforms": [pygame.Rect(0,560,800,40), pygame.Rect(100,480,130,20), pygame.Rect(320,400,140,20), pygame.Rect(550,320,150,20), pygame.Rect(200,230,160,20)],
            "hazards": [pygame.Rect(220,540,110,20), pygame.Rect(480,300,60,20)],
            "goal": pygame.Rect(710,150,50,60),
            "start": (80,400)
        },
        # Level 3
        {
            "platforms": [pygame.Rect(0,560,250,40), pygame.Rect(320,470,110,20), pygame.Rect(500,390,130,20), pygame.Rect(150,310,120,20), pygame.Rect(650,240,130,20), pygame.Rect(300,170,150,20)],
            "hazards": [pygame.Rect(200,540,140,20), pygame.Rect(420,360,70,20)],
            "goal": pygame.Rect(720,100,50,60),
            "start": (80,400)
        },
        # Level 4
        {
            "platforms": [pygame.Rect(0,560,800,40), pygame.Rect(80,450,140,20), pygame.Rect(280,370,100,20), pygame.Rect(480,290,160,20), pygame.Rect(650,200,120,20)],
            "hazards": [pygame.Rect(180,540,160,20), pygame.Rect(350,350,50,20)],
            "goal": pygame.Rect(730,130,50,60),
            "start": (80,400)
        },
        # Level 5 - Final
        {
            "platforms": [pygame.Rect(0,560,200,40), pygame.Rect(250,470,110,20), pygame.Rect(420,380,130,20), pygame.Rect(180,290,100,20), pygame.Rect(520,230,140,20), pygame.Rect(650,150,130,20), pygame.Rect(100,100,120,20)],
            "hazards": [pygame.Rect(220,540,130,20), pygame.Rect(380,360,60,20), pygame.Rect(580,210,70,20)],
            "goal": pygame.Rect(720,60,50,60),
            "start": (80,400)
        }
    ]

levels = create_levels()

def load_level(level_idx):
    global player
    data = levels[level_idx]
    player = Player(*data["start"])
    player.start_x, player.start_y = data["start"]
    return data["platforms"], data["hazards"], data["goal"]

platforms, hazards, goal = load_level(current_level)

def draw_ui():
    hints = [
        "A/D or Arrows - Move",
        "SPACE/UP - Jump",
        "W/UP - Fly (1.3 sec, 30 sec cooldown)"
    ]
    for i, text in enumerate(hints):
        surf = small_font.render(text, True, WHITE)
        screen.blit(surf, (20, 20 + i * 26))
   
    level_text = small_font.render(f"Level: {current_level + 1}/5   Lives: {lives}", True, WHITE)
    screen.blit(level_text, (WIDTH - level_text.get_width() - 20, 20))
   
    current_time = time.time()
    if player.is_flying:
        flight_left = max(0, player.flight_end_time - current_time)
        status = small_font.render(f"FLYING! {flight_left:.1f}s", True, CYAN)
        screen.blit(status, (WIDTH//2 - 70, 20))
    else:
        cooldown_left = max(0, 30 - (current_time - player.last_flight_use))
        if cooldown_left > 0:
            status = small_font.render(f"Flight cooldown: {cooldown_left:.1f}s", True, (200, 200, 100))
            screen.blit(status, (WIDTH//2 - 95, 20))

running = True
while running:
    current_time = time.time()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_over:
        screen.fill(DARK)
        screen.blit(font.render("GAME OVER", True, RED), (WIDTH//2 - 110, HEIGHT//2 - 50))
        screen.blit(small_font.render("Press R to Restart", True, WHITE), (WIDTH//2 - 95, HEIGHT//2 + 20))
        if keys[pygame.K_r]:
            current_level = 0
            lives = 12
            game_over = False
            platforms, hazards, goal = load_level(current_level)
        pygame.display.flip()
        continue

    if victory:
        screen.fill(DARK)
        screen.blit(font.render("CONGRATULATIONS!", True, YELLOW), (WIDTH//2 - 140, HEIGHT//2 - 60))
        screen.blit(font.render("You completed all 5 levels!", True, YELLOW), (WIDTH//2 - 160, HEIGHT//2 - 20))
        screen.blit(small_font.render("Press R to Play Again", True, WHITE), (WIDTH//2 - 90, HEIGHT//2 + 40))
        if keys[pygame.K_r]:
            current_level = 0
            lives = 12
            victory = False
            platforms, hazards, goal = load_level(current_level)
        pygame.display.flip()
        continue

    dx = 0
    if keys[pygame.K_a] or keys[pygame.K_LEFT]: dx = -move_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: dx = move_speed

    if (keys[pygame.K_w] or keys[pygame.K_UP]) and not player.is_flying and (current_time - player.last_flight_use) >= 30:
        player.is_flying = True
        player.flight_end_time = current_time + 1.3
        player.last_flight_use = current_time

    if player.is_flying:
        dy = 0
        if keys[pygame.K_w] or keys[pygame.K_UP]: dy = -flight_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: dy = flight_speed
        player.vel_y = dy
        if current_time > player.flight_end_time:
            player.is_flying = False
    else:
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and player.on_ground:
            player.vel_y = jump_power
            player.on_ground = False

    player.x += dx
    for p in platforms:
        if player.colliderect(p):
            if dx > 0: player.right = p.left
            elif dx < 0: player.left = p.right

    if not player.is_flying:
        player.vel_y += gravity
    player.y += player.vel_y

    player.on_ground = False
    for p in platforms:
        if player.colliderect(p):
            if player.vel_y > 0 and not player.is_flying:
                player.bottom = p.top
                player.vel_y = 0
                player.on_ground = True
            elif player.vel_y < 0:
                player.top = p.bottom
                player.vel_y = 0

    if player.y > HEIGHT + 100 or any(player.colliderect(h) for h in hazards):
        lives -= 1
        player.reset()
        if lives <= 0:
            game_over = True

    if player.colliderect(goal):
        current_level += 1
        if current_level >= len(levels):
            victory = True
        else:
            platforms, hazards, goal = load_level(current_level)

    screen.fill(DARK)
    for p in platforms:
        pygame.draw.rect(screen, GREEN, p)
    for h in hazards:
        pygame.draw.rect(screen, RED, h)
        pygame.draw.polygon(screen, (255, 100, 100), [(h.left, h.bottom), (h.centerx, h.top - 5), (h.right, h.bottom)])
    pygame.draw.rect(screen, YELLOW, goal)
    screen.blit(small_font.render("GOAL", True, DARK), (goal.centerx - 20, goal.y - 25))
    pygame.draw.rect(screen, BLUE, player)

    draw_ui()
    pygame.display.flip()

pygame.quit()
sys.exit()