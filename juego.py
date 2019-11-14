""" 
 Mostramos como usar un sprite respaldado por un gráfico.
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Vídeo explicativo: http://youtu.be/vRB_983kUMc
"""
 
import pygame 
import time
from random import randint
from Cuadro import *

 
# Definimos algunos colores
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
ANCHO = 700
LARGO = 500
x_1 = 20
x_2 = ANCHO - x_1
y_1 = 20
y_2 = LARGO - y_1
pygame.init()
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [ANCHO, LARGO]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")

#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
 
hecho = False
x = ANCHO/2
y = LARGO*0.8
vel = 5
vel_caida = 1
# Se usa para establecer cuan rápido se actualiza la pantalla
var_izq = False
var_der = False
var_arr = False
var_aba = False
reloj = pygame.time.Clock()


cuadros = []

bucle = 0
perdio = False
flag_velocidad = 0
limit_bucle = 10

def moverCuadros(actual):
    for i in (cuadros): 
        i.aumentarY(vel_caida)
        obstaculo = pygame.draw.rect(pantalla, AZUL, [i.getX(), i.getY(), 20, 20], 0)
        if actual.colliderect(obstaculo):
            return True
    return False

def generarCuadros():
    for i in range(0,3): 
        cuadros.append(Cuadro(randint(x_1, x_2),y_1))  

def mostrarFinJuego():
    font = pygame.font.Font('freesansbold.ttf', 32)  
    text = font.render('Fin del juego, presione r', True, AZUL, NEGRO) 
    textRect = text.get_rect()   
    textRect.center = (ANCHO // 2, LARGO // 2) 
    pantalla.blit(text, textRect)

    
# -------- Bucle principal del Programa -----------
while not hecho:
   
    # --- Bucle principal de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            hecho = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if y - vel > y_1:
                    y -= vel
                    var_arr = True 
            elif event.key == pygame.K_a:
                if x - vel > x_1:
                    x -= vel
                    var_izq = True
            elif event.key == pygame.K_s:
                if y - vel < y_2:
                    y += vel
                    var_aba = True
            elif event.key == pygame.K_d:
                if x + vel < x_2:
                    x += vel
                    var_der = True
            elif event.key == pygame.K_r:
                if(perdio == True):                          
                    perdio = False                
                    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                var_arr = False 
            elif event.key == pygame.K_a:
                var_izq = False
            elif event.key == pygame.K_s:
                var_aba = False
            elif event.key == pygame.K_d:
                var_der = False

    if perdio == False:
        if var_izq == True:
            if x - vel > x_1:
                x -= vel

        if var_der == True:
            if x + vel < x_2:
                x += vel

        if var_arr == True:
            if y - vel > y_1:
                y -= vel

        if var_aba == True:
            if y - vel < y_2:
                y += vel
     
        pantalla.fill(BLANCO)
        actual = pygame.draw.rect(pantalla, ROJO, [x, y, 20, 20], 0)
        perdio = moverCuadros(actual)


        if bucle == 0:
            generarCuadros()
        
        if bucle > limit_bucle:
            bucle = 0
            flag_velocidad = flag_velocidad + 1
            if flag_velocidad == 5:
                vel_caida = vel_caida + 1
                flag_velocidad = 0
        else:
            bucle = bucle + 1

        pygame.display.flip()
        reloj.tick(60)
    else:
        pantalla.fill(BLANCO)
        mostrarFinJuego()
        x = ANCHO/2
        y = LARGO*0.8
        cuadros = []    
        flag_velocidad = 0
        vel_caida = 1    
        limit_bucle = 40 
        pygame.draw.rect(pantalla, ROJO, [x, y, 20, 20], 0)
        pygame.display.update()
     

pygame.quit()



