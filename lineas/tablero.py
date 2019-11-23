import numpy as np

class Tablero():
	
	def __init__(self, filas, columnas):
		self.filas = filas
		self.columnas = columnas
		self.nodos = filas * columnas
		self.cuadros = ( filas - 1 ) * ( columnas - 1 )
		self.matriz_adyacencia = np.zeros((self.nodos, self.nodos), dtype=bool)
		self.cuadros = np.zeros((self.cuadros), dtype=bool)
		#filas = self.cuadros / ( self.columnas - 1 )
		
		
	def hay_relacion(self, nodo_1, nodo_2):
    	return self.matriz_adyacencia.item(nodo_1, nodo_2)   

    def registrar_linea(self, nodo_1, nodo_2):
    	matriz_estado.itemset((nodo_1,nodo_2), True)
    	matriz_estado.itemset((nodo_2,nodo_1), True)
    	#Registrar el cuadro

    #Devuelve los indices de los cuadros que hace parte una linea
    def obtener_cuadros(self, nodo_1, nodo_2):
    	indice_cuadros = []
		mi_fila_por_linea = self.fila_por_linea(nodo_1, nodo_2)
		indice_izq = ( ( self.columnas - 1 ) * mi_fila_por_linea ) + columna_por_nodo(nodo_1)
		indice_der = indice_izq + 1
		if self.cuadros.item(indice_izq):
			indice_cuadros.appened(indice_izq)

		if self.cuadros.item(indice_der):
			indice_cuadros.item(indice_der)

    	return indice_cuadros

    def registrar_cuadro():
    	pass

    def es_horizontal(self, nodo_1, nodo_2):
    	return (nodo_1 - 1) == nodo_2 or (nodo_1 + 1) == nodo_2

    def columna_por_linea(self, nodo_1, nodo_2):
    	return 0

    #Solo funciona para linea verticales, esta basado en la matriz abstarcta de cuadros no de puntos
    def fila_por_linea(self, nodo_1, nodo_2):
    	fila_n_1 = fila_por_nodo(nodo_1)
    	fila_n_2 = fila_por_nodo(nodo_2)
    	if (fila_n_1 + 1) == fila_n_2:
    		return fila_n_1
    	return -1

    def fila_por_nodo(self, nodo_1):
    	mi_f = 0
    	var = 0
    	for fil in range(0, self.nodos):
    		if fil == nodo_1:
    			return mi_f
    		if var == self.columnas - 1:
    			mi_f = mi_f + 1 
    		var = var + 1

    def columna_por_nodo(self, nodo_1):
    	return nodo_1 - self.columnas
		