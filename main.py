"""
Sistema Inteligente de Rutas de Transporte Masivo
Integra la base de conocimiento, motor de inferencia y búsqueda de rutas
"""

from base_conocimiento import BaseConocimiento
from motor_inferencia import MotorInferencia
from sistema_rutas import SistemaRutas

def mostrar_introduccion():
    """Muestra la introducción del programa"""
    print("\n" + "="*70)
    print("SISTEMA INTELIGENTE DE RUTAS DE TRANSPORTE MASIVO")
    print("="*70)
    print("\n📍 ¿QUÉ ES ESTE SISTEMA?")
    print("-" * 70)
    print("""
Este sistema busca rutas óptimas en la red de transporte de Bogotá y alrededores.
Utiliza un motor de inferencia con reglas lógicas para encontrar la mejor ruta
según tu criterio: tiempo, costo o distancia.

CARACTERÍSTICAS:
  • Inteligencia Artificial: Motor A* para búsqueda óptima
  • 12 estaciones conectadas en 5 líneas de transporte
  • Detección automática de puntos de transferencia
  • Optimización por 3 criterios (tiempo, costo, distancia)
  • Sistema de inferencia con razonamiento lógico
""")

def menu_principal():
    """Menú principal para elegir qué hacer"""
    print("\n¿QUÉ DESEAS HACER?")
    print("-" * 70)
    print("  1. Ver ejemplos de búsqueda de rutas (demostraciones)")
    print("  2. Ir directamente al menú interactivo")
    print("  3. Ver estadísticas del sistema")
    print("  4. Salir")
    
    while True:
        try:
            opcion = int(input("\nSelecciona opción (1-4): ").strip())
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("[ERROR] Ingresa un número entre 1 y 4")
        except ValueError:
            print("[ERROR] Ingresa un número válido")

def inicializar_sistema():
    """Inicializa silenciosamente el sistema sin mostrar detalles"""
    base_conocimiento = BaseConocimiento()
    motor_inferencia = MotorInferencia(base_conocimiento)
    motor_inferencia.inferir()
    sistema_rutas = SistemaRutas(base_conocimiento)
    return base_conocimiento, motor_inferencia, sistema_rutas

def mostrar_ejemplos(base_conocimiento, sistema_rutas):
    """Muestra ejemplos de búsqueda de rutas"""
    print("\n[DEMOSTRACIONES] EJEMPLOS DE BÚSQUEDA DE RUTAS")
    print("="*70)
    
    # Ejemplo 1: Minimizar tiempo
    print("\n[EJEMPLO 1] Buscar ruta con MINIMO TIEMPO")
    print("-" * 70)
    ruta_rapida = sistema_rutas.buscar_ruta_optima('Mosquera', 'Bogota_Centro', criterio='tiempo')
    sistema_rutas._mostrar_ruta(ruta_rapida, 'tiempo')
    
    # Ejemplo 2: Minimizar costo
    print("\n[EJEMPLO 2] Buscar ruta con MINIMO COSTO")
    print("-" * 70)
    ruta_economica = sistema_rutas.buscar_ruta_optima('Funza', 'Bogota_Chapinero', criterio='costo')
    sistema_rutas._mostrar_ruta(ruta_economica, 'costo')
    
    # Ejemplo 3: Minimizar distancia
    print("\n[EJEMPLO 3] Buscar ruta con MINIMA DISTANCIA")
    print("-" * 70)
    ruta_corta = sistema_rutas.buscar_ruta_optima('Soacha', 'Bogota_Centro', criterio='distancia')
    sistema_rutas._mostrar_ruta(ruta_corta, 'distancia')

def mostrar_estadisticas(base_conocimiento, motor_inferencia):
    """Muestra estadísticas del sistema"""
    print("\n[ESTADÍSTICAS] DEL SISTEMA")
    print("="*70)
    
    print(f"\nTotal de estaciones: {len(base_conocimiento.estaciones)}")
    print(f"Total de líneas: {len(base_conocimiento.lineas)}")
    
    print("\nLíneas de transporte:")
    for nombre_linea, linea in base_conocimiento.lineas.items():
        print(f"  • {nombre_linea}: {' → '.join(linea['estaciones'])}")
    
    print(f"\nTotal de conexiones directas: {len(base_conocimiento.hechos_derivados['conexiones'])}")
    print(f"Puntos de transferencia: {len(base_conocimiento.hechos_derivados['puntos_transferencia'])}")
    print(f"Ciclos de inferencia: {motor_inferencia.ciclos_inferencia}")
    
    print("\nPuntos de transferencia estratégicos:")
    for punto in base_conocimiento.hechos_derivados['puntos_transferencia']:
        lineas = base_conocimiento.obtener_lineas_estacion(punto)
        print(f"  • {punto}: {', '.join(lineas)}")

