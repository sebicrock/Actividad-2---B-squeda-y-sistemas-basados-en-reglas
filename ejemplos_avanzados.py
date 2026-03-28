"""
Ejemplos Avanzados de Uso del Sistema de Rutas
Casos de uso complejos y análisis detallado
"""

from base_conocimiento import BaseConocimiento
from motor_inferencia import MotorInferencia
from sistema_rutas import SistemaRutas

def ejemplo_1_expansion_sistema():
    """Ejemplo: Expandir el sistema con nuevas líneas y estaciones"""
    
    print("\n" + "="*70)
    print("EJEMPLO 1: EXPANSIÓN DEL SISTEMA DE TRANSPORTE")
    print("="*70 + "\n")
    
    bc = BaseConocimiento()
    
    print("🚀 Agregando nuevas estaciones...")
    bc.agregar_estacion('Zipaquira_Centro', (0, 6))
    bc.agregar_estacion('Nemocón', (1, 6))
    bc.agregar_estacion('La_Calera', (2, 5))
    
    print("✓ Nuevas estaciones agregadas: Zipaquira_Centro, Nemocón, La_Calera")
    
    print("\n🚃 Agregando nuevas líneas...")
    bc.agregar_linea('Ruta_Sabana',
                     ['Bogota_Centro', 'Chia', 'Nemocón', 'Zipaquira_Centro'],
                     tiempo_viaje=15,
                     costo=2500)
    
    bc.agregar_linea('Bus_Union',
                     ['Zipaquira_Centro', 'La_Calera', 'Bogota_Suba'],
                     tiempo_viaje=12,
                     costo=2200)
    
    print("✓ Nuevas líneas agregadas: Ruta_Sabana, Bus_Union")
    
    print(f"\nTotal de estaciones: {len(bc.estaciones)}")
    print(f"Total de líneas: {len(bc.lineas)}")
    
    # Ejecutar inferencia
    motor = MotorInferencia(bc)
    motor.inferir()
    
    # Buscar rutas en el sistema expandido
    sr = SistemaRutas(bc)
    
    print("\n📍 Búsqueda de rutas en el sistema expandido:")
    print("-" * 70)
    
    resultado = sr.buscar_ruta_optima('A_Centro', 'Aeropuerto', 'tiempo')
    sr._mostrar_ruta(resultado, 'tiempo')
    
    resultado = sr.buscar_ruta_optima('Hospital_Central', 'Parque_Mayor', 'costo')
    sr._mostrar_ruta(resultado, 'costo')

def ejemplo_2_analisis_puntos_criticos():
    """Ejemplo: Análisis de puntos críticos (hubs de transferencia)"""
    
    print("\n" + "="*70)
    print("EJEMPLO 2: ANÁLISIS DE PUNTOS CRÍTICOS DE TRANSFERENCIA")
    print("="*70 + "\n")
    
    bc = BaseConocimiento()
    motor = MotorInferencia(bc)
    motor.inferir()
    
    print("🔍 Identificando hubs de transferencia...")
    print("-" * 70)
    
    # Contar líneas por estación
    estaciones_por_linea = {}
    for estacion in bc.estaciones:
        lineas = bc.obtener_lineas_estacion(estacion)
        estaciones_por_linea[estacion] = len(lineas)
    
    # Ordenar por importancia
    importancia = sorted(estaciones_por_linea.items(), 
                        key=lambda x: x[1], reverse=True)
    
    print(f"\n{'Estación':<20} {'Líneas':<10} {'Importancia':<20}")
    print("-" * 50)
    
    for estacion, num_lineas in importancia:
        if num_lineas > 0:
            barra = "█" * num_lineas
            print(f"{estacion:<20} {num_lineas:<10} {barra}")
    
    print("\n📊 Estadísticas de conectividad:")
    print("-" * 70)
    
    promedio_lineas = sum(estaciones_por_linea.values()) / len(estaciones_por_linea)
    print(f"Líneas promedio por estación: {promedio_lineas:.2f}")
    print(f"Máximo número de líneas: {max(estaciones_por_linea.values())}")
    print(f"Mínimo número de líneas: {min(estaciones_por_linea.values())}")

