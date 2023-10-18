import pygame

class Pipe(pygame.sprite.Sprite):
  def __init__(self, START_X, START_Y, inverted = False):
    super().__init__()
    self.image = pygame.image.load("pipe.png")
    self.image = pygame.transform.scale(self.image, (46*1.5, 294*2))

    if inverted:
      self.image = pygame.transform.rotate(self.image, 180)
      self.rect = self.image.get_rect(bottomleft = (START_X, START_Y))
    else:
      self.rect = self.image.get_rect(topleft = (START_X, START_Y))

    self.speed = 3
    

  def update(self):
    self.rect.move_ip(-self.speed, 0)


    