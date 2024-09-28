import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_size = (500, 500)

# Set up the display surface (window)
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption('Pygame Window with Text')

# Define colors (RGB values)
white = (255, 255, 255)
black = (0, 0, 0)

# Choose a font and size
font = pygame.font.Font(None, 36)  # None uses default font, size 36

# Render the text
text = "Hello, Pygame!"
text_surface = font.render(text, True, black)

# Get the rectangle for the text
text_rect = text_surface.get_rect(center=(window_size[0] // 2, window_size[1] // 2))

# Main game loop
while True:
    # Fill the screen with white background
    screen.fill(white)

    # Draw the text on the screen
    screen.blit(text_surface, text_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.flip()
