import pygame

pygame.init()
screenW = 1024
screenH = 512
window = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Tower Defence")

amount_of_arrows = 3000
heroShot = amount_of_arrows*[pygame.image.load("hero\\s1.png"),pygame.image.load("hero\\s2.png"),
            pygame.image.load('hero\\s3.png'),pygame.image.load("hero\\s4.png")]
stand = pygame.image.load("hero\\st.png")

h2A = 30*[pygame.image.load("hero2\\atack\\attack1.png"),pygame.image.load("hero2\\atack\\attack2.png"),
       pygame.image.load("hero2\\atack\\attack3.png"),pygame.image.load("hero2\\atack\\attack4.png"),
       pygame.image.load("hero2\\atack\\attack5.png")]

h2W = 30*[pygame.image.load("hero2\\walk\\R1.png"),pygame.image.load("hero2\\walk\\R2.png"),
       pygame.image.load("hero2\\walk\\R3.png"),pygame.image.load("hero2\\walk\\R4.png"),
       pygame.image.load("hero2\\walk\\R4.png"),pygame.image.load("hero2\\walk\\R6.png")]
hPunch = pygame.image.load("punch.png")
arrow = pygame.image.load("bullet.png")
bg = pygame.image.load("bgcas.png")
score = 0
n = 0
R = 512


