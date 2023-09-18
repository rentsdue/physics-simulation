import pygame

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Physics Simulation")

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = 0
        self.acceleration = 0.1  # You can adjust this value for gravity

ball = Ball(400, 50, 20)  # Create a ball object

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the object's position
    ball.velocity += ball.acceleration
    ball.y += ball.velocity

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the object (ball in this case)
    pygame.draw.circle(screen, (255, 255, 255), (ball.x, int(ball.y)), ball.radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(10)

pygame.quit()
