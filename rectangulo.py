"Modulo para gestion de escenas en Pygame."

import pygame as p
from pygame.locals import K_ESCAPE
from comun import PANTALLA
from logica import Logica

class Rectangulo():

    def __init__(self, titulo= ""):
		"Inicializar Pygame."
		p.init()
		self.pantalla = p.display.set_mode(PANTALLA)
		self.pantalla.fill((0,0,0))
		p.display.set_caption(titulo)
		self.reloj = p.time.Clock()
		self.logica = Logica()
		
        
    def ejecutar(self):
		"Ejecuta la logica del juego."
		jugando = True
		while jugando:
			self.reloj.tick(60)
			if self.logica.fin() == False: 
				self.logica.ejecutar()
				for event in p.event.get():
					if event.type == p.KEYDOWN:
						self.logica.evento(event.key)
					if event.type == p.KEYUP:
						self.logica.evento2(event.key)			
				self.logica.colision()
				self.logica.actualizar(self.pantalla)
				p.display.flip()
			else:
				self.logica.terminado(self.pantalla)
			for event in p.event.get():
				if event.type == p.QUIT:
					jugando=False
		p.quit()
	




