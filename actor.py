
import  pygame
from PIL import Image

class jugador(pygame.sprite.Sprite):
    def __init__(self,x,y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        self.rect = pygame.Rect(x, y, 32, 32)

    def mover(self, px, py): # * los movimientos activos para el jugar, en este caso la serpiente

        if px != 0:
            self.mover_on_axis(px, 0)
        if py != 0:
            self.mover_on_axis(0, py)

    def mover_on_axis(self, px, py):
        self.rect.x += px
        self.rect.y += py


        for pared in paredes: # * colisiones de las paredes
            if pygame.sprite.collide_rect(self, pared):   
                if px > 0:
                     self.rect.right = pared.rect.left
                if px < 0:
                    self.rect.left = pared.rect.right
                if py > 0:
                    self.rect.bottom = pared.rect.top                        
                if py < 0:
                    self.rect.top = pared.rect.bottom

class pared (pygame.sprite.Sprite):
    def __init__(self, wx):
        super().__init__()
        all_Sprite_List.add(self)
        pared.add(self)
        self.image = pygame.Surface((32,32))
        self.rect = pygame.Rect(wx[0], wx[1], 32, 32)

class area (pygame.sprite.Sprite):
    def __init__(self, wx):
        super().__init__()
        all_Sprite_List.add(self)
        area.add(self)
        self.image = pygame.Surface((32,32))
        self.rect = pygame.Rect(wx[0], wx[1], 32, 32)

class meta (pygame.sprite.Sprite):
    def __init__(self, wx):
        super().__init__()
        all_Sprite_List.add(self)
        meta.add(self)
        self.image = pygame.Surface((32,32))
        self.rect = pygame.Rect(wx[0], wx[1], 32, 32)

pared = Image.open('pared.png','r')      # imagen en color 
jugador = Image.open('serpiente.png','r')
area = Image.open('area.png', 'r')
meta = Image.open('meta.png', 'r')