def ejemplo_3_analisis_costo_beneficio():
    """Ejemplo: Comparación de costo-beneficio en diferentes rutas"""
    
    print("\n" + "="*70)
    print("EJEMPLO 3: ANÁLISIS DE COSTO-BENEFICIO")
    print("="*70 + "\n")
    
    bc = BaseConocimiento()
    motor = MotorInferencia(bc)
    motor.inferir()
    sr = SistemaRutas(bc)
    
    pares_estaciones = [
        ('Mosquera', 'Bogota_Centro'),
        ('Funza', 'Bogota_Chapinero'),
        ('Soacha', 'Zipaquira')
    ]
    
    print("Comparando diferentes criterios de optimización...\n")
    
    for origen, destino in pares_estaciones:
        print(f"\n{'='*70}")
        print(f"Ruta: {origen} -> {destino}")
        print(f"{'='*70}")
        
        ruta_tiempo = sr.buscar_ruta_optima(origen, destino, 'tiempo')
        ruta_costo = sr.buscar_ruta_optima(origen, destino, 'costo')
        ruta_distancia = sr.buscar_ruta_optima(origen, destino, 'distancia')
        
        if 'exitosa' in ruta_tiempo and 'exitosa' in ruta_costo:
            print("\n┌─── OPTIMIZADO POR TIEMPO ───┐")
            print(f"│ Tiempo: {ruta_tiempo['tiempo_total']} min")
            print(f"│ Costo: ${ruta_costo['costo_total']}")
            print(f"│ Distancia: {ruta_tiempo['distancia_total']} km")
            print(f"│ Pasos: {len(ruta_tiempo['pasos'])}")
            print(f"└──────────────────────────────┘")
            
            print("\n┌─── OPTIMIZADO POR COSTO ───┐")
            print(f"│ Tiempo: {ruta_costo['tiempo_total']} min")
            print(f"│ Costo: ${ruta_costo['costo_total']}")
            print(f"│ Distancia: {ruta_costo['distancia_total']} km")
            print(f"│ Pasos: {len(ruta_costo['pasos'])}")
            print(f"└──────────────────────────────┘")
            
            print("\n┌─── OPTIMIZADO POR DISTANCIA ───┐")
            print(f"│ Tiempo: {ruta_distancia['tiempo_total']} min")
            print(f"│ Costo: ${ruta_distancia['costo_total']}")
            print(f"│ Distancia: {ruta_distancia['distancia_total']} km")
            print(f"│ Pasos: {len(ruta_distancia['pasos'])}")
            print(f"└──────────────────────────────────┘")
            
            # Análisis
            ahorro_costo = ruta_tiempo['costo_total'] - ruta_costo['costo_total']
            perdida_tiempo = ruta_costo['tiempo_total'] - ruta_tiempo['tiempo_total']
            
            if ahorro_costo != 0:
                print(f"\n💰 Al elegir costo: Ahorras ${abs(ahorro_costo)} pero pierdes {abs(perdida_tiempo)} min")

def ejemplo_4_grafos_conectividad():
    """Ejemplo: Análisis de grafos y conectividad"""
    
    print("\n" + "="*70)
    print("EJEMPLO 4: ANÁLISIS DE GRAFOS Y CONECTIVIDAD")
    print("="*70 + "\n")
    
    bc = BaseConocimiento()
    motor = MotorInferencia(bc)
    motor.inferir()
    
    print("📊 Matriz de adyacencia (estaciones conectadas directamente):\n")
    
    estaciones = list(bc.estaciones.keys())
    
    # Crear matriz de conectividad
    conexiones = {}
    for est in estaciones:
        conexiones[est] = bc.obtener_estaciones_conexas(est)
    
    # Mostrar de manera compacta
    for estacion, conectadas in sorted(conexiones.items()):
        if conectadas:
            print(f"  {estacion:20} → {', '.join(conectadas)}")
    
    print("\n📈 Estadísticas de conectividad:")
    print("-" * 70)
    
    # Calcular grado de cada nodo
    grados = {est: len(conexiones[est]) for est in estaciones}
    
    print(f"\nGrado promedio: {sum(grados.values()) / len(grados):.2f}")
    print(f"Nodo más conectado: {max(grados, key=grados.get)} ({max(grados.values())} conexiones)")
    print(f"Nodo menos conectado: {min(grados, key=grados.get)} ({min(grados.values())} conexiones)")
    
    # Verificar si hay aislados
    aislados = [est for est in grados if grados[est] == 0]
    if aislados:
        print(f"Estaciones aisladas: {aislados}")
    else:
        print("✓ Todas las estaciones están conectadas")

