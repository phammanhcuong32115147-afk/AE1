import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Game variables
gravity = 0.5
bird_movement = 0
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
pipe_width = 60
pipe_gap = 150
pipe_speed = 3
score = 0

# Fonts
font = pygame.font.Font(None, 36)

# Clock
clock = pygame.time.Clock()

# Pipes
pipes = []
pipe_timer = 0


def create_pipe():
    pipe_height = random.randint(100, SCREEN_HEIGHT - pipe_gap - 100)
    top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, pipe_height)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - pipe_height - pipe_gap)
    return top_pipe, bottom_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.x -= pipe_speed
    return [pipe for pipe in pipes if pipe.x + pipe_width > 0]


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.y == 0:  # Top pipe
            pygame.draw.rect(screen, GREEN, pipe)
        else:  # Bottom pipe
            pygame.draw.rect(screen, BLUE, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            return True
    if bird.top <= 0 or bird.bottom >= SCREEN_HEIGHT:
        return True
    return False


# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -10

    # Bird movement
    bird_movement += gravity
    bird_y += bird_movement
    bird = pygame.Rect(bird_x, bird_y, 30, 30)
    pygame.draw.rect(screen, BLACK, bird)

    # Pipe logic
    pipe_timer += 1
    if pipe_timer > 100:
        pipes.extend(create_pipe())
        pipe_timer = 0

    pipes = move_pipes(pipes)
    draw_pipes(pipes)

    # Collision detection
    if check_collision(pipes):
        running = False

    # Score
    for pipe in pipes:
        if pipe.x + pipe_width == bird_x:
            score += 1
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
# Display "Game Over" title
game_over_font = pygame.font.Font(None, 72)
game_over_text = game_over_font.render("Game Over", True, BLACK)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
pygame.display.flip()
pygame.time.wait(2000)  # Wait for 2 seconds before restarting

# Restart the game
bird_movement = 0
bird_y = SCREEN_HEIGHT // 2
pipes = []
pipe_timer = 0
score = 0
running = True