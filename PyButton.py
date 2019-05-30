import pygame

class PyButton(pygame.sprite.Sprite):
    def __init__(self, (xPos, yPos, Width, Height), (red, green, blue), text, textSize, (textRed, textGreen, textBlue)):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((Width, Height))
        self.image.fill((red, green, blue))
        self.rect = self.image.get_rect()
        self.rect.center = (xPos, yPos)

        buttonFont = pygame.font.SysFont(None, textSize)
        self.buttonText = buttonFont.render(text, True, (textRed, textGreen, textBlue))
        self.buttonTextRect = self.buttonText.get_rect()
        self.buttonTextRect.center = (xPos, yPos)

        self.pressTimer = 0
        self.pressed = False

    def update(self):
        if (pygame.mouse.get_pressed() == (1, 0, 0)):
            if (self.rect.collidepoint(pygame.mouse.get_pos()) and self.pressTimer <= 0):
                self.pressed = True
                self.pressTimer = 0.4
            elif (self.pressTimer >= 0):
                self.pressTimer -= 0.1
                self.pressed = False

    def DrawText(self, surface):
        surface.blit(self.buttonText, self.buttonTextRect)

    def IsPressed(self):
        return self.pressed


def DrawButtonTexts(buttonGroup, surface):
    for i in buttonGroup:
        i.DrawText(surface)
