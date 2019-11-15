
import pygame 
import time

pygame.init()
pantalla = pygame.display.set_mode([ANCHO, LARGO]) 
pygame.display.set_caption("Lineas")

#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
hecho = False
x = ANCHO/2
y = LARGO*0.8

ancho_juego = 5
largo_juego = 5

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
        elif event.type == nueva_linea:
            if perdio == False:
                if bucle_generar > bucle_time:                    
                    generarCuadros()
                    bucle_generar = 0
                bucle_generar = bucle_generar + 1  
                bucle = bucle + 1           
                if bucle == 510:
                    vel_caida = vel_caida + 1
                    bucle = 0
                    bucle_time = bucle_time - vel_caida * 2

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
        bucle = 0
        bucle_time = 50
        pygame.draw.rect(pantalla, ROJO, [x, y, 20, 20], 0)
        pygame.display.update()
     

pygame.quit()


