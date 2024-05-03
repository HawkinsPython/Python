import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokémon Sprite")

# Load Pokémon sprite
pokemon_image = pygame.image.load(os.path.join('sprites', 'pikachu.png'))  # Provide the path to your Pokémon sprite

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill((255, 255, 255))  # White background

    # Blit Pokémon sprite onto the screen
    screen.blit(pokemon_image, (screen_width // 2 - pokemon_image.get_width() // 2,
                                screen_height // 2 - pokemon_image.get_height() // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
