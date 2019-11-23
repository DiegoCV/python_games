
import pygame 
import numpy as np
from Linea import *
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
y_t = 100

filas = 3
columnas = 3



# Se usa para establecer cuan rápido se actualiza la pantalla
var_izq = False
var_der = False
var_arr = False
var_aba = False

#ANCHO ENTRE LOS PUNTOS 
sep = 20

#VARIABLES PARA CONTROLAR LA POSICION DE LA LINEA D E POSICION ACTUAL
lc_coord_ini = [x_t, y_t]
lc_coord_fin = [x_t + sep, y_t]

#Lineas definitivas
lineas_final = []

#Matriz con el estado actual del juego filas columnas
tablero = Tablero(filas, columnas)

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
    

def pintar_lineas_final():
    for linea in lineas_final:
        pintar_linea((linea.get_x_0(), linea.get_y_0()), (linea.get_x_1(), linea.get_y_1()), AZUL)
        #pintar_linea([linea["c_ini"][0], linea["c_ini"][1]], [linea["c_fin"][0], linea["c_fin"][1]], AZUL)
        #print()

#Se encarga de comprobar si la ultima linea puesta encierra un cuadrado
def validar_cuadro(c_ini, c_fin):
    if esta_vertical_linea(c_ini, c_fin):
        #Valido la linea del frente
        print(obtener_nodo(sumeCoordenada(c_ini,'h','d')))
        if hay_relacion(obtener_nodo(sumeCoordenada(c_ini,'h','d')), obtener_nodo(sumeCoordenada(c_fin,'h','d'))):
            if hay_relacion(obtener_nodo(c_ini), obtener_nodo(sumeCoordenada(c_fin,'h','d'))):
                if hay_relacion(obtener_nodo(c_fin), obtener_nodo(sumeCoordenada(c_fin,'h','d'))):
                    return True
        else:
            return False

    elif esta_horizontal_linea(c_ini, c_fin):
        return 1
        
def sumeCoordenada(c_cord, orientacion, direccion):
    if orientacion == 'h':
        if direccion == 'd':
            c_cord[1] = c_cord[1] + sep
        else:
            c_cord[1] = c_cord[1] - sep
    else:
        if direccion == 'a':
            c_cord[0] = c_cord[0] - sep
        else:
            c_cord[0] = c_cord[0] + sep
    return c_cord



def pintar_linea(c_ini, c_fin, color):
    pygame.draw.line(pantalla, color, c_ini, c_fin, 1)

def mover_lc_arriba():
    lc_coord_ini[1] = lc_coord_ini[1] - sep
    lc_coord_fin[1] = lc_coord_fin[1] - sep

def mover_lc_abajo():
    lc_coord_ini[1] = lc_coord_ini[1] + sep
    lc_coord_fin[1] = lc_coord_fin[1] + sep

def mover_lc_izquierda():
    lc_coord_ini[0] = lc_coord_ini[0] - sep
    lc_coord_fin[0] = lc_coord_fin[0] - sep

def mover_lc_derecha():
    lc_coord_ini[0] = lc_coord_ini[0] + sep
    lc_coord_fin[0] = lc_coord_fin[0] + sep

def cambiar_posicion():
    if esta_vertical_linea_principal():
        lc_coord_fin[0] = lc_coord_ini[0]
        lc_coord_fin[1] = lc_coord_ini[1] + sep
    elif esta_horizontal_linea_principal():
        lc_coord_fin[0] = lc_coord_ini[0] + sep
        lc_coord_fin[1] = lc_coord_ini[1]

def esta_vertical_linea_principal():
    return lc_coord_ini[1] == lc_coord_fin[1]

def esta_horizontal_linea_principal():
    return lc_coord_ini[0] == lc_coord_fin[0]

def esta_vertical_linea(c_ini, c_fin):
    return c_ini[0] == c_fin[0]

def esta_horizontal_linea(c_ini, c_fin):
    return c_ini[1] == c_fin[1]


def parsear_coordenada(coordenada):
    return [int((coordenada[1] - 100)/20), int((coordenada[0] - 100)/sep)]


# -------- Bucle principal del Programa -----------
while not hecho:
   
    # --- Bucle principal de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            hecho = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mover_lc_arriba()
            elif event.key == pygame.K_a:
                mover_lc_izquierda()
            elif event.key == pygame.K_s:
                mover_lc_abajo()
            elif event.key == pygame.K_d:
                mover_lc_derecha()
            elif event.key == pygame.K_f:
                cambiar_posicion()
            elif event.key == pygame.K_r:
                registrar_linea(lc_coord_ini, lc_coord_fin)
                print(validar_cuadro(lc_coord_ini, lc_coord_fin))
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
    pintar_lineas_final()
    pintar_puntos(columnas, filas, sep, [100,100])
    #pintar_linea(lc_coord_ini, lc_coord_fin, VERDE)
    pintar_linea(lc_coord_ini, lc_coord_fin, VERDE)
    #pintar_linea([120,120], [140,140], VERDE)
    #pintar_linea([160,160], [180,180], VERDE)
    #pintar_lineas_final()
    
    
    pygame.display.flip()
    reloj.tick(60)
     

pygame.quit()


