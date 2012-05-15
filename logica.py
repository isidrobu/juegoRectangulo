import random
import pygame as p
from pygame.locals import K_F5
from comun import WIDTH, HEIGHT, Texto


class Logica(p.sprite.Sprite):
	"Inicia los rectangulos"
	def __init__(self):
		self.listarec=[]
		self.listarec2=[]
		self.marcador=0
		self.r1=p.Rect(300,220,25,25)
		self.segundosTotal=0
		self.fuente1=p.font.SysFont("Arial", 30,True, False)
		for x in range(50):
			w=random.randrange(10,30)
			h=random.randrange(10, 40)
			x=random.randrange(450)
			y= random.randrange(30, 450)
			self.listarec.append(p.Rect(x,y,w,h))
		for x in range(20):
			w=random.randrange(10,20)
			h=random.randrange(10, 20)
			x=random.randrange(450)
			y= random.randrange(30, 450)
			self.listarec2.append(p.Rect(x,y,w,h))
	"Contador de segundos"
	def ejecutar(self):
		self.segundosTotal=p.time.get_ticks()/1000
		
	"Resuelve los evento de teclado sin pulsar"
	def evento(self, evento):
		if evento == p.K_UP:
			self.r1.centery-=15
		if evento == p.K_DOWN:
			self.r1.centery+=15
		if evento == p.K_RIGHT:
			self.r1.centerx+=15
		if evento == p.K_LEFT:
			self.r1.centerx-=15
	"Eventos del teclado pulsado"
	def evento2(self, evento):
		if evento == p.K_UP:
			self.r1.centery-=15
		if evento == p.K_DOWN:
			self.r1.centery+=15
		if evento == p.K_RIGHT:
			self.r1.centerx+=15
		if evento == p.K_LEFT:
			self.r1.centerx-=15 
	"Si colisiona con otro rectangulo"
	def colision(self):
		for recs in self.listarec:
				if self.r1.colliderect(recs):
					self.marcador+=25
					self.listarec.remove(recs)
		for recs in self.listarec2:
				if self.r1.colliderect(recs):
					self.marcador-=15
					self.listarec2.remove(recs)	
		
	"Pinta pantalla, rectangulos"
	def actualizar(self, pantalla):
		cadena="Marcador = "+ str(self.marcador)
		pantalla.fill((0,0,0))
		txt_salir = Texto(cadena, 30)
		txt_salir.pos(2, 2)
		pantalla.blit(txt_salir.mostrar(), txt_salir.pos(20, 20, 0, 0))
		cadena="Contador: "+ str(self.segundosTotal)
		txt_salir = Texto(cadena, 30)
		txt_salir.pos(1, 0)
		pantalla.blit(txt_salir.mostrar(), txt_salir.pos(2, 2, 0, 0))
		for recs in self.listarec:
			p.draw.rect(pantalla,(255,255,0), recs)
		for recs in self.listarec2:
			p.draw.rect(pantalla,(255,0,255), recs)
		p.draw.rect(pantalla, (200,20,20), self.r1)
		p.display.update()
	"Juego terminado por acabar el tiempo"
	def terminado(self, pantalla):
		if  self.marcador<1000:
			cadena="GameOver Min 1000"+ " tu puntuacion de: " + str(self.marcador)
			pantalla.fill((0,0,0))
			self.txt_salir = Texto(cadena, tamano=30)
			self.txt_salir.pos(2, 2)
			pantalla.blit(self.txt_salir.mostrar(), self.txt_salir.pos(20, 20, 0, 0))
			p.display.update()
		else:
			cadena="Coseguido puntuacion>1000 puntos: "+ " " + str(self.marcador)
			pantalla.fill((0,0,0))
			txt_salir = Texto(cadena, 30)
			txt_salir.pos(2, 2)
			pantalla.blit(txt_salir.mostrar(), txt_salir.pos(20, 20, 0, 0))
			p.display.update()
		
	"Controla el numero de segundos totales del juego"	
	def fin(self):
		if self.segundosTotal>30:
			return True
		else:
			return False

		






		
	
