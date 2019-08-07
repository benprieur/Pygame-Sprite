import pygame
from CLASSES import *
pygame.init()

def AFFICHER_SCORE():
  texte = FONT.render(str(_SCORE) + " points", 1, (255, 0, 0))
  textpos = texte.get_rect(centerx=LARGEUR_FENETRE / 2, centery=50)
  ECRAN.blit(texte, textpos)

ECRAN = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption("FUSEE PLANETES - CH 7")
FONT = pygame.font.Font(None, 24)
_SCORE = 0

fusee = FUSEE()
LISTE_GLOBALE_SPRITES.add(fusee)

planete_gauche = PLANETE(XX_PLANETE, YY_PLANETE)
LISTE_PLANETES.add(planete_gauche)
LISTE_GLOBALE_SPRITES.add(planete_gauche)

planete_droite = PLANETE(XX_PLANETE + XX_ENTRE_PLANETES,
                         YY_PLANETE + YY_ENTRE_PLANETE)
LISTE_PLANETES.add(planete_droite)
LISTE_GLOBALE_SPRITES.add(planete_droite)

clock = pygame.time.Clock()
print("C'est parti...")

while not ARRET_JEU:

  LISTE_CONFLIT = pygame.sprite.spritecollide(fusee, LISTE_PLANETES, False)
  if len(LISTE_CONFLIT) > 0:
    ARRET_JEU = True
    print("C'est perdu")
    pygame.time.wait(5000)

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      ARRET_JEU = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          fusee.DIRECTION = 'D'
    elif event.type == pygame.KEYUP:
      fusee.DIRECTION = 'G'

  if len(LISTE_PLANETES) == 0:

     XX_PLANETE = randint(30, 130)
     planete_gauche = PLANETE(XX_PLANETE, YY_PLANETE)
     LISTE_PLANETES.add(planete_gauche)
     LISTE_GLOBALE_SPRITES.add(planete_gauche)

     planete_droite = PLANETE(XX_PLANETE + XX_ENTRE_PLANETES, YY_PLANETE + YY_ENTRE_PLANETE)
     LISTE_PLANETES.add(planete_droite)
     LISTE_GLOBALE_SPRITES.add(planete_droite)

     _SCORE = _SCORE + 1

  LISTE_GLOBALE_SPRITES.update()
  ECRAN.fill(COULEUR_FOND)
  LISTE_GLOBALE_SPRITES.draw(ECRAN)
  print(_SCORE)
  AFFICHER_SCORE()
  pygame.display.flip()

