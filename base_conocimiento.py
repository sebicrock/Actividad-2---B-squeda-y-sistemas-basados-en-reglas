"""
Base de Conocimiento para Sistema de Transporte Masivo
Contiene hechos y reglas lógicas sobre las estaciones, líneas y conexiones
"""

class BaseConocimiento:
    """Almacena hechos y reglas sobre el sistema de transporte"""
    
    def __init__(self):
        # Hechos: estaciones con sus coordenadas (x, y) - Ciudades y municipios colombianos
        self.estaciones = {
            'Bogota_Centro': (0, 0),                    # Carrera 7 con Calle 19
            'Bogota_SantaFe': (1, 2),                  # Sector Santa Fe
            'Bogota_Chapinero': (2, 3),                # Zona de Chapinero
            'Bogota_Suba': (-1, 4),                    # Localidad de Suba
            'Mosquera': (-3, 1),                       # Municipio de Mosquera
            'Funza': (-2, -1),                         # Municipio de Funza
            'Soacha': (1, -3),                         # Municipio de Soacha
            'Zipaquira': (0, 5),                       # Municipio de Zipaquirá
            'Chia': (2, 4),                            # Municipio de Chía
            'Facatativa': (-4, 2),                     # Municipio de Facatativá
            'Cajica': (1, 5),                          # Municipio de Cajicá
            'Madrid': (-3, 0)                          # Municipio de Madrid
        }
        
        # Hechos: líneas de transporte con sus estaciones - Rutas reales de transporte masivo
        self.lineas = {
            'Transmilenio_K80': {
                'estaciones': ['Bogota_Centro', 'Bogota_Chapinero', 'Bogota_Suba', 'Zipaquira'],
                'tiempo_viaje': 15,  # minutos entre estaciones
                'costo': 2950  # pesos colombianos
            },
            'Ruta_Expreso_Mosquera': {
                'estaciones': ['Mosquera', 'Madrid', 'Funza', 'Bogota_Centro'],
                'tiempo_viaje': 20,  # minutos entre estaciones
                'costo': 2500  # buseta/colectivo
            },
            'Bus_Soacha_Bogota': {
                'estaciones': ['Soacha', 'Bogota_Centro', 'Bogota_SantaFe', 'Bogota_Chapinero'],
                'tiempo_viaje': 18,  # minutos entre estaciones
                'costo': 2850  # pesos
            },
            'Ruta_Chia_Cajica': {
                'estaciones': ['Facatativa', 'Chia', 'Cajica', 'Bogota_Suba'],
                'tiempo_viaje': 12,  # minutos entre estaciones
                'costo': 2500  # pesos
            },
            'Circular_Centro': {
                'estaciones': ['Bogota_Centro', 'Bogota_SantaFe', 'Bogota_Chapinero', 'Bogota_Suba'],
                'tiempo_viaje': 10,  # minutos entre estaciones
                'costo': 2950  # Transmilenio integrado
            }
        }
        
        # Reglas lógicas en formato (condición, consecuencia)
        self.reglas = [
            # Regla 1: Conectividad directa
            {
                'nombre': 'conectividad_directa',
                'descripcion': 'Si dos estaciones están en la misma línea, están directamente conectadas',
                'condicion': self._estaciones_en_misma_linea,
                'consecuencia': self._agregar_conexion_directa
            },
            # Regla 2: Equivalencia de estaciones
            {
                'nombre': 'proximidad_geografica',
                'descripcion': 'Si dos estaciones están muy cercanas, se pueden considerar alternativas',
                'condicion': self._estaciones_proximas,
                'consecuencia': self._marcar_alternativa
            },
            # Regla 3: Transferencia
            {
                'nombre': 'punto_transferencia',
                'descripcion': 'Si una estación está en múltiples líneas, es punto de transferencia',
                'condicion': self._es_punto_transferencia,
                'consecuencia': self._marcar_transferencia
            }
        ]
        
        # Hechos derivados (se actualizan con inferencias)
        self.hechos_derivados = {
            'conexiones': {},
            'puntos_transferencia': [],
            'alternativas': {}
        }
    
    def _estaciones_en_misma_linea(self, linea):
        """Verifica si hay estaciones en la misma línea"""
        return len(linea['estaciones']) > 1
    
    def _agregar_conexion_directa(self, linea):
        """Agrega conexión directa entre estaciones consecutivas"""
        estaciones = linea['estaciones']
        for i in range(len(estaciones) - 1):
            key = (estaciones[i], estaciones[i + 1])
            if key not in self.hechos_derivados['conexiones']:
                self.hechos_derivados['conexiones'][key] = {
                    'linea': linea['nombre'] if 'nombre' in linea else 'desconocida',
                    'tiempo': linea['tiempo_viaje'],
                    'costo': linea['costo']
                }
    
    def _estaciones_proximas(self, estacion1, estacion2, limite=3):
        """Verifica si dos estaciones están geográficamente cercanas"""
        if estacion1 in self.estaciones and estacion2 in self.estaciones:
            x1, y1 = self.estaciones[estacion1]
            x2, y2 = self.estaciones[estacion2]
            distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            return distancia <= limite
        return False
    
    def _marcar_alternativa(self, estacion1, estacion2):
        """Marca estaciones como alternativas una de la otra"""
        if estacion1 not in self.hechos_derivados['alternativas']:
            self.hechos_derivados['alternativas'][estacion1] = []
        self.hechos_derivados['alternativas'][estacion1].append(estacion2)
    
    def _es_punto_transferencia(self, estacion):
        """Verifica si una estación es punto de transferencia"""
        contador = 0
        for linea in self.lineas.values():
            if estacion in linea['estaciones']:
                contador += 1
        return contador > 1
    
    def _marcar_transferencia(self, estacion):
        """Marca una estación como punto de transferencia"""
        if estacion not in self.hechos_derivados['puntos_transferencia']:
            self.hechos_derivados['puntos_transferencia'].append(estacion)
    
    def agregar_estacion(self, nombre, coordenadas):
        """Agrega una nueva estación a la base de conocimiento"""
        self.estaciones[nombre] = coordenadas
    
    def agregar_linea(self, nombre_linea, estaciones, tiempo_viaje, costo):
        """Agrega una nueva línea de transporte"""
        self.lineas[nombre_linea] = {
            'estaciones': estaciones,
            'tiempo_viaje': tiempo_viaje,
            'costo': costo
        }
    
    def obtener_lineas_estacion(self, estacion):
        """Obtiene todas las líneas que pasan por una estación"""
        lineas_disponibles = []
        for nombre_linea, linea in self.lineas.items():
            if estacion in linea['estaciones']:
                lineas_disponibles.append(nombre_linea)
        return lineas_disponibles
    
    def obtener_estaciones_conexas(self, estacion):
        """Obtiene todas las estaciones conectadas a la actual"""
        conexas = set()
        for linea in self.lineas.values():
            if estacion in linea['estaciones']:
                idx = linea['estaciones'].index(estacion)
                if idx > 0:
                    conexas.add(linea['estaciones'][idx - 1])
                if idx < len(linea['estaciones']) - 1:
                    conexas.add(linea['estaciones'][idx + 1])
        return list(conexas)
