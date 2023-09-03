import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Load background image
background = pygame.image.load('bg.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Snake initial position
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (0, -1)  # Start moving upward

# Food initial position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score
score = 0

font = pygame.font.Font(None, 36)

def draw_snake(snake):
    for i, segment in enumerate(snake):
        x, y = segment
        segment_rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        if i == 0:
            pygame.draw.rect(screen, GREEN, segment_rect)
        else:
            pygame.draw.rect(screen, GREEN, segment_rect)
            pygame.draw.circle(screen, GREEN, (int(x * GRID_SIZE + GRID_SIZE / 2), int(y * GRID_SIZE + GRID_SIZE / 2)), GRID_SIZE // 2)

def draw_food(food):
    x, y = food
    food_rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, RED, food_rect)
    pygame.draw.circle(screen, RED, (int(x * GRID_SIZE + GRID_SIZE / 2), int(y * GRID_SIZE + GRID_SIZE / 2)), GRID_SIZE // 2)

def move_snake(snake, direction):
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)
    if head == food:
        global score
        score += 1
        generate_food()
    else:
        snake.pop()

def generate_food():
    global food
    while True:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if food not in snake:
            break

def check_collision():
    head = snake[0]
    if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT or head in snake[1:]:
        return True
    return False

def draw_score():
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

def main():
    global snake_direction, score

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        move_snake(snake, snake_direction)

        if check_collision():
            print("Game Over! Your Score:", score)
            pygame.quit()
            sys.exit()

        screen.blit(background, (0, 0))
        draw_snake(snake)
        draw_food(food)
        draw_score()
        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

if __name__ == "__main__":
    main()
