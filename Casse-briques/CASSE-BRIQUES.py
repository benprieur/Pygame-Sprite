from CLASSES import *
import pygame, sys
pygame.init()

FENETRE = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.key.set_repeat(400, 30)
pygame.display.set_caption('Jeu du casse-briques')
clock = pygame.time.Clock()
score = 0

LISTE_GLOBALE_SPRITES = pygame.sprite.Group()
LISTE_RAQUETTE_BRIQUES = pygame.sprite.Group()
LISTE_BRIQUES = pygame.sprite.Group()

balle = BALLE('BALLE.png', BALLE_VITESSE, -BALLE_VITESSE)
LISTE_GLOBALE_SPRITES.add(balle)

raquette = RAQUETTE('RAQUETTE.png')
LISTE_GLOBALE_SPRITES.add(raquette)
LISTE_RAQUETTE_BRIQUES.add(raquette)

for i in range(8):
    for j in range(8):
        brique = BRIQUE('BRIQUE.png', (i+1)*BRIQUE_LARGEUR + 5, (j+3)*BRIQUE_HAUTEUR + 5)
        LISTE_GLOBALE_SPRITES.add(brique)
        LISTE_RAQUETTE_BRIQUES.add(brique)
        LISTE_BRIQUES.add(brique)

while True:
    if balle.rect.y > HAUTEUR:
        print ("Perdu :)")
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                raquette.DéplacerGauche()
            elif event.key == pygame.K_RIGHT:
                raquette.DéplacerDroite()

    REBONDS = pygame.sprite.spritecollide(balle, LISTE_RAQUETTE_BRIQUES, False)
    if REBONDS:
        RECT = REBONDS[0].rect
        if RECT.left > balle.rect.left or balle.rect.right < RECT.right:
            balle.VITESSE_Y *= -1
        else:
            balle.VITESSE_X *= -1

        if pygame.sprite.spritecollide(balle, LISTE_BRIQUES, True):
            score += len(REBONDS)
            print( "%s points" % score)

        if len(LISTE_BRIQUES) == 0:
          print("Gagné, bravo :)")
          pygame.quit()
          sys.exit()

    FENETRE.fill((0, 0, 0))
    LISTE_GLOBALE_SPRITES.draw(FENETRE)

    LISTE_GLOBALE_SPRITES.update()
    clock.tick(60)
    pygame.display.flip()