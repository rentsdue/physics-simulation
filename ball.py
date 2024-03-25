import pygame

class Ball:
    def __init__(self, x, y, radius, ground_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity_x = 50
        self.velocity_y = -50
        self.acceleration = 9.8
        self.ground_y = ground_y

    def update(self):
        # Update the object's position
        self.velocity_y += self.acceleration
        self.y += self.velocity_y
        self.x += self.velocity_x  # Added horizontal motion

        # Check if the ball hits the ground
        if self.y >= self.ground_y - self.radius:
            self.y = self.ground_y - self.radius  # Keep the ball above or on the ground
            self.velocity_y *= -0.8  # Adjust the 0.8 to change the elasticity

    def draw(self, screen):
        # Draw the object (ball in this case)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)