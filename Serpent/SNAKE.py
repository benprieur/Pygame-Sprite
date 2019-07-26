import pygame, random, sys

pygame.mixer.init()

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

TUILE_TAILLE = 32
TUILE_NOMBRE = 15
SCORE_HAUTEUR = 32

LARGEUR = TUILE_TAILLE * TUILE_NOMBRE
HAUTEUR = TUILE_TAILLE * TUILE_NOMBRE + SCORE_HAUTEUR

POINT_UNITE = 1
DUREE_NOURRITURE_DISPARITION = 5500

# CLASSE SERPENT
class SERPENT(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.SON_NOURRITURE = pygame.mixer.Sound('NOURRITURE.wav')
    self.SON_NOURRITURE.set_volume(1.0)

    self.TETE = pygame.image.load("TETE.png").convert_alpha()
    self.image = self.TETE

    self.rect = self.image.get_rect()
    self.rect.y = (TUILE_NOMBRE / 2) * TUILE_TAILLE
    self.rect.x = (TUILE_NOMBRE / 2) * TUILE_TAILLE

    self.POINTS = 0
    self.DIRECTION = 'G'
    self.TERMINE = False

  def AJOUTER_NOUVEAU_CORPS(self):
    nouveau_corps = CORPS(self.rect.x, self.rect.y)
    LISTE_SERPENT.add(nouveau_corps)
    LISTE_GLOBALE_SPRITES.add(nouveau_corps)

  def update(self):
    COORD_COURANTE_X = self.rect.x
    COORD_COURANTE_Y = self.rect.y

    if self.DIRECTION == 'G':
      self.image = pygame.transform.rotate(self.TETE, 90)
      self.rect.x -= TUILE_TAILLE
    elif self.DIRECTION == 'D':
      self.image = pygame.transform.rotate(self.TETE, -90)
      self.rect.x += TUILE_TAILLE
    elif self.DIRECTION == 'H':
      self.image = pygame.transform.rotate(self.TETE, 0)
      self.rect.y -= TUILE_TAILLE
    elif self.DIRECTION == 'B':
      self.image = pygame.transform.rotate(self.TETE, 180)
      self.rect.y += TUILE_TAILLE

    for ELT in LISTE_SERPENT:
      x = ELT.GET_X()
      y = ELT.GET_Y()
      ELT.set_xy(COORD_COURANTE_X, COORD_COURANTE_Y)
      COORD_COURANTE_X = x
      COORD_COURANTE_Y = y

    if self.rect.x >= LARGEUR:
      self.rect.x = 0
    elif self.rect.x < 0:
      self.rect.x = LARGEUR - TUILE_TAILLE
    elif self.rect.y >= HAUTEUR:
      self.rect.y = SCORE_HAUTEUR
    elif self.rect.y < SCORE_HAUTEUR:
      self.rect.y = HAUTEUR - SCORE_HAUTEUR

    LISTE_COLLISION_SERPENT = pygame.sprite.spritecollide(self, LISTE_SERPENT, False)
    if len(LISTE_COLLISION_SERPENT):
      print("Perdu")
      self.TERMINE = True

    LISTE_COLLISION_NOURRITURE = pygame.sprite.spritecollide(self, LISTE_NOURRITURE, False)
    for nourriture in LISTE_COLLISION_NOURRITURE:
      nourriture.kill()
      self.AJOUTER_NOUVEAU_CORPS()
      self.SON_NOURRITURE.play()
      self.POINTS += POINT_UNITE


# CLASSE CORPS
class CORPS(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load("CORPS.png").convert_alpha()

    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

  def GET_X(self):
    return self.rect.x

  def GET_Y(self):
    return self.rect.y

  def set_xy(self, x, y):
    self.rect.x = x
    self.rect.y = y

# CLASSE NOURRITURE
class NOURRITURE(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load("NOURRITURE.png").convert_alpha()

    self.rect = self.image.get_rect()
    self.rect.y = random.randint(0, TUILE_NOMBRE - 1) * TUILE_TAILLE + SCORE_HAUTEUR
    self.rect.x = random.randint(0, TUILE_NOMBRE - 1) * TUILE_TAILLE

    self.time = pygame.time.get_ticks()

  def update(self):
    if pygame.time.get_ticks() - self.time > DUREE_NOURRITURE_DISPARITION:
      self.kill()

# AFFICHER_SCORE
def AFFICHER_SCORE():
  font = pygame.font.SysFont('Arial', TUILE_TAILLE - 5)
  background = pygame.Surface((LARGEUR, SCORE_HAUTEUR))
  background = background.convert()
  background.fill(BLANC)
  text = font.render("Points = %d" % _serpent.POINTS, 1, NOIR)
  textpos = text.get_rect(centerx=LARGEUR / 2, centery=SCORE_HAUTEUR / 2)
  background.blit(text, textpos)
  screen.blit(background, (0, 0))

pygame.init()

screen = pygame.display.set_mode([LARGEUR, HAUTEUR])
pygame.display.set_caption('Le jeu du serpent')

LISTE_SERPENT = pygame.sprite.Group()
LISTE_NOURRITURE = pygame.sprite.Group()
LISTE_GLOBALE_SPRITES = pygame.sprite.Group()

SON_NOURRITURE = pygame.mixer.Sound('NOURRITURE.wav')
SON_NOURRITURE.set_volume(1.0)

SON_PERDU = pygame.mixer.Sound('PERDU.wav')
SON_PERDU.set_volume(1.0)

_serpent = SERPENT()
LISTE_GLOBALE_SPRITES.add(_serpent)

clock = pygame.time.Clock()

print("C'est parti...")

TERMINE = False

while not TERMINE:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      TERMINE = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT and _serpent.DIRECTION != 'D':
        _serpent.DIRECTION = 'G'
        break
      elif event.key == pygame.K_RIGHT and _serpent.DIRECTION != 'G':
        _serpent.DIRECTION = 'D'
        break
      elif event.key == pygame.K_UP and _serpent.DIRECTION != 'B':
        _serpent.DIRECTION = 'H'
        break
      elif event.key == pygame.K_DOWN and _serpent.DIRECTION != 'H':
        _serpent.DIRECTION = 'B'
        break

  if random.randint(0, 18) == 0:
    _nourriture = NOURRITURE()

    LISTE_CONFLIT = pygame.sprite.spritecollide(_nourriture, LISTE_GLOBALE_SPRITES, False)
    if len(LISTE_CONFLIT) == 0:
      SON_NOURRITURE.play()
      LISTE_GLOBALE_SPRITES.add(_nourriture)
      LISTE_NOURRITURE.add(_nourriture)

  LISTE_GLOBALE_SPRITES.update()
  screen.fill(BLANC)

  LISTE_GLOBALE_SPRITES.draw(screen)
  AFFICHER_SCORE()

  if _serpent.TERMINE:
    SON_PERDU.play()
    pygame.time.wait(5000)
    TERMINE = True

  pygame.display.flip()
  clock.tick(7)

print("Votre score : %d points" % _serpent.POINTS)
pygame.quit()
