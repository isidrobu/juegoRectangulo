"Funciones comunes utilizadas por los diversos juegos."

import os
import pygame as p

WIDTH    = 600
HEIGHT   = 480
PANTALLA = (WIDTH, HEIGHT)


class Texto():
    "Crea un texto para mostrar en pantalla."
    def __init__(
        self, predeterminado= "", tamano= 24, fuente= None, color= (255, 0, 255)
    ):
        "Inicializa el texto."
        self.fuente = p.font.Font(fuente, tamano)
        self.default = predeterminado
        self.texto = None
        self.rect = None
        self.color = color
        self.mostrar()
        
    def mostrar(self, cadena= ""):
        "Regresa el texto a mostrar."
        self.texto = self.fuente.render(self.default + cadena, True, self.color)
        self.rect = self.texto.get_rect()
        return self.texto
        
    def pos(self, horz= 0, vert= 0, offset_x= 0, offset_y= 0):
        "Obtiene la posicion en la cual se mostrara el texto."
        if vert == 0:
            self.rect.top = offset_y
        elif vert == 1:
            self.rect.centery = HEIGHT / 2 + offset_y
        elif vert == 2:
            self.rect.bottom = HEIGHT - offset_y
        
        if horz == 0:
            self.rect.left = offset_x
        elif horz == 1:
            self.rect.centerx = WIDTH / 2 + offset_x
        elif horz == 2:
            self.rect.right = WIDTH - offset_x
        return self.rect
