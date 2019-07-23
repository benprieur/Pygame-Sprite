import sys, pygame

COULEUR_ROUGE = 255, 0, 0
COULEUR_BLEUE = 0, 0, 255

# ----------------
#
# class CARRE
#
# ----------------
class CARRE(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.fill(COULEUR_ROUGE)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

        self.DEPLACEMENT = 3

    def update(self):
        self.rect.x += self.DEPLACEMENT

        if  self.rect.x >= 320:
            self.rect.x = 320
            self.DEPLACEMENT = -3
        elif  self.rect.x <= 0:
            self.rect.x = 0
            self.DEPLACEMENT = 3

# ----------------
#
# Code
#
# ----------------
pygame.init()
screen = pygame.display.set_mode((400, 400))
background = pygame.Surface(screen.get_size())
background.fill(COULEUR_BLEUE)
screen.blit(background, (0, 0))

pygame.display.set_caption("Le carré qui rebondit")

clock = pygame.time.Clock()

XX = 300
DEPLACEMENT = 3

all_sprites = pygame.sprite.Group()
carre = CARRE()
all_sprites.add(carre)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    all_sprites.clear(screen, background)
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
