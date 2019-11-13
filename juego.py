""" 
 Mostramos como usar un sprite respaldado por un gráfico.
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Vídeo explicativo: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
 
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
# Se usa para establecer cuan rápido se actualiza la pantalla
var_izq = False
var_der = False
var_arr = False
var_aba = False
reloj = pygame.time.Clock()

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                var_arr = False 
            elif event.key == pygame.K_a:
                var_izq = False
            elif event.key == pygame.K_s:
                var_aba = False
            elif event.key == pygame.K_d:
                var_der = False

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
    pygame.draw.rect(pantalla, ROJO, [x, y, 20, 20], 0)
    pygame.display.flip()
    reloj.tick(60)
     

pygame.quit()