def main():
    """Función principal que ejecuta el sistema completo"""
    
    mostrar_introduccion()
    
    print("\n⚙️ Inicializando sistema...")
    base_conocimiento, motor_inferencia, sistema_rutas = inicializar_sistema()
    print("[OK] Sistema listo!\n")
    
    while True:
        opcion = menu_principal()
        
        if opcion == 1:
            mostrar_ejemplos(base_conocimiento, sistema_rutas)
        
        elif opcion == 2:
            menu_interactivo(base_conocimiento, sistema_rutas)
            break
        
        elif opcion == 3:
            mostrar_estadisticas(base_conocimiento, motor_inferencia)
        
        elif opcion == 4:
            print("\n[OK] ¡Gracias por usar el sistema! Hasta luego.")
            break

def seleccionar_estacion(base_conocimiento, mensaje=""):
    """Muestra lista de estaciones y permite seleccionar por número"""
    estaciones = sorted(list(base_conocimiento.estaciones.keys()))
    
    if mensaje:
        print(f"\n{mensaje}")
    
    print("\nEstaciones disponibles:")
    for i, estacion in enumerate(estaciones, 1):
        print(f"  {i}. {estacion}")
    
    while True:
        try:
            opcion = int(input("\nSeleccione número: ").strip())
            if 1 <= opcion <= len(estaciones):
                return estaciones[opcion - 1]
            else:
                print(f"[ERROR] Ingrese un número entre 1 y {len(estaciones)}")
        except ValueError:
            print("[ERROR] Ingrese un número válido")

def seleccionar_criterio():
    """Muestra opciones de criterio y permite seleccionar por número"""
    criterios = ['tiempo', 'costo', 'distancia']
    
    print("\nCriterios disponibles:")
    print("  1. Tiempo mínimo")
    print("  2. Costo mínimo")
    print("  3. Distancia mínima")
    
    while True:
        try:
            opcion = int(input("\nSeleccione criterio (1-3): ").strip())
            if 1 <= opcion <= len(criterios):
                return criterios[opcion - 1]
            else:
                print(f"[ERROR] Ingrese un número entre 1 y {len(criterios)}")
        except ValueError:
            print("[ERROR] Ingrese un número válido")

def menu_interactivo(base_conocimiento, sistema_rutas):
    """Menu interactivo para crear nuevas consultas"""
    
    print("\n[7] MENU INTERACTIVO")
    print("="*70)
    
    while True:
        print("\nOpciones:")
        print("  1. Buscar ruta optimizada (por tiempo, costo o distancia)")
        print("  2. Comparar rutas (todos los criterios)")
        print("  3. Ver información de estación")
        print("  4. Salir")
        
        opcion = input("\nSeleccione opción (1-4): ").strip()
        
        if opcion == '1':
            origen = seleccionar_estacion(base_conocimiento, "Seleccione ESTACION ORIGEN:")
            destino = seleccionar_estacion(base_conocimiento, "Seleccione ESTACION DESTINO:")
            criterio = seleccionar_criterio()
            
            resultado = sistema_rutas.buscar_ruta_optima(origen, destino, criterio)
            sistema_rutas._mostrar_ruta(resultado, criterio)
        
        elif opcion == '2':
            origen = seleccionar_estacion(base_conocimiento, "Seleccione ESTACION ORIGEN:")
            destino = seleccionar_estacion(base_conocimiento, "Seleccione ESTACION DESTINO:")
            sistema_rutas.comparar_rutas(origen, destino)
        
        elif opcion == '3':
            estacion = seleccionar_estacion(base_conocimiento, "Seleccione ESTACION:")
            coords = base_conocimiento.estaciones[estacion]
            lineas = base_conocimiento.obtener_lineas_estacion(estacion)
            conexas = base_conocimiento.obtener_estaciones_conexas(estacion)
            
            print(f"\n{'='*70}")
            print(f"[PUNTO] Información de {estacion}:")
            print(f"{'='*70}")
            print(f"   Coordenadas: {coords}")
            print(f"   Líneas que pasan: {', '.join(lineas)}")
            print(f"   Estaciones conexas: {', '.join(conexas)}")
        
        elif opcion == '4':
            print("\n[OK] Sistema finalizado. ¡Gracias por usar el servicio!")
            break
        
        else:
            print("[ERROR] Opción no válida")

if __name__ == "__main__":
    main()
