import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player car
player_car_img = pygame.image.load("player_car.png")  # Replace "player_car.png" with your car image
player_car_width, player_car_height = player_car_img.get_size()
player_car_x = (WIDTH - player_car_width) // 2
player_car_y = HEIGHT - player_car_height - 20
player_car_speed = 10

# Enemy car
enemy_car_img = pygame.image.load("enemy_car.png")  # Replace "enemy_car.png" with enemy car image
enemy_car_width, enemy_car_height = enemy_car_img.get_size()
enemy_car_x = random.randint(0, WIDTH - enemy_car_width)
enemy_car_y = -enemy_car_height
enemy_car_speed = 6

clock = pygame.time.Clock()

def draw_player_car(x, y):
    screen.blit(player_car_img, (x, y))

def draw_enemy_car(x, y):
    screen.blit(enemy_car_img, (x, y))

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_car_x -= player_car_speed
    if keys[pygame.K_RIGHT]:
        player_car_x += player_car_speed

    # Move the enemy car
    enemy_car_y += enemy_car_speed
    if enemy_car_y > HEIGHT:
        enemy_car_x = random.randint(0, WIDTH - enemy_car_width)
        enemy_car_y = -enemy_car_height

    # Check for collision
    if (player_car_x < enemy_car_x + enemy_car_width and
        player_car_x + player_car_width > enemy_car_x and
        player_car_y < enemy_car_y + enemy_car_height and
        player_car_y + player_car_height > enemy_car_y):
        game_over()
        break

    # Draw cars
    draw_player_car(player_car_x, player_car_y)
    draw_enemy_car(enemy_car_x, enemy_car_y)

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