class player(object):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed =  30
        self.shot = False
        self.shotCount = 0
        self.left = False
        self.right = False
        self.walkCount = 0
        self.hit = False
        self.hitCount = 0
        self.hitbox = (self.x + 45, self.y + 11, 70, 130)
        self.health = 20



    def draw(self,window):
        if self.shotCount+1 >= 16:
            self.shotCount = 0
            
        if self.shot:
            window.blit(heroShot[int(self.shotCount//4)], (self.x,self.y))          
            self.shotCount += 1
        else:
            window.blit(stand, (self.x,self.y))

        pygame.draw.rect(window,(250,0,0),(self.hitbox[0], self.hitbox[1]-35, 50, 15))#RED BACKGROUND OF HEALTH BAR
        pygame.draw.rect(window,(0,255,0),(self.hitbox[0], self.hitbox[1]-35, 50 - ((50/10) * (10 - self.health)), 15))

        self.hitbox = (self.x + 15, self.y + 11, 35, 105)
        #pygame.draw.rect(window,(255,0,0),self.hitbox,2)

        
    def draw2(self, window):
        if self.walkCount+1 >= 36:
            self.walkCount = 0

        if self.hitCount +1 >= 20:
            self.hitCount = 0
        if self.left:
            window.blit(h2W[self.walkCount//4],(self.x,self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(h2W[self.walkCount//4],(self.x,self.y))
            self.walkCount += 1        
        elif self.hit:
            window.blit(h2A[int(self.hitCount//5)], (self.x,self.y))
            self.hitCount += 0.5
        else:
            window.blit(stand, (self.x,self.y))

        pygame.draw.rect(window,(250,0,0),(self.hitbox[0], self.hitbox[1]-35, 50, 15))#RED BACKGROUND OF HEALTH BAR
        pygame.draw.rect(window,(0,255,0),(self.hitbox[0], self.hitbox[1]-35, 50 - ((50/10) * (10 - self.health)), 15))

        self.hitbox = (self.x + 15, self.y + 11, 35, 105)
        #pygame.draw.rect(window,(255,0,0),self.hitbox,2)


        

class projectile(object):
    def __init__(self,x,y,radius,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,window):
        window.blit(arrow, (self.x,self.y))
    def draw2(self,window):
        window.blit(hPunch, (self.x, self.y))



clock = pygame.time.Clock()

#_______________________ENEMY_____________________________________________________#
class enemy():
        walkRight = [pygame.image.load('enemy\\R1E.png'),pygame.image.load('enemy\\R2E.png'),
pygame.image.load('enemy\\R3E.png'),pygame.image.load('enemy\\R4E.png'),pygame.image.load('enemy\\R5E.png'),
pygame.image.load('enemy\\R6E.png'),pygame.image.load('enemy\\R7E.png'),pygame.image.load('enemy\\R8E.png'),
pygame.image.load('enemy\\R9E.png'),pygame.image.load('enemy\\R10E.png')]
        walkLeft = [pygame.image.load('enemy\\L1E.png'),pygame.image.load('enemy\\L2E.png'),
pygame.image.load('enemy\\L3E.png'),pygame.image.load('enemy\\L4E.png'),pygame.image.load('enemy\\L5E.png'),
pygame.image.load('enemy\\L6E.png'),pygame.image.load('enemy\\L7E.png'),pygame.image.load('enemy\\L8E.png'),
pygame.image.load('enemy\\L9E.png'),pygame.image.load('enemy\\L10E.png')]

        def __init__(self, x, y, width, height, end):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.end = end
                self.path = [self.end, self.x]
                self.walkCount = 0
                self.vel = 1.5
                self.hitbox = (self.x + 45, self.y + 11, 35, 105)

                self.health = 20
                self.visible = True

        def draw(self,win):
                self.move()
                if self.visible:
                        if self.walkCount + 1 >= 40:
                                self.walkCount = 0

                        if self.vel > 0:
                                win.blit(self.walkRight[self.walkCount //4], (self.x, self.y))
                                self.walkCount += 1
                        else:
                                win.blit(self.walkLeft[self.walkCount //4], (self.x, self.y))
                                self.walkCount += 1 


                        pygame.draw.rect(win,(250,0,0),(self.hitbox[0], self.hitbox[1]-35, 50, 15))#RED BACKGROUND OF HEALTH BAR
                        pygame.draw.rect(win,(0,0,255),(self.hitbox[0], self.hitbox[1]-35, 50 - ((50/10) * (10 - self.health)), 15))

                        self.hitbox = (self.x + 20, self.y + 11, 35, 105)
                       # pygame.draw.rect(win,(255,0,0),self.hitbox,2)

        def move(self):
                if self.vel > 0:
                        if self.x + self.vel < self.path[1]:
                                self.x += self.vel
                        else:
                                self.vel = self.vel * -1
                                self.walkCount = 0
                else:
                        if self.x - self.vel > self.path[0]:
                                self.x += self.vel
        def hit(self):
                if self.health > 0:
                        self.health -= 1
                else:
                        self.y = -300
                        global score
                        global n
                        global R
                        score += 1
                        if n < 10:
                            n += 1
                        else:
                            n = R
                            
                print("Super HIT")
#################################################################################################################

def redrawGameWindow():
    window.blit(bg, (0,0))
    hero2.draw2(window)
    hero.draw(window)
    zombie0.draw(window)
    zombie1.draw(window)
    zombie2.draw(window)
    zombie3.draw(window)
    zombie4.draw(window)
    zombie5.draw(window)
    zombie6.draw(window)
    zombie7.draw(window)
    zombie8.draw(window)
    zombie9.draw(window)
    zombie10.draw(window)


    for bullet in bullets:
        bullet.draw(window)
    for punch in punches:
        punch.draw2(window)
    text = font.render("Score: " + str(score), 1, (255,255,255))
    window.blit(text, (700,10))
    pygame.display.update()


hero = player(200, 160, 120, 135)
hero2 = player(200, 370, 120, 135)
zombie0 = enemy(600, 370, 95, 150, 300)
zombie1 = enemy(725, 370, 95, 150, 300)
zombie2 = enemy(650, 370, 95, 150, 300)
zombie3 = enemy(700, 370, 95, 150, 300)
zombie4 = enemy(750, 370, 95, 150, 300)
zombie5 = enemy(800, 370, 95, 150, 300)
zombie6 = enemy(725, 370, 95, 150, 300)
zombie7 = enemy(650, 180, 95, 150, 300)
zombie8 = enemy(700, 180, 95, 150, 300)
zombie9 = enemy(750, 180, 95, 150, 300)
zombie10 = enemy(750, 180, 95, 150, 300)

zombies = [zombie0,zombie1,zombie2,zombie3,zombie4,zombie5,zombie6,zombie7,zombie8,zombie9,zombie10]
bullets = []
punches = []
run = True
while run:
    clock.tick(88)
    font = pygame.font.SysFont("comicsans", 30,True, True)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    for bullet in bullets:

        if bullet.x < 900:
            bullet.x += bullet.vel
        elif bullet.x >= 900:
            bullets.pop(bullets.index(bullet))
    if n != R:
        for bull in bullets:
                    if bull.y - bull.radius < zombies[n].hitbox[1] + zombies[n].hitbox[3] and bull.y + bull.radius > zombies[n].hitbox[1]:
                            if bull.x + bull.radius > zombies[n].hitbox[0] and bull.x - bull.radius < zombies[n].hitbox[0] + zombies[n].hitbox[2]: #Bullet should disappear if it is outside this interval 
                                zombies[n].hit()
                                bullets.pop(bullets.index(bull))
            
            
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        hero.shot = True
        while len(bullets) < 2:
            bullets.append(projectile(round(hero.x + hero.width //2), round(hero.y + hero.height//2 - 27), 5, 1))
    else:
        hero.shot = False



    for punch in punches:
        if punch.x < hero2.x + 3.8:
            punch.x += punch.vel
        elif punch.x >= hero2.x + 5:
            punches.pop(punches.index(punch))
    if n != R:
        for punch in punches:
                    if punch.y - punch.radius < zombies[n].hitbox[1] + zombies[n].hitbox[3] and punch.y + punch.radius > zombies[n].hitbox[1]:
                            if punch.x + punch.radius > zombies[n].hitbox[0] and punch.x - punch.radius < zombies[n].hitbox[0] + zombies[n].hitbox[2]: #Bullet should disappear if it is outside this interval 
                                zombies[n].hit()
                                punches.pop(punches.index(punch))

    if keys[pygame.K_p]:
        hero2.hit = True
        while len(punches) <= 1:
            punches.append(projectile(round(hero2.x + hero2.width //2), round(hero2.y + hero2.height//2 - 27), 1, 1))
    else:
        hero2.hit = False

    if keys[pygame.K_LEFT] and hero2.x > 250:
        hero2.left = True
        hero2.right = False
        hero2.x -= hero2.speed
    elif keys[pygame.K_RIGHT] and hero2.x < screenW - hero2.width - hero2.speed:
        hero2.right = True
        hero2.left = False
        hero2.x += hero2.speed
    else:
        hero2.left = False
        hero2.right = False
    redrawGameWindow()        
pygame.quit()

t = open("Scores.txt","a")
t.write(str(score)+"\n")
t.close()
