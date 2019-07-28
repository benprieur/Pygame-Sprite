import pygame, random, sys
from CONSTANTES import *
from datetime import timedelta, datetime, date, time

LISTE_OBJETS = pygame.sprite.Group()
LISTE_MURS = pygame.sprite.Group()
LISTE_GLOBALE_SPRITES = pygame.sprite.Group()

class MUR(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("MUR.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = TUILE_TAILLE * y + SCORE_HAUTEUR
    self.rect.x = TUILE_TAILLE * x

class OBJET(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("OBJET.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = random.randint(0, TUILE_NOMBRE - 1) * TUILE_TAILLE + SCORE_HAUTEUR
    self.rect.x = random.randint(0, TUILE_NOMBRE - 1) * TUILE_TAILLE

class PERSONNAGE(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("PERSONNAGE.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = random.randint(0, TUILE_NOMBRE - 1) * TUILE_TAILLE + SCORE_HAUTEUR
    self.rect.x = random.randint(0, TUILE_NOMBRE - 1) * TUILE_TAILLE
    self.POINTS = 0
    self.TERMINE = False
    self.DIRECTION = '-'
    self.chrono = Chrono()

  def update(self):
    X_COURANT = self.rect.x
    Y_COURANT = self.rect.y
    if self.DIRECTION == 'G':
      self.rect.x -= TUILE_TAILLE
      self.DIRECTION = '-'
    elif self.DIRECTION == 'D':
      self.rect.x += TUILE_TAILLE
      self.DIRECTION = '-'
    elif self.DIRECTION == 'H':
      self.rect.y -= TUILE_TAILLE
      self.DIRECTION = '-'
    elif self.DIRECTION == 'B':
      self.rect.y += TUILE_TAILLE
      self.DIRECTION = '-'

    LISTE_COLLISION_MUR = pygame.sprite.spritecollide(self, LISTE_MURS, False)
    if len(LISTE_COLLISION_MUR) > 0:
        self.rect.x = X_COURANT
        self.rect.y = Y_COURANT

    LISTE_COLLISION_OBJET = pygame.sprite.spritecollide(self, LISTE_OBJETS, False)
    for objet in LISTE_COLLISION_OBJET:
      objet.kill()
      self.POINTS += POINT_UNITE
      if self.POINTS == 10:
          self.chrono.stop()

class Chrono:
  def __init__(self):
   self.Timer = datetime.combine(date.today(), time(0, 0))
   self.STOP = False

  def stop(self):
      self.STOP = True

  def update(self, dt):
      if self.STOP == False:
        self.Timer += timedelta(milliseconds=dt)
