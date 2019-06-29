# pygame 1.9.4
def win():
    import pygame, sys, random
    pygame.init()
    pygame.key.set_repeat(10)
    size = width, height = 1680, 1050
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    backround = pygame.image.load("res/alienback.png")

    backrect = backround.get_rect()
    font = pygame.font.SysFont("BankGothic", 45)
    font2 = pygame.font.SysFont("BankGothic", 80)
    font3 = pygame.font.SysFont("BankGothic", 222)
    font4 = pygame.font.SysFont("BankGothic", 15)
    font5 = pygame.font.Font("res/pixelmix_bold.ttf", 85)
    font6 = pygame.font.Font("res/pixelmix_bold.ttf", 222)
    black = [0, 0, 0]
    gray = [55, 55, 55]
    white = [255, 255, 255]
    green = [0, 255, 0]
    orange = [255, 140, 0]
    red = [255, 0, 0]
    gray = [35, 35, 35]
    blue = [0, 0, 255]
    yellow = [255, 255, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    gamep1()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        screen.blit(backround, backrect)
        renderedText = font5.render("Press Enter To Play Again", 1, yellow)
        screen.blit(renderedText, (50, height - 195))
        renderedText = font6.render("You Win!", 1, yellow)
        screen.blit(renderedText, (183, 195))

        pygame.display.flip()
        # pygame.time.wait(2)


def lose():
    import pygame, sys, random
    pygame.init()
    pygame.key.set_repeat(10)
    size = width, height = 1680, 1050
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    backround = pygame.image.load("res/alienback.png")

    backrect = backround.get_rect()
    font = pygame.font.SysFont("BankGothic", 45)
    font2 = pygame.font.SysFont("BankGothic", 80)
    font3 = pygame.font.SysFont("BankGothic", 222)
    font4 = pygame.font.SysFont("BankGothic", 15)
    font5 = pygame.font.Font("res/pixelmix_bold.ttf", 85)
    font6 = pygame.font.Font("res/pixelmix_bold.ttf", 222)
    black = [0, 0, 0]
    gray = [55, 55, 55]
    white = [255, 255, 255]
    green = [0, 255, 0]
    orange = [255, 140, 0]
    red = [255, 0, 0]
    gray = [35, 35, 35]
    blue = [0, 0, 255]
    yellow = [255, 255, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    gamep1()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        screen.blit(backround, backrect)
        renderedText = font5.render("Press Enter to Play Again", 1, yellow)
        screen.blit(renderedText, (45, height - 195))
        renderedText = font6.render("You Lose", 1, yellow)
        screen.blit(renderedText, (166, 195))

        pygame.display.flip()
        # pygame.time.wait(2)


def startscreen():
    aliens = []
    alienSpeed = 7
    import pygame, sys, random
    pygame.init()
    pygame.key.set_repeat(10)
    size = width, height = 1680, 1050
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    backround = pygame.image.load("res/alienback.png")
    alienrect = pygame.image.load("res/alienblur.png")

    # pygame.mixer.music.load('alienstartmusic.wav')
    # pygame.mixer.music.play(-1)

    def addAliens():
        for row in range(0, 5):
            for col in range(0, 15):
                aliens.append(pygame.Rect(10 + col * 75, 10 + row * 75, 50, 50))

    backrect = backround.get_rect()
    font = pygame.font.SysFont("BankGothic", 45)
    font2 = pygame.font.SysFont("BankGothic", 80)
    font3 = pygame.font.SysFont("BankGothic", 222)
    font4 = pygame.font.SysFont("BankGothic", 15)
    font5 = pygame.font.SysFont("BankGothic", 95)
    font6 = pygame.font.SysFont("Bell Gothic Std Black", 111)
    font7 = pygame.font.Font("res/pixelmix_bold.ttf", 99)
    font8 = pygame.font.Font("res/pixelmix_bold.ttf", 150)
    black = [0, 0, 0]
    gray = [55, 55, 55]
    white = [255, 255, 255]
    green = [0, 255, 0]
    orange = [255, 140, 0]
    yellow = [255, 255, 0]
    red = [255, 0, 0]
    gray = [35, 35, 35]
    blue = [0, 0, 255]
    addAliens()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    gamep1()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        # find the smallest left and the largest right in the set
        minleft = width
        maxright = 0
        for alien in aliens:
            if alien.left < minleft:
                minleft = alien.left
            if alien.right > maxright:
                maxright = alien.right

        # If the leftmost or rightmost alien hits the border:
        if maxright > width - 5 or minleft < 5:
            # Reverse direction:
            alienSpeed = -alienSpeed
            # Move every alien down:
            for alien in aliens:
                alien.top = alien.top + 20

        # move them left or right
        for alien in aliens:
            alien.left = alien.left + alienSpeed

        screen.blit(backround, backrect)
        for alien in aliens:
            screen.blit(alienrect, alien)
        renderedText = font7.render("Press Space to Start", 1, yellow)
        screen.blit(renderedText, (93, height - 195))
        renderedText = font8.render("Space Invaders", 1, yellow)
        screen.blit(renderedText, (43, 95))
        pygame.display.flip()
        # pygame.time.wait(2)


xpls = []


class Xplosan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 3

    def update(self):
        self.timer = self.timer - 1
        if self.timer <= 0:
            xpls.remove(self)
            del self


bxpls = []


class bXplosan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 3

    def update(self):
        self.timer = self.timer - 1
        if self.timer <= 0:
            bxpls.remove(self)
            del self


def gamep1():
    import pygame, sys, random
    pygame.init()
    pygame.key.set_repeat(10)

    size = width, height = 1680, 1050
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption('Space Invaders')
    backround = pygame.image.load("res/alienback.png")
    playerect = pygame.image.load("res/alienship2.png")
    alienrect = pygame.image.load("res/alienalien.png")
    bullet_img = pygame.image.load("res/alienbullet.png")
    bulletrect = bullet_img.get_rect()
    bombrect = pygame.image.load("res/alienbomb.png")
    xploderect = pygame.image.load("res/xplosan.png")
    bxploderect = pygame.image.load("res/bxplosan.png")
    backrect = backround.get_rect()
    player = pygame.Rect(width / 2, 911, 52, 135)

    # pygame.mixer.music.load('alienmusic.wav')
    # pygame.mixer.music.play(-1)
    # hitsnd = pygame.mixer.Sound('alienhit.wav')
    # shootsnd = pygame.mixer.Sound('alienpew.wav')

    canshoot = 0

    black = [0, 0, 0]
    white = [255, 255, 255]
    green = [0, 255, 0]
    orange = [255, 140, 0]
    red = [255, 0, 0]
    gray = [35, 35, 35]
    blue = [0, 0, 255]

    bullets = []
    aliens = []
    bombs = []
    shelters = []
    lives = 10
    alienSpeed = 17

    def addAliens():
        for row in range(0, 5):
            for col in range(0, 15):
                aliens.append(pygame.Rect(10 + col * 75, 10 + row * 75, 50, 50))

    def addShelters():
        siz = 30
        sep = 420
        lft = (width - 3 * sep - 6 * siz) / 2  # center the shelters on the screen
        for row in range(0, 4):
            for col in range(0, 6):
                for num in range(0, 4):
                    bit = pygame.Rect(lft + sep * num + col * siz, height - 200 - row * siz, siz, siz)
                    if row == 3 and (col == 0 or col == 5):
                        bit.top = bit.top + 400
                    shelters.append(bit)

    addShelters();
    addAliens()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.left = player.left - 25
            if keys[pygame.K_RIGHT]:
                player.right = player.right + 25
            if keys[pygame.K_SPACE] and len(bullets) <= 5 and canshoot == 0:
                bullets.append([player.centerx - 12, player.top])
                canshoot = 5
                # shootsnd.play(0)
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
        if canshoot > 0:
            canshoot = canshoot - 1
        # find the smallest left and the largest right in the set
        minleft = width
        maxright = 0
        for alien in aliens:
            if alien.left < minleft:
                minleft = alien.left
            if alien.right > maxright:
                maxright = alien.right

        # If the leftmost or rightmost alien hits the border:
        if maxright > width - 5 or minleft < 5:
            # Reverse direction:
            alienSpeed = -alienSpeed
            # Move every alien down:
            for alien in aliens:
                alien.top = alien.top + 20
                if alien.bottom > player.top:
                    lose()

        # move them left or right
        for alien in aliens:
            alien.left = alien.left + alienSpeed

        for bullet in bullets:
            bullet[1] = bullet[1] - 22
            if bullet[1] < 0:
                bullets.remove(bullet)

        for bomb in bombs:
            bomb[1] = bomb[1] + 20
            if bomb[1] < 0:
                bombs.remove(bomb)

        #### Check if bullets hit aliens ####
        for bullet in bullets:
            for alien in aliens:
                if alien.collidepoint(bullet):
                    aliens.remove(alien)
                    bullets.remove(bullet)
                    bxpls.append(bXplosan(bullet[0], bullet[1]))

        #### Check if bombs hit shelters ####
        for bomb in bombs:
            for bit in shelters:
                if bit.collidepoint(bomb):
                    shelters.remove(bit)
                    bombs.remove(bomb)
                    xpls.append(Xplosan(bomb[0], bomb[1]))
                    break
        for xpl in xpls:
            xpl.update()

        for bxpl in bxpls:
            bxpl.update()
        #### Check if bullets hit shelters ####
        for bullet in bullets:
            for bit in shelters:
                bulletrect.x = bullet[0]
                bulletrect.y = bullet[1]
                if bit.colliderect(bulletrect):
                    shelters.remove(bit)
                    bullets.remove(bullet)
                    bxpls.append(bXplosan(bullet[0], bullet[1]))
                    break

        #### Check if bombs hit player ####
        for bomb in bombs:
            if player.collidepoint(bomb):
                lives = lives - 1
                bombs.remove(bomb)
                xpls.append(Xplosan(bomb[0], bomb[1]))
                # hitsnd.play(0)

                break

        if lives == 0:
            lose()
        if lives == 3:
            green = [255, 0, 0]
        if lives == 6:
            green = [255, 255, 0]

        if len(aliens) == 0:
            win()

        # drop bombs
        for alien in aliens:
            if random.randint(0, 150) == 0:
                bombs.append([alien.centerx, alien.bottom])

        screen.blit(backround, backrect)
        # draw your game elements here:
        screen.blit(playerect, player)
        for alien in aliens:
            screen.blit(alienrect, alien)

        for bit in shelters:
            pygame.draw.rect(screen, gray, bit, 0)

        for bomb in bombs:
            screen.blit(bombrect, bomb)

        for bullet in bullets:
            screen.blit(bullet_img, bullet)

        for x in range(0, lives):
            rct = pygame.Rect(10 + x * 40, height - 25, 35, 25)
            pygame.draw.rect(screen, green, rct, 0)
        for xpl in xpls:
            screen.blit(xploderect, (xpl.x, xpl.y))
        for bxpl in bxpls:
            screen.blit(bxploderect, (bxpl.x - 5, bxpl.y))
        pygame.display.flip()
        # pygame.time.wait(30)


startscreen()
