
import pygame 
import time
ANCHO = 700
LARGO = 500
pygame.init()
pantalla = pygame.display.set_mode([ANCHO, LARGO]) 
pygame.display.set_caption("Lineas")

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
hecho = False
x = ANCHO/2
y = LARGO*0.8
x_t = 100
y_t = 50

ancho_juego = 5
largo_juego = 5

# Se usa para establecer cuan rápido se actualiza la pantalla
var_izq = False
var_der = False
var_arr = False
var_aba = False

reloj = pygame.time.Clock()

def pintar_puntos(can_x, can_y, sep, coord_ini):
    i = 0
    j = 0
    v_x = coord_ini[0]
    v_y = coord_ini[1]
    while(j < can_y):
        i = 0
        while(i < can_x):
            pygame.draw.circle(pantalla, ROJO, (v_x, v_y), 3, 0)
            v_x = v_x + sep
            i = i + 1
        v_x = coord_ini[0]
        v_y = v_y + sep
        j = j + 1

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
    
    pintar_puntos(10, 5, 20, [100,100])
    pygame.display.flip()
    reloj.tick(60)
     

pygame.quit()


