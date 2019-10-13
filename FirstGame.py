import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("First Game")

x=50
y=50
width=20
height=40
vel=5
rgb = (0,255,0)
run = True
while run:
	pygame.time.delay(30) #change value for fast/slow movement

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		x-=vel
		if x<0:
			x=0
	if keys[pygame.K_RIGHT]:
		x+=vel
		if x+width>500:
			x=500-width
	if keys[pygame.K_UP]:
		y-=vel
		if y<0:
			y=0
	if keys[pygame.K_DOWN]:
		y+=vel
		if y+height>500:
			y=500-height
	win.fill((0,0,0))
	pygame.draw.rect(win, rgb, (x,y,width,height))
	pygame.display.update()

pygame.quit()