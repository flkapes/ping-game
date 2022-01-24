import pygame
from pygame.locals import *
from Player import *
from Ball import *
import pygame.freetype

clock = None
window = None
font = None
width, height = 1600, 900
fps = 30


def init_ping(w, h):
    global clock
    global window
    global font
    pygame.init()
    font = pygame.freetype.SysFont("Comic Sans MS", 30)
    resolution = (w, h)
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Ping: My PyGame Implementation of Pong")


all_sprites_list = pygame.sprite.Group()

playerA = Player(20, 130, (245, 66, 152))
playerA.rect.x = 5
playerA.rect.y = 15

playerB = Player(20, 130, (0, 100, 160))
playerB.rect.x = 1575
playerB.rect.y = 740


def add_ball(x, y, width, height):
    ball = Ball((255, 255, 255), x, y)
    ball.rect.x = width / 2
    ball.rect.y = height / 2
    all_sprites_list.add(ball)


all_sprites_list.add(playerA)
all_sprites_list.add(playerB)


def main():
    running = True
    add_ball(10, 10, width, height)
    ball = all_sprites_list.sprites()[-1]
    scoreA = 0
    scoreB = 0
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:  # Checks if user has closed the game
                running = False

        all_sprites_list.update()
        window.fill((0, 0, 0))

        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_k]:
            playerA.move_down(dist)
        if key[pygame.K_i]:
            playerA.move_up(dist)
        if key[pygame.K_w]:
            playerB.move_up(dist)
        if key[pygame.K_s]:
            playerB.move_down(dist)
        if ball.rect.x > 1599:
            scoreA += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            scoreB += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y > 899:
            ball.velocity[1] = -ball.velocity[1]

        if ball.is_collided_with(all_sprites_list.sprites()[1]) or ball.is_collided_with(all_sprites_list.sprites()[0]):
            ball.bounce()

        all_sprites_list.draw(window)
        ball.update()
        text = "{}          {}".format(str(scoreA), str(scoreB))
        text_rect = font.get_rect(text, size=30)
        text_rect.center = window.get_rect().center
        text_rect.top = 30
        font.render_to(window, text_rect, text, (255, 255, 255), size=30)
        pygame.display.flip()
        clock.tick(fps * 2)


if __name__ == '__main__':
    init_ping(width, height)
    main()
