import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, w, h, color):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.color = color

        pygame.draw.rect(self.image, color, pygame.rect.Rect(0, 0, 20, 130), 0)

        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels

        if self.rect.y > 770:
            self.rect.y = 770

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)

