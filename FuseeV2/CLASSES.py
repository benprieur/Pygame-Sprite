import pygame, random, sys
from CONSTANTES import *
from datetime import timedelta, datetime, date, time

LISTE_PLANETES = pygame.sprite.Group()
LISTE_GLOBALE_SPRITES = pygame.sprite.Group()

class PLANETE(pygame.sprite.Sprite):

  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("img/PLANETE.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

  def update(self):

    self.rect.y = self.rect.y + VITESSE_PLANETES

    if self.rect.y > HAUTEUR_FENETRE:
      LISTE_GLOBALE_SPRITES.remove(self)
      LISTE_PLANETES.remove(self)
      self.kill()

class FUSEE(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("img/FUSEE.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = 210
    self.rect.y = 300
    self.DIRECTION = 'G'

  def update(self):

    print(self.DIRECTION)
    if self.DIRECTION == 'G':
      self.rect.x -= 4
    elif self.DIRECTION == 'D':
      self.rect.x += 4

    if self.rect.x < 0:
      self.rect.x = 0
    elif self.rect.x > LARGEUR_FENETRE - LARGEUR_FUSEE:
      self.rect.x = LARGEUR_FENETRE - LARGEUR_FUSEE

