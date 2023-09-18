import pygame

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Projectile Motion Simulation")

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = 0
        self.acceleration = 9.8  # You can adjust this value for gravity

    def update(self):
        # Update the object's position
        self.velocity += self.acceleration
        self.y += self.velocity

        # Check if the ball hits the ground
        if self.y >= ground_y - self.radius:
            self.y = ground_y - self.radius  # Keep the ball above or on the ground
            self.velocity = -self.velocity  # Reverse the velocity for rebound

    def draw(self, screen):
        # Draw the object (ball in this case)
        pygame.draw.circle(screen, (255, 255, 255), (self.x, int(self.y)), self.radius)

ball = Ball(400, 50, 10)  # Create a ball object
ground_y = 550  # Height of the ground

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
    pygame.time.delay(100)

pygame.quit()
