import pygame
import time

from pygame.locals import*
from time import sleep

class Model():
	def __init__(self):
		self.p1 = 0
		self.p2 = 1
		self.p2x = 100
		self.p2y = 540
		self.p1x = 1300
		self.p1y = 540
		self.ph = 5
		self.pw = 5
		self.p2xd = 1
		self.p2yd = 0
		self.p1xd = -1
		self.p1yd = 0
		self.winner = "none"

	def update(self):
		self.p1x += (5 * self.p1xd)
		self.p1y += (5 * self.p1yd)
		self.p2x += (5 * self.p2xd)
		self.p2y += (5 * self.p2yd)
		if self.p1x >= 1400:
			self.p1x = 0
		elif self.p1x < 0:
			self.p1x = 1400
		elif self.p1y >= 700:
			self.p1y = 0
		elif self.p1y < 0:
			self.p1y = 700
		elif self.p2x > 1400:
			self.p2x = 0
		elif self.p2x < 0:
			self.p2x = 1400
		elif self.p2y >= 700:
			self.p2y = 0
		elif self.p2y < 0:
			self.p2y = 700

class Controller():
	def __init__(self, model):
		self.model = model
		self.keepGoing = True

	def update(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.keepGoing = False
			elif event.type == KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.keepGoing = False
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.model.p1xd = -1
			self.model.p1yd = 0
		if keys[K_RIGHT]:
			self.model.p1xd = 1
			self.model.p1yd = 0
		if keys[K_UP]:
			self.model.p1xd = 0
			self.model.p1yd = -1
		if keys[K_DOWN]:
			self.model.p1xd = 0
			self.model.p1yd = 1
		if keys[K_a]:
			self.model.p2xd = -1
			self.model.p2yd = 0
		if keys[K_d]:
			self.model.p2xd = 1
			self.model.p2yd = 0
		if keys[K_w]:
			self.model.p2xd = 0
			self.model.p2yd = -1
		if keys[K_s]:
			self.model.p2xd = 0
			self.model.p2yd = 1

class View():
	def __init__(self, model):
		self.model = model
		screen_size = (1400, 700)
		self.screen = pygame.display.set_mode(screen_size, 32)
		self.keepGoing = True
		white = (255, 255, 255)
		pygame.draw.rect(self.screen, white, (0,0,1800,1080), 0)

	def update(self):
		blue = (0, 0, 255)
		red = (255, 0, 0)
		if self.model.p1x >= 5 and self.model.p1x <= 1394 and self.model.p1y >= 5 and self.model.p1y <= 694:
			if not self.screen.get_at((self.model.p1x + (self.model.p1xd * 5), self.model.p1y + (self.model.p1yd * 5)))[:3] == (255,255,255):
				self.keepGoing = False
				self.model.winner = "red"
		if self.model.p2x >= 5 and self.model.p2x <= 1394 and self.model.p2y >= 5 and self.model.p2y <= 694:
			if not self.screen.get_at((self.model.p2x + (self.model.p2xd * 5), self.model.p2y + (self.model.p2yd * 5)))[:3] == (255,255,255):
				self.keepGoing = False
				if not self.model.winner == "red":
					self.model.winner = "blue"
				else:
					self.model.winner = "tie"
		pygame.draw.rect(self.screen, blue, (self.model.p1x, self.model.p1y, self.model.pw, self.model.ph), 0)
		pygame.draw.rect(self.screen, red, (self.model.p2x, self.model.p2y, self.model.pw, self.model.ph), 0)
		if self.model.winner == "red":
			redWins = pygame.image.load("redWins.png")
			redWins = pygame.transform.scale(redWins, (500,500))
			self.screen.blit(redWins, (450, 100))
		if self.model.winner == "blue":
			blueWins = pygame.image.load("blueWins.png")
			blueWins = pygame.transform.scale(blueWins, (500,500))
			self.screen.blit(blueWins, (450, 100))
		pygame.display.flip()

pygame.init()
m = Model()
c = Controller(m)
v = View(m)
while c.keepGoing and v.keepGoing:
	c.update()
	m.update()
	v.update()
	sleep(.04)
sleep(4)
	