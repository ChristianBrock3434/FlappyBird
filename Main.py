#Kendle Sylvester, Christan brock, Talan Knipp, Wesley Oxman, Callie Shoemaker,Tessa Thomson,Eli Stewart, and Devan Mathis
import pygame
import random
from Player import Player
from Pipe import Pipe
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
  player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  running = True

  clock = pygame.time.Clock()

  allSprites = pygame.sprite.Group()
  allSprites.add(player)

  allPipes = pygame.sprite.Group()

  SPAWN_PIPE = pygame.USEREVENT + 0
  pygame.time.set_timer(SPAWN_PIPE, 2000)

  while running:
    # Event handling
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      
      if event.type == SPAWN_PIPE:
        height = random.randint(100, 350)
        spacing = random.randint(100, 200) 
        topPipe = Pipe(SCREEN_WIDTH, height, True)
        bottomPipe = Pipe(SCREEN_WIDTH, height + spacing)

        allSprites.add(topPipe)
        allPipes.add(topPipe)

        allSprites.add(bottomPipe)
        allPipes.add(bottomPipe)

    # Game logic
    keys = pygame.key.get_pressed()
    if (not player.update(keys)):
      player.kill()
      running = False

    allPipes.update()

    # Collision detection
    if pygame.sprite.spritecollideany(player, allPipes):
        player.kill()
        running = False

    # Drawing code
    screen.fill((255,255,255))
    allSprites.draw(screen)

    # Update screen
    pygame.display.flip()

    clock.tick(60)
  
if __name__ == "__main__":
  pygame.init()
  main()
  pygame.quit()