import pygame

LARGEUR, HAUTEUR = 640, 480
BALLE_LARGEUR, BALLE_HAUTEUR = 16, 16
BRIQUE_LARGEUR, BRIQUE_HAUTEUR = 64, 16
RAQUETTE_LARGEUR, RAQUETTE_HAUTEUR = 64, 16
RAQUETTE_VITESSE = 20
BALLE_VITESSE = 2


class OBJET(pygame.sprite.Sprite):

    def __init__(self, IMAGE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMAGE).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()


class RAQUETTE(OBJET):

    def __init__(self, IMAGE):
        OBJET.__init__(self, IMAGE)
        self.rect.bottom = HAUTEUR
        self.rect.left = (LARGEUR - self.image.get_width()) / 2

    def DéplacerGauche(self):
        if self.rect.left > 0:
            self.rect.move_ip(-RAQUETTE_VITESSE, 0)

    def DéplacerDroite(self):
        if self.rect.right < LARGEUR:
            self.rect.move_ip(RAQUETTE_VITESSE, 0)


class BRIQUE(OBJET):

    def __init__(self, IMAGE, x, y):
        OBJET.__init__(self, IMAGE)
        self.rect.x, self.rect.y = x, y


class BALLE(OBJET):

    def __init__(self, IMAGE, VITESSE_X, VITESSE_Y):
        OBJET.__init__(self, IMAGE)
        self.rect.bottom = HAUTEUR - RAQUETTE_LARGEUR
        self.rect.left = HAUTEUR / 2
        self.VITESSE_X = VITESSE_X
        self.VITESSE_Y = VITESSE_Y

    def update(self):
        self.rect = self.rect.move(self.VITESSE_X, self.VITESSE_Y)

        if self.rect.x > LARGEUR - self.image.get_width() or self.rect.x < 0:
            self.VITESSE_X *= -1
        if self.rect.y < 0:
            self.VITESSE_Y *= -1