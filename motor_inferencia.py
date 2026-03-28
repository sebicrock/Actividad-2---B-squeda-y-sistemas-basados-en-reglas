"""
Motor de Inferencia con Forward Chaining
Aplica reglas lógicas sobre la base de conocimiento para derivar nuevos hechos
"""

class MotorInferencia:
    """Motor de inferencia que aplica reglas lógicas de manera iterativa"""
    
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento
        self.hechos_nuevos = []
        self.ciclos_inferencia = 0
        self.max_ciclos = 10
    
    def inferir(self):
        """Ejecuta el proceso de forward chaining hasta que no haya nuevos hechos"""
        print("Iniciando proceso de inferencia...")
        print("-" * 60)
        
        while self.ciclos_inferencia < self.max_ciclos:
            hechos_antes = len(self._obtener_hechos())
            self._aplicar_reglas()
            hechos_despues = len(self._obtener_hechos())
            
            self.ciclos_inferencia += 1
            print(f"Ciclo {self.ciclos_inferencia}: Hechos encontrados: {hechos_despues}")
            
            # Si no hay nuevos hechos, detenemos
            if hechos_antes == hechos_despues:
                print("No hay nuevos hechos. Inferencia completada.")
                break
        
        print("-" * 60)
        self._mostrar_hechos_derivados()
    
    def _aplicar_reglas(self):
        """Aplica todas las reglas de la base de conocimiento"""
        # Regla 1: Conectividad directa
        for nombre_linea, linea in self.base_conocimiento.lineas.items():
            linea['nombre'] = nombre_linea
            if self.base_conocimiento._estaciones_en_misma_linea(linea):
                self.base_conocimiento._agregar_conexion_directa(linea)
        
        # Regla 2: Proximidad geográfica
        estaciones = list(self.base_conocimiento.estaciones.keys())
        for i in range(len(estaciones)):
            for j in range(i + 1, len(estaciones)):
                if self.base_conocimiento._estaciones_proximas(estaciones[i], estaciones[j]):
                    self.base_conocimiento._marcar_alternativa(estaciones[i], estaciones[j])
                    self.base_conocimiento._marcar_alternativa(estaciones[j], estaciones[i])
        
        # Regla 3: Puntos de transferencia
        for estacion in self.base_conocimiento.estaciones.keys():
            if self.base_conocimiento._es_punto_transferencia(estacion):
                self.base_conocimiento._marcar_transferencia(estacion)
    
    def _obtener_hechos(self):
        """Obtiene todos los hechos derivados"""
        hechos = []
        hechos.extend(self.base_conocimiento.hechos_derivados['conexiones'].keys())
        hechos.extend(self.base_conocimiento.hechos_derivados['puntos_transferencia'])
        return hechos
    
    def _mostrar_hechos_derivados(self):
        """Muestra los hechos derivados de manera legible"""
        print("\n=== HECHOS DERIVADOS ===\n")
        
        print("1. CONEXIONES DIRECTAS:")
        print("-" * 40)
        for (origen, destino), info in self.base_conocimiento.hechos_derivados['conexiones'].items():
            print(f"  {origen} → {destino}")
            print(f"    Línea: {info['linea']}")
            print(f"    Tiempo: {info['tiempo']} min | Costo: ${info['costo']}")
        
        print("\n2. PUNTOS DE TRANSFERENCIA:")
        print("-" * 40)
        for punto in self.base_conocimiento.hechos_derivados['puntos_transferencia']:
            lineas = self.base_conocimiento.obtener_lineas_estacion(punto)
            print(f"  {punto}: {', '.join(lineas)}")
        
        print("\n3. ESTACIONES ALTERNATIVAS (PROXIMIDAD):")
        print("-" * 40)
        for estacion, alternativas in self.base_conocimiento.hechos_derivados['alternativas'].items():
            if alternativas:
                print(f"  {estacion} → {alternativas}")
    
    def consultar_hecho(self, condicion):
        """Consulta si un hecho existe en la base de datos"""
        # Busca en conexiones
        if condicion in self.base_conocimiento.hechos_derivados['conexiones']:
            return True
        # Busca en puntos de transferencia
        if condicion in self.base_conocimiento.hechos_derivados['puntos_transferencia']:
            return True
        return False
    
    def obtener_especializacion(self, concepto):
        """Obtiene las especializaciones de un concepto (hechos más específicos)"""
        especializaciones = []
        
        # Buscar en conexiones que son especializaciones del concepto
        for (origen, destino), info in self.base_conocimiento.hechos_derivados['conexiones'].items():
            if origen == concepto or destino == concepto:
                especializaciones.append((origen, destino, info))
        
        return especializaciones