def ejemplo_5_simulacion_viaje():
    """Ejemplo: Simulación interactiva de un viaje"""
    
    print("\n" + "="*70)
    print("EJEMPLO 5: SIMULACIÓN DE VIAJE INTERACTIVO")
    print("="*70 + "\n")
    
    bc = BaseConocimiento()
    motor = MotorInferencia(bc)
    motor.inferir()
    sr = SistemaRutas(bc)
    
    # Viaje predefinido
    origen = 'A_Sur'
    destino = 'B_Este'
    
    print(f"👤 Pasajero sube en: {origen}")
    print(f"🎯 Destino: {destino}\n")
    
    # Obtener mejor ruta
    ruta = sr.buscar_ruta_optima(origen, destino, 'tiempo')
    
    if 'exitosa' in ruta:
        print("🚌 Iniciando viaje...\n")
        print(f"Total de paradas: {len(ruta['ruta'])}")
        print(f"Tiempo estimado: {ruta['tiempo_total']} minutos")
        print(f"Costo del viaje: ${ruta['costo_total']}\n")
        
        print("📍 Itinerario detallado:")
        print("-" * 70)
        
        tiempo_acumulado = 0
        costo_acumulado = 0
        
        for i, paso in enumerate(ruta['pasos'], 1):
            tiempo_acumulado += paso['tiempo']
            costo_acumulado += paso['costo']
            
            print(f"\nPaso {i}:")
            print(f"  Origen: {paso['origen']}")
            print(f"  Destino: {paso['destino']}")
            print(f"  Línea: {paso['linea']}")
            print(f"  Duración: {paso['tiempo']} min")
            print(f"  Costo: ${paso['costo']}")
            print(f"  Tiempo acumulado: {tiempo_acumulado} min")
            print(f"  Costo acumulado: ${costo_acumulado}")
        
        print("\n✓ ¡Viaje completado exitosamente!")
        print(f"Transferencias totales: {ruta['transferencias']}")

def menu_ejemplos():
    """Menú para seleccionar ejemplos"""
    
    ejemplos = {
        '1': ('Expansión del Sistema', ejemplo_1_expansion_sistema),
        '2': ('Análisis de Puntos Críticos', ejemplo_2_analisis_puntos_criticos),
        '3': ('Análisis de Costo-Beneficio', ejemplo_3_analisis_costo_beneficio),
        '4': ('Análisis de Grafos', ejemplo_4_grafos_conectividad),
        '5': ('Simulación de Viaje', ejemplo_5_simulacion_viaje),
        '0': ('Ejecutar todos los ejemplos', None)
    }
    
    print("\n" + "="*70)
    print("EJEMPLOS AVANZADOS - SISTEMA DE RUTAS INTELIGENTE")
    print("="*70)
    
    for key, (desc, _) in ejemplos.items():
        print(f"  {key}. {desc}")
    
    seleccion = input("\nSeleccione un ejemplo (0-5): ").strip()
    
    if seleccion == '0':
        for key in ['1', '2', '3', '4', '5']:
            ejemplos[key][1]()
            input("\n[Presione Enter para continuar...]")
    elif seleccion in ejemplos:
        if ejemplos[seleccion][1]:
            ejemplos[seleccion][1]()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    menu_ejemplos()
