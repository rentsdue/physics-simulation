import pygame
from ball import Ball

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Projectile Motion Simulation")

ball_radius = 10  # Radius of the ball
ball_x = 0  # Initial x-position of the ball
ground_y = 550  # Height of the ground

# Create a ball object starting at the ground
ball = Ball(ball_x, ground_y - ball_radius, ball_radius, ground_y)

# Create a ground surface
ground_color = (0, 255, 0)  # Green color for the ground
ground = pygame.Surface((800, 50))
ground.fill(ground_color)

trajectory_points = []  # List to store trajectory points

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the object
    ball.update()

    # Add the current position to the trajectory points
    trajectory_points.append((ball.x, ball.y))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ground
    pygame.draw.rect(screen, (0, 255, 0), (0, ground_y, 800, 50))  # Green ground rectangle

    # Draw the trajectory
    if len(trajectory_points) > 1:
        pygame.draw.lines(screen, (255, 0, 0), False, trajectory_points, 2)

    # Draw the object
    ball.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(300)

pygame.quit()
