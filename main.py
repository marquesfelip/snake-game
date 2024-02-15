# initial configs
import random
import pygame

pygame.init()
pygame.display.set_caption("Snake Game - Python")
width, height = 960, 680

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# snake params
square_size = 10
game_speed = 25


# Functions
def food_generator():
    food_x = round(
        random.randrange(0, width - square_size) / float(square_size)
    ) * float(square_size)
    food_y = round(
        random.randrange(0, height - square_size) / float(square_size)
    ) * float(square_size)

    return food_x, food_y


def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, green, [food_x, food_y, size, size])


def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], size, size])


def draw_points(points):
    font = pygame.font.SysFont("Arial", 25)
    text = font.render(f"Pontos: {points}", True, red)
    screen.blit(text, [4, 1])


def pick_speed(key_pressed):
    if key_pressed == pygame.K_DOWN:
        speed_x = 0
        speed_y = square_size
    elif key_pressed == pygame.K_UP:
        speed_x = 0
        speed_y = -square_size
    elif key_pressed == pygame.K_RIGHT:
        speed_x = square_size
        speed_y = 0
    elif key_pressed == pygame.K_LEFT:
        speed_x = -square_size
        speed_y = 0

    return speed_x, speed_y


# infinite loop
def play_game():
    end_game = False

    x = width / 2
    y = height / 2

    speed_x = 0
    speed_y = 0

    snake_size = 1
    pixels = []

    food_x, food_y = food_generator()

    while not end_game:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = pick_speed(event.key)

        # Draw the food
        draw_food(square_size, food_x, food_y)

        # update the snake position
        if x < 0 or x >= width or y < 0 or y >= height:
            end_game = True

        x += speed_x
        y += speed_y

        # Draw the snake
        pixels.append([x, y])
        if len(pixels) > snake_size:
            del pixels[0]

        # if snake hits their own body
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True

        draw_snake(square_size, pixels)

        # Draw the points
        draw_points(snake_size - 1)

        # Draw a new food
        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = food_generator()

        # Update screen
        pygame.display.update()
        clock.tick(game_speed)


play_game()
