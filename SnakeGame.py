import pygame, time, random
running = True
# Setup
width = 800
height = 800
screen = pygame.display.set_mode((width,height+100))
pygame.display.set_caption('Snake Game')
playerX = height / 2
playerY = width / 2
fruitX = random.randint(0,19) * 40
fruitY = random.randint(0,19) * 40
tailX = [playerX]
tailY = [playerY]
prev2X = 0
prev2Y = 0
prevX = 0
prevY = 0
score = 0
scores = [0]
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
direction = 'STOP'
has_been_reset = False
while running:
    if has_been_reset:
        time.sleep(1)
        direction = 'STOP'
    screen.fill((10,10,10))
    # Draw
    for i in range(len(tailX)):
        if i % 2 == 0:
            pygame.draw.rect(screen, (0, 150, 0), (tailY[i], tailX[i], 40, 40))
        else:
            pygame.draw.rect(screen, (0, 100, 0), (tailY[i], tailX[i], 40, 40))
    pygame.draw.rect(screen, (0, 255, 0), (playerY, playerX, 40, 40))
    pygame.draw.rect(screen, (0, 0, 0), (playerY+5, playerX+5, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (playerY+25, playerX+5, 10, 10))
    # pygame.draw.rect(screen, (255, 255, 255), (playerY+5, playerX+5, 5, 5))
    # pygame.draw.rect(screen, (255, 255, 255), (playerY+25, playerX+5, 5, 5))
    pygame.draw.ellipse(screen, (150, 0, 0), (fruitY, fruitX, 40, 40))
    pygame.draw.ellipse(screen, (255, 0, 0), (fruitY+3, fruitX+3, 30, 30))
    pygame.draw.ellipse(screen, (255, 255, 255), (fruitY+6, fruitX+6, 15, 15))
    pygame.draw.line(screen, (255, 255, 255), (0, 800), (800, 800))
    screen.blit(font.render('SCORE : '+ str(score), True, (255, 255, 255)), (310, 810))
    screen.blit(font.render(f'HIGHEST SCORE : {scores[-1]}', True, (255, 255, 255)), (250, 850))
    # Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not has_been_reset:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if direction != 'DOWN':
                        direction = 'UP'
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if direction != 'UP':
                        direction = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if direction != 'RIGHT':
                        direction = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if direction != 'LEFT':
                        direction = 'RIGHT'
    # Logic
    prevX = tailX[0]
    prevY = tailY[0]
    if direction == 'UP':
        playerX -= 40
    if direction == 'DOWN':
        playerX += 40
    if direction == 'LEFT':
        playerY -= 40
    if direction == 'RIGHT':
        playerY += 40
    tailX[0] = playerX
    tailY[0] = playerY
    if playerX == fruitX and playerY == fruitY:
        fruitX = random.randint(0,19) * 40
        fruitY = random.randint(0,19) * 40
        tailX.append(0)
        tailY.append(0)
        score += 1
    reset = False
    if playerX < 0 or playerY < 0 or playerX > 760 or playerY > 760:
        reset = True
    # if playerX < 0:
    #     playerX = 760
    # if playerX > 760:
    #     playerX = 0
    # if playerY < 0:
    #     playerY = 760
    # if playerY > 760:
    #     playerY = 0
    for i in range(1, len(tailX)):
        prev2X = tailX[i]
        prev2Y = tailY[i]
        tailX[i] = prevX
        tailY[i] = prevY
        prevX = prev2X
        prevY = prev2Y
        if (playerX == tailX[i] and playerY == tailY[i]):
            reset = True
        if (fruitX == tailX[i] and fruitY == tailY[i]):
            fruitX = random.randint(0,19) * 40
            fruitY = random.randint(0,19) * 40
    if has_been_reset:
	    direction = 'STOP'
	    has_been_reset = False
    if reset:
        tailX = [playerX]
        tailY = [playerY]
        scores.append(score)
        scores.sort()
        score = 0
        playerX = height / 2
        playerY = width / 2
        has_been_reset = True
        fruitX = random.randint(0,19) * 40
        fruitY = random.randint(0,19) * 40
    ############---------------------------############
    pygame.display.update()
    time.sleep(0.1)
