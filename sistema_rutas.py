"""
Sistema de Búsqueda de Rutas Óptimas
Utiliza algoritmo A* para encontrar la mejor ruta considerando tiempo, costo y distancia
"""

import heapq
from typing import List, Tuple, Dict
import math

class NodoRuta:
    """Representa un nodo en la búsqueda de rutas"""
    
    def __init__(self, estacion, costo_real=0, heuristica=0, padre=None, linea_usada=None):
        self.estacion = estacion
        self.costo_real = costo_real  # g(n)
        self.heuristica = heuristica  # h(n)
        self.costo_total = costo_real + heuristica  # f(n) = g(n) + h(n)
        self.padre = padre
        self.linea_usada = linea_usada
    
    def __lt__(self, otro):
        """Comparación para la cola de prioridad"""
        return self.costo_total < otro.costo_total
    
    def __eq__(self, otro):
        return self.estacion == otro.estacion
    
    def reconstruir_ruta(self):
        """Reconstruye la ruta desde el inicio hasta este nodo"""
        ruta = []
        nodo_actual = self
        while nodo_actual is not None:
            ruta.append(nodo_actual.estacion)
            nodo_actual = nodo_actual.padre
        return list(reversed(ruta))

class SistemaRutas:
    """Motor de búsqueda de rutas óptimas usando A*"""
    
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento
        self.mejor_ruta = None
        self.costo_mejor_ruta = float('inf')
    
    def _calcular_distancia_euclidiana(self, estacion1, estacion2):
        """Calcula la distancia euclidiana entre dos estaciones"""
        x1, y1 = self.base_conocimiento.estaciones[estacion1]
        x2, y2 = self.base_conocimiento.estaciones[estacion2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def _obtener_heuristica(self, estacion_actual, destino, criterio='tiempo'):
        """Calcula la heurística admisible para A*"""
        distancia = self._calcular_distancia_euclidiana(estacion_actual, destino)
        
        if criterio == 'tiempo':
            # Estimación optimista: velocidad máxima
            velocidad_maxima = 2  # unida de distancia por minuto
            return distancia / velocidad_maxima
        elif criterio == 'costo':
            # Estimación optimista del costo
            costo_minimo_por_distancia = 300  # pesos por unidad
            return (distancia * costo_minimo_por_distancia) / 2
        else:
            return distancia
    
    def _obtener_vecinos(self, estacion):
        """Obtiene las estaciones vecinas directamente conectadas"""
        vecinos = []
        for linea_nombre, linea_info in self.base_conocimiento.lineas.items():
            if estacion in linea_info['estaciones']:
                idx = linea_info['estaciones'].index(estacion)
                
                # Estación anterior en la línea
                if idx > 0:
                    vecino = linea_info['estaciones'][idx - 1]
                    vecinos.append({
                        'estacion': vecino,
                        'linea': linea_nombre,
                        'tiempo': linea_info['tiempo_viaje'],
                        'costo': linea_info['costo']
                    })
                
                # Estación siguiente en la línea
                if idx < len(linea_info['estaciones']) - 1:
                    vecino = linea_info['estaciones'][idx + 1]
                    vecinos.append({
                        'estacion': vecino,
                        'linea': linea_nombre,
                        'tiempo': linea_info['tiempo_viaje'],
                        'costo': linea_info['costo']
                    })
        
        return vecinos
    
    def buscar_ruta_optima(self, origen, destino, criterio='tiempo'):
        """
        Busca la ruta óptima usando algoritmo A*
        
        Args:
            origen: estación de inicio
            destino: estación de llegada
            criterio: 'tiempo', 'costo' o 'distancia'
        
        Returns:
            Dict con la ruta y sus métricas
        """
        
        if origen not in self.base_conocimiento.estaciones:
            return {'error': f'Estación origen {origen} no existe'}
        
        if destino not in self.base_conocimiento.estaciones:
            return {'error': f'Estación destino {destino} no existe'}
        
        # Inicialización
        cola_abierta = []
        conjunto_cerrado = set()
        nodo_inicio = NodoRuta(origen, costo_real=0, heuristica=0)
        heapq.heappush(cola_abierta, nodo_inicio)
        
        mejor_costo_por_nodo = {origen: 0}
        ruta_encontrada = None
        
        while cola_abierta:
            nodo_actual = heapq.heappop(cola_abierta)
            
            # Si ya está en cerrados, continuar
            if nodo_actual.estacion in conjunto_cerrado:
                continue
            
            conjunto_cerrado.add(nodo_actual.estacion)
            
            # Si alcanzamos el destino
            if nodo_actual.estacion == destino:
                ruta_encontrada = nodo_actual
                break
            
            # Explorar vecinos
            vecinos = self._obtener_vecinos(nodo_actual.estacion)
            
            for vecino_info in vecinos:
                vecino_estacion = vecino_info['estacion']
                
                if vecino_estacion in conjunto_cerrado:
                    continue
                
                # Calcular el costo según el criterio
                if criterio == 'tiempo':
                    costo_movimiento = vecino_info['tiempo']
                elif criterio == 'costo':
                    costo_movimiento = vecino_info['costo']
                else:
                    costo_movimiento = self._calcular_distancia_euclidiana(
                        nodo_actual.estacion, vecino_estacion
                    )
                
                nuevo_costo = nodo_actual.costo_real + costo_movimiento
                
                # Solo procesar si encontramos un mejor camino
                if vecino_estacion not in mejor_costo_por_nodo or nuevo_costo < mejor_costo_por_nodo[vecino_estacion]:
                    mejor_costo_por_nodo[vecino_estacion] = nuevo_costo
                    
                    heuristica = self._obtener_heuristica(vecino_estacion, destino, criterio)
                    nodo_vecino = NodoRuta(
                        vecino_estacion,
                        costo_real=nuevo_costo,
                        heuristica=heuristica,
                        padre=nodo_actual,
                        linea_usada=vecino_info['linea']
                    )
                    
                    heapq.heappush(cola_abierta, nodo_vecino)
        
        # Construir resultado
        if ruta_encontrada:
            ruta = ruta_encontrada.reconstruir_ruta()
            return self._calcular_metricas_ruta(ruta, criterio)
        else:
            return {'error': 'No se encontró ruta entre las estaciones'}
    
    def _calcular_metricas_ruta(self, ruta, criterio):
        """Calcula las métricas completas de una ruta"""
        if len(ruta) < 2:
            return {'error': 'Ruta inválida'}
        
        tiempo_total = 0
        costo_total = 0
        distancia_total = 0
        lineas_utilizadas = set()
        transferencias = 0
        linea_actual = None
        
        pasos = []
        
        for i in range(len(ruta) - 1):
            estacion_actual = ruta[i]
            estacion_siguiente = ruta[i + 1]
            
            # Encontrar la línea que conecta estas estaciones
            linea_conexion = None
            tiempo_paso = 0
            costo_paso = 0
            
            for linea_nombre, linea_info in self.base_conocimiento.lineas.items():
                if (estacion_actual in linea_info['estaciones'] and 
                    estacion_siguiente in linea_info['estaciones']):
                    idx_actual = linea_info['estaciones'].index(estacion_actual)
                    idx_siguiente = linea_info['estaciones'].index(estacion_siguiente)
                    
                    # Verificar que sean adyacentes
                    if abs(idx_actual - idx_siguiente) == 1:
                        linea_conexion = linea_nombre
                        tiempo_paso = linea_info['tiempo_viaje']
                        costo_paso = linea_info['costo']
                        break
            
            if linea_conexion:
                tiempo_total += tiempo_paso
                costo_total += costo_paso
                lineas_utilizadas.add(linea_conexion)
                
                # Contar transferencias
                if linea_actual and linea_actual != linea_conexion:
                    transferencias += 1
                linea_actual = linea_conexion
                
                distancia_paso = self._calcular_distancia_euclidiana(
                    estacion_actual, estacion_siguiente
                )
                distancia_total += distancia_paso
                
                pasos.append({
                    'origen': estacion_actual,
                    'destino': estacion_siguiente,
                    'linea': linea_conexion,
                    'tiempo': tiempo_paso,
                    'costo': costo_paso,
                    'distancia': round(distancia_paso, 2)
                })
        
        return {
            'ruta': ruta,
            'pasos': pasos,
            'tiempo_total': tiempo_total,
            'costo_total': costo_total,
            'distancia_total': round(distancia_total, 2),
            'lineas_utilizadas': list(lineas_utilizadas),
            'num_lineas': len(lineas_utilizadas),
            'transferencias': transferencias,
            'criterio_optimizado': criterio,
            'exitosa': True
        }
    
    def comparar_rutas(self, origen, destino):
        """
        Compara las rutas óptimas según diferentes criterios
        """
        print(f"\n{'='*70}")
        print(f"Comparando rutas de {origen} a {destino}")
        print(f"{'='*70}\n")
        
        rutas = {}
        
        for criterio in ['tiempo', 'costo', 'distancia']:
            resultado = self.buscar_ruta_optima(origen, destino, criterio)
            if 'exitosa' in resultado:
                rutas[criterio] = resultado
                self._mostrar_ruta(resultado, criterio)
        
        return rutas
    
    def _mostrar_ruta(self, ruta_info, criterio):
        """Muestra una ruta de manera legible"""
        if 'error' in ruta_info:
            print(f"[ERROR] {ruta_info['error']}\n")
            return
        
        print(f"OPTIMIZACIÓN POR {criterio.upper()}:")
        print("-" * 70)
        print(f"Ruta: {' → '.join(ruta_info['ruta'])}")
        print(f"\nDetalles del viaje:")
        for i, paso in enumerate(ruta_info['pasos'], 1):
            print(f"  Paso {i}: {paso['origen']} → {paso['destino']}")
            print(f"           Línea: {paso['linea']}")
            print(f"           Tiempo: {paso['tiempo']} min | Costo: ${paso['costo']} | Distancia: {paso['distancia']} km")
        
        print(f"\nResumen:")
        print(f"  • Tiempo total: {ruta_info['tiempo_total']} minutos")
        print(f"  • Costo total: ${ruta_info['costo_total']}")
        print(f"  • Distancia total: {ruta_info['distancia_total']} km")
        print(f"  • Líneas utilizadas: {', '.join(ruta_info['lineas_utilizadas'])}")
        print(f"  • Transferencias: {ruta_info['transferencias']}\n")
