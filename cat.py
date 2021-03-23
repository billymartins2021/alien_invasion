import pygame

class Cat:
    """A class to manage the cat, which may take the place of the ship."""

    def __init__(self, ai_game):
        """Initialize the cat and then set it's starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the cat image and get its rect.
        self.image = pygame.image.load('images/cat.bmp')
        self.rect = self.image.get_rect()

        # Start each new cat at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the cat at its current location."""
        self.screen.blit(self.image, self.rect)
