import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
    super().__init__()

    self.SCREEN_WIDTH, self.SCREEN_HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT

    self.image = pygame.image.load("flappyBird.png")
    self.rect = self.image.get_rect(center = (SCREEN_WIDTH/4, SCREEN_HEIGHT/3))
    
    self.yVelocity = pygame.math.Vector2(0, 0)

  def update(self, keys):
    self.yVelocity += pygame.math.Vector2(0, 0.1)
    if self.yVelocity.y > 5:
      self.yVelocity.y = 5

    if keys[pygame.K_SPACE]:
        self.yVelocity = pygame.math.Vector2(0, -5)


    self.rect.move_ip(self.yVelocity)

    if self.rect.top < 0:
      return False
    elif self.rect.bottom > self.SCREEN_HEIGHT:
      return False
    return True
