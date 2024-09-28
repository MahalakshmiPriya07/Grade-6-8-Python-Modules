import pygame
import sys

# Initialize pygame
pygame.init()

# Define colors
grey = (58, 58, 58)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Set up the display surface (window)
display_surface = pygame.display.set_mode((500, 500))

# Set the pygame window title
pygame.display.set_caption('My First Game Screen')

# Load the image file (ensure the path is correct)
try:
    image = pygame.image.load('Pokemon.jpg')
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

# Set the size for the image
DEFAULT_IMAGE_SIZE = (300, 300)

# Scale the image to the desired size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

# Set a default position for the image
DEFAULT_IMAGE_POSITION = (100, 100)

# Main game loop
while True:
    # Fill the display surface with grey
    display_surface.fill(grey)

    # Display the image at the specified position
    display_surface.blit(image, DEFAULT_IMAGE_POSITION)

    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Safely exit the program

    # Update the display with the latest changes
    pygame.display.flip()

    # Control the frame rate (30 frames per second)
    clock.tick(30)
