import pygame, random, sys
from CLASSES import *
from CONSTANTES import *

def AFFICHER_SCORE():
  font = pygame.font.SysFont('Arial', TUILE_TAILLE - 5)
  background = pygame.Surface((LARGEUR, SCORE_HAUTEUR))
  background = background.convert()
  background.fill(BLANC)
  text = font.render(_personnage.chrono.Timer.strftime("%H:%M:%S"), 1, NOIR)
  textpos = text.get_rect(centerx=LARGEUR / 2, centery=SCORE_HAUTEUR / 2)
  background.blit(text, textpos)
  screen.blit(background, (0, 0))

pygame.init()

screen = pygame.display.set_mode([LARGEUR, HAUTEUR])
pygame.display.set_caption('Le jeu du labyrinthe')

XX = 0
YY = 0
with open("Labyrinthe.txt", "r") as fichier:
  for ligne in fichier:
    for sprite in ligne:
      if sprite == 'M':
        _mur = MUR(XX, YY)
        LISTE_MURS.add(_mur)
        LISTE_GLOBALE_SPRITES.add(_mur)
      XX = XX + 1
    XX = 0
    YY = YY + 1

_personnage = None
RECHERCHE_PERSONNAGE = True
while RECHERCHE_PERSONNAGE:
    _personnage = PERSONNAGE()
    LISTE_CONFLIT = pygame.sprite.spritecollide(_personnage, LISTE_MURS, False)
    if len(LISTE_CONFLIT) == 0:
        LISTE_GLOBALE_SPRITES.add(_personnage)
        RECHERCHE_PERSONNAGE = False

while len(LISTE_OBJETS) < 10:
    _objet = OBJET()
    LISTE_CONFLIT = pygame.sprite.spritecollide(_objet, LISTE_GLOBALE_SPRITES, False)
    if len(LISTE_CONFLIT) == 0:
        LISTE_GLOBALE_SPRITES.add(_objet)
        LISTE_OBJETS.add(_objet)

clock = pygame.time.Clock()

print("C'est parti...")

TERMINE = False

while not TERMINE:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      TERMINE = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        _personnage.DIRECTION = 'G'
        break
      elif event.key == pygame.K_RIGHT:
        _personnage.DIRECTION = 'D'
        break
      elif event.key == pygame.K_UP:
        _personnage.DIRECTION = 'H'
        break
      elif event.key == pygame.K_DOWN:
        _personnage.DIRECTION = 'B'
        break

  LISTE_GLOBALE_SPRITES.update()
  screen.fill(BLANC)

  LISTE_GLOBALE_SPRITES.draw(screen)
  AFFICHER_SCORE()

  if _personnage.TERMINE:
    pygame.time.wait(5000)
    TERMINE = True

  pygame.display.flip()
  dt = clock.tick(60)
  _personnage.chrono.update(dt)

print("Nombre d'objets ramassés : %d" % _personnage.POINTS)
pygame.quit()
