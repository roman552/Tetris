#tetris
import pygame
pygame.init()

WHITE=(255,255,255)

W=300
H=500

clock=pygame.time.Clock()
FPS=15

sc=pygame.display.set_mode((W,H))
sc.fill(WHITE)

pygame.display.set_caption('TETRIS')

icon=pygame.image.load('C:/Users/A/Desktop/tetris/Tetris-icon.png')
pygame.display.set_icon(icon)

red_s=0
green_s=0
blue_s=0

f=0

Red_Brick=pygame.image.load('C:/Users/A/Desktop/tetris/red_brick.png')
red_scale=pygame.transform.scale(Red_Brick,(Red_Brick.get_width()//2,Red_Brick.get_height()//2))
red_x=125
red_y=0

Green_Brick=pygame.image.load('C:/Users/A/Desktop/tetris/green_brick.png')
green_scale=pygame.transform.scale(Green_Brick,(Green_Brick.get_width()//2,Green_Brick.get_height()//2))
green_x=125
green_y=0

Blue_Brick=pygame.image.load('C:/Users/A/Desktop/tetris/blue_brick.png')
blue_scale=pygame.transform.scale(Blue_Brick,(Blue_Brick.get_width()//2,Blue_Brick.get_height()//2))
blue_x=125
blue_y=0

class RedBrick(pygame.sprite.Sprite):
	def __init__(self,x,scale,y,group):
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.scale = scale
		self.scale_rect = self.scale.get_rect(center=(x, y))
		self.group=group

class GreenBrick(pygame.sprite.Sprite):
	def __init__(self,x,scale,y,group):
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.scale = scale
		self.scale_rect = self.scale.get_rect(center=(x, y))
		self.group=group

class BlueBrick(pygame.sprite.Sprite):
	def __init__(self,x,scale,y,group):
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.scale = scale
		self.scale_rect = self.scale.get_rect(center=(x, y))
		self.group=group

red=pygame.sprite.Group() 
green=pygame.sprite.Group()
blue=pygame.sprite.Group()

red_brick=RedBrick(red_x,red_scale,red_y,red) 
red_brick2=RedBrick(red_x+25,red_scale,red_y,red)
red_brick3=RedBrick(red_x+50,red_scale,red_y,red)
red_brick4=RedBrick(red_x+75,red_scale,red_y,red)

red.add(red_brick,red_brick2,red_brick3,red_brick4)

green_brick=GreenBrick(green_x,green_scale,green_y,green) 
green_brick2=GreenBrick(green_x,green_scale,green_y+25,green)
green_brick3=GreenBrick(green_x,green_scale,green_y+50,green)
green_brick4=GreenBrick(green_x+25,green_scale,green_y+50,green)

green.add(green_brick,green_brick2,green_brick3,green_brick4)

blue_brick=BlueBrick(blue_x,blue_scale,blue_y,blue) 
blue_brick2=BlueBrick(blue_x,blue_scale,blue_y+25,blue)
blue_brick3=BlueBrick(blue_x+25,blue_scale,blue_y,blue)
blue_brick4=BlueBrick(blue_x+25,blue_scale,blue_y+25,blue)

blue.add(blue_brick,blue_brick2,blue_brick3,blue_brick4)

pygame.display.update()

red1_move=0
red2_move=0
red3_move=0


green1_move=0
green2_move=0
green3_move=0


blue1_move=0
blue2_move=0
blue3_move=0

while 1:
	sc.fill(WHITE)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			break
		if event.type==pygame.KEYDOWN:
			if f==0:
				if event.key==pygame.K_f and red_s==0 and red_brick4.scale_rect.y<475:
					red_brick.scale_rect.y-=25
					red_brick2.scale_rect.x-=25
					red_brick3.scale_rect.x-=50
					red_brick3.scale_rect.y+=25
					red_brick4.scale_rect.x-=75
					red_brick4.scale_rect.y+=50
					red_s=1
				elif event.key==pygame.K_f and red_s==1 and red_brick4.scale_rect.y<475:
					red_brick.scale_rect.y+=25
					red_brick2.scale_rect.x+=25
					red_brick3.scale_rect.x+=50
					red_brick3.scale_rect.y-=25
					red_brick4.scale_rect.x+=75
					red_brick4.scale_rect.y-=50
					red_s=0

			elif f==1:
				if event.key==pygame.K_f and green_s==0 and green_brick4.scale_rect.y<475:
					green_brick.scale_rect.y+=25
					green_brick2.scale_rect.x+=25
					green_brick3.scale_rect.x+=50
					green_brick3.scale_rect.y-=25
					green_brick4.scale_rect.x+=25
					green_brick4.scale_rect.y-=50
					green_s=1
				elif event.key==pygame.K_f and green_s==1 and green_brick4.scale_rect.y<450:
					green_brick.scale_rect.y-=25
					green_brick2.scale_rect.x-=25
					green_brick3.scale_rect.x-=50
					green_brick3.scale_rect.y+=25
					green_brick4.scale_rect.x-=25
					green_brick4.scale_rect.y+=50
					green_s=0

	
	if f==0 and red1_move==0:
		keys = pygame.key.get_pressed()
		for i in red.sprites():
			if keys[pygame.K_LEFT]:
				if red_brick.scale_rect.x>0:
					if red_brick4.scale_rect.y<475:
						for i in red.sprites():
							i.scale_rect.x-=10
			if keys[pygame.K_RIGHT]:
				if red_brick4.scale_rect.x<275:
					if red_brick4.scale_rect.y<475:
						for i in red.sprites():
							i.scale_rect.x+=10
			if keys[pygame.K_DOWN]:
				if red_brick4.scale_rect.y<475:
					for i in red.sprites():
						i.scale_rect.y+=10

		if f==0 and red1_move==0: 
			for i in red.sprites():
				sc.blit(i.scale,i.scale_rect)
				if red_brick4.scale_rect.y<475:
					i.scale_rect.y+=10
		
			if red_brick4.scale_rect.y>=475:
				red1_move=1
				f+=1	
				for i in red.sprites():
					i.scale_rect.x=i.scale_rect.x
					i.scale_rect.y=i.scale_rect.y
					
	if f==1 and green1_move==0:
		keys = pygame.key.get_pressed()
		for i in green.sprites():
			if keys[pygame.K_LEFT]:
				if green_brick.scale_rect.x>0:
					if green_s==0 and green_brick.scale_rect.y<475:
						for i in green.sprites():
							i.scale_rect.x-=10
					elif green_s==1 and green_brick4.scale_rect.y<450:
						for i in green.sprites():
							i.scale_rect.x-=10
			if keys[pygame.K_RIGHT]:
				if green_brick4.scale_rect.x<275:
					if green_s==0 and green_brick.scale_rect.y<475:
						for i in green.sprites():
							i.scale_rect.x+=10
					elif green_s==1 and green_brick4.scale_rect.y<450:
						for i in green.sprites():
							i.scale_rect.x+=10

			if keys[pygame.K_DOWN]:
				if green_brick4.scale_rect.y<475 and green_brick.scale_rect.y<475:
					for i in green.sprites():
						i.scale_rect.y+=10

	if f==1 and green1_move==0:
		for i in green.sprites():
			sc.blit(i.scale,i.scale_rect)
			if green_s==0 and green_brick.scale_rect.y<475:
				i.scale_rect.y+=10
			if green_s==1 and green_brick4.scale_rect.y<450:
				i.scale_rect.y+=10

			if green_brick4.scale_rect.y>=475 or green_brick.scale_rect.y>=475:
				green1_move=1
				f+=1	
				for i in green.sprites():
					i.scale_rect.x=i.scale_rect.x
					i.scale_rect.y=i.scale_rect.y
			
	if f==2 and blue1_move==0:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			if blue_brick.scale_rect.x>0:
				if blue_brick4.scale_rect.y<475:
					for i in blue.sprites():
						i.scale_rect.x-=10
		if keys[pygame.K_RIGHT]:
			if blue_brick4.scale_rect.x<275:
				if blue_brick4.scale_rect.y<475:
					for i in blue.sprites():
						i.scale_rect.x+=10
		if keys[pygame.K_DOWN]:
			if blue_brick4.scale_rect.y<475:
				for i in blue.sprites():
					i.scale_rect.y+=10

	if f==2 and blue1_move==0:
		for i in blue.sprites():
			sc.blit(i.scale,i.scale_rect)
			if blue_brick4.scale_rect.y<475:
				i.scale_rect.y+=10
		
			if blue_brick4.scale_rect.y>=475:
				blue1_move=1
				f+=1	
				for i in blue.sprites():
					i.scale_rect.x=i.scale_rect.x
					i.scale_rect.y=i.scale_rect.y

	if red1_move==1:
		for i in red.sprites():
			sc.blit(i.scale,i.scale_rect)

	if green1_move==1:
		for i in green.sprites():
			sc.blit(i.scale,i.scale_rect)

	if blue1_move==1:
		for i in blue.sprites():
			sc.blit(i.scale,i.scale_rect)

	clock.tick(FPS)
	pygame.display.update()
