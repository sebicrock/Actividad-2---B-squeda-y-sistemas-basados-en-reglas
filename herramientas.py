"""
Utilidades y Herramientas para el Sistema de Rutas
Scripts auxiliares para facilitar el uso
"""

import os
import sys

class HerramientasUtiles:
    """Colección de herramientas útiles para el sistema"""
    
    @staticmethod
    def limpiar_pantalla():
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def mostrar_banner():
        """Muestra el banner del sistema"""
        banner = """
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║     🚌 SISTEMA INTELIGENTE DE RUTAS DE TRANSPORTE MASIVO 🚌       ║
║                                                                    ║
║  Desarrollado con:                                                 ║
║  • Base de Conocimiento (Reglas Lógicas)                          ║
║  • Motor de Inferencia (Forward Chaining)                         ║
║  • Algoritmo A* (Búsqueda Óptima de Rutas)                        ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    @staticmethod
    def mostrar_menu_principal():
        """Muestra el menú principal"""
        menu = """
╔════════════════════════════════════════════════════════════════════╗
║                      MENÚ PRINCIPAL                               ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  1. 🚀 Ejecutar programa principal (main.py)                      ║
║  2. 💡 Ver ejemplos avanzados (ejemplos_avanzados.py)             ║
║  3. ✅ Ejecutar pruebas (test_sistema.py)                         ║
║  4. 📖 Ver documentación (README.md)                              ║
║  5. ⚙️  Ver configuración (CONFIGURACION.md)                      ║
║  6. 📚 Ver guía de desarrollo                                     ║
║  7. 🔄 Ejecutar modo demostración                                 ║
║  8. ❌ Salir                                                       ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
        """
        print(menu)
    
    @staticmethod
    def ejecutar_demo():
        """Ejecuta una demostración rápida del sistema"""
        from base_conocimiento import BaseConocimiento
        from motor_inferencia import MotorInferencia
        from sistema_rutas import SistemaRutas
        
        print("\n" + "="*70)
        print("MODO DEMOSTRACIÓN - SISTEMA DE RUTAS INTELIGENTE")
        print("="*70 + "\n")
        
        try:
            # Carregar BC
            print("⏳ Inicializando sistema...")
            bc = BaseConocimiento()
            motor = MotorInferencia(bc)
            motor.inferir()
            sr = SistemaRutas(bc)
            print("✓ Sistema inicializado\n")
            
            # Demo 1
            print("📍 Demo 1: Ruta más rápida")
            print("-" * 70)
            ruta1 = sr.buscar_ruta_optima('A_Centro', 'B_Este', 'tiempo')
            sr._mostrar_ruta(ruta1, 'tiempo')
            
            input("\n[Presione Enter para continuar...]")
            
            # Demo 2
            print("\n📍 Demo 2: Ruta más económica")
            print("-" * 70)
            ruta2 = sr.buscar_ruta_optima('A_Sur', 'B_Este', 'costo')
            sr._mostrar_ruta(ruta2, 'costo')
            
            input("\n[Presione Enter para continuar...]")
            
            # Demo 3
            print("\n📍 Demo 3: Estadísticas del sistema")
            print("-" * 70)
            print(f"Total estaciones: {len(bc.estaciones)}")
            print(f"Total líneas: {len(bc.lineas)}")
            print(f"Conexiones: {len(bc.hechos_derivados['conexiones'])}")
            print(f"Puntos de transferencia: {len(bc.hechos_derivados['puntos_transferencia'])}")
            
            print("\n✓ Demostración completada")
            
        except Exception as e:
            print(f"❌ Error en demostración: {e}")
    
    @staticmethod
    def mostrar_estadisticas_sistema():
        """Muestra estadísticas del sistema"""
        from base_conocimiento import BaseConocimiento
        from motor_inferencia import MotorInferencia
        
        print("\n" + "="*70)
        print("ESTADÍSTICAS DEL SISTEMA")
        print("="*70 + "\n")
        
        bc = BaseConocimiento()
        motor = MotorInferencia(bc)
        
        print("📊 Componentes cargados:")
        print(f"  • Estaciones: {len(bc.estaciones)}")
        print(f"  • Líneas: {len(bc.lineas)}")
        print(f"  • Reglas lógicas: {len(bc.reglas)}")
        
        print("\n🔄 Ejecutando inferencia...")
        motor.inferir()
        
        print("\n📈 Hechos derivados:")
        print(f"  • Conexiones directas: {len(bc.hechos_derivados['conexiones'])}")
        print(f"  • Puntos de transferencia: {len(bc.hechos_derivados['puntos_transferencia'])}")
        print(f"  • Alternativas identificadas: {sum(len(v) for v in bc.hechos_derivados['alternativas'].values())}")
        
        print("\n⏱️  Ciclos de inferencia: {motor.ciclos_inferencia}")
    
    @staticmethod
    def mostrar_guia_desarrollo():
        """Muestra guía de desarrollo"""
        guia = """
╔════════════════════════════════════════════════════════════════════╗
║              GUÍA DE DESARROLLO - EXTENSIONES                     ║
╚════════════════════════════════════════════════════════════════════╝

1. AGREGAR NUEVA REGLA LÓGICA
──────────────────────────────────────────────────────────────────
En base_conocimiento.py, agregue a la lista de reglas:

    {
        'nombre': 'nombre_regla',
        'descripcion': 'Descripción de la regla',
        'condicion': self._mi_condicion,
        'consecuencia': self._mi_consecuencia
    }

Luego defina los métodos condición y consecuencia.

2. PERSONALIZAR HEURÍSTICA A*
──────────────────────────────────────────────────────────────────
En sistema_rutas.py, modifique _obtener_heuristica():

    def _obtener_heuristica(self, actual, destino, criterio):
        # Su lógica personalizada aquí
        return valor_heuristica

3. AGREGAR NUEVO CRITERIO DE OPTIMIZACIÓN
──────────────────────────────────────────────────────────────────
En sistema_rutas.py, buscar_ruta_optima():

    elif criterio == 'mi_criterio':
        costo_movimiento = calcular_costo_especial(...)

4. INTEGRAR CON API REST
──────────────────────────────────────────────────────────────────
from flask import Flask, jsonify, request
from sistema_rutas import SistemaRutas

app = Flask(__name__)
sr = SistemaRutas(base_conocimiento)

@app.route('/ruta', methods=['POST'])
def get_ruta():
    data = request.json
    ruta = sr.buscar_ruta_optima(...)
    return jsonify(ruta)

5. AGREGAR BASE DE DATOS
──────────────────────────────────────────────────────────────────
import sqlite3

conn = sqlite3.connect('transporte.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE estaciones
                 (id INTEGER PRIMARY KEY, nombre TEXT)''')

6. VISUALIZAR RUTAS
──────────────────────────────────────────────────────────────────
import matplotlib.pyplot as plt

for estacion in ruta['ruta']:
    coords = bc.estaciones[estacion]
    plt.plot(coords[0], coords[1], 'o')

7. ANÁLISIS DE COMPLEJIDAD
──────────────────────────────────────────────────────────────────
• Espacio: O(V + E)
• Búsqueda A*: O((V + E) log V)
• Inferencia: O(n²) peor caso

8. TESTING DE NUEVAS FEATURES
──────────────────────────────────────────────────────────────────
import unittest

class TestMiFeature(unittest.TestCase):
    def test_algo(self):
        resultado = mi_funcion()
        self.assertIsNotNone(resultado)

Ejecutar con: python -m unittest

╚════════════════════════════════════════════════════════════════════╝
        """
        print(guia)

def menu_principal():
    """Menú principal del programa"""
    
    HerramientasUtiles.mostrar_banner()
    
    while True:
        HerramientasUtiles.mostrar_menu_principal()
        
        opcion = input("Seleccione opción (1-8): ").strip()
        
        if opcion == '1':
            print("\n⏳ Iniciando programa principal...\n")
            os.system('python main.py')
        
        elif opcion == '2':
            print("\n⏳ Iniciando ejemplos avanzados...\n")
            os.system('python ejemplos_avanzados.py')
        
        elif opcion == '3':
            print("\n⏳ Ejecutando pruebas...\n")
            os.system('python test_sistema.py')
        
        elif opcion == '4':
            print("\n📖 Abriendo documentación (README.md)")
            if os.path.exists('README.md'):
                os.system('notepad README.md' if os.name == 'nt' else 'cat README.md | less')
            else:
                print("❌ Archivo README.md no encontrado")
        
        elif opcion == '5':
            print("\n⚙️  Abriendo configuración (CONFIGURACION.md)")
            if os.path.exists('CONFIGURACION.md'):
                os.system('notepad CONFIGURACION.md' if os.name == 'nt' else 'cat CONFIGURACION.md | less')
            else:
                print("❌ Archivo CONFIGURACION.md no encontrado")
        
        elif opcion == '6':
            HerramientasUtiles.mostrar_guia_desarrollo()
        
        elif opcion == '7':
            try:
                HerramientasUtiles.ejecutar_demo()
            except Exception as e:
                print(f"❌ Error en demostración: {e}")
        
        elif opcion == '8':
            print("\n✓ Gracias por usar el Sistema de Rutas");
            print("¡Hasta luego! 👋\n")
            break
        
        else:
            print("❌ Opción no válida. Intente de nuevo.")
        
        input("\n[Presione Enter para continuar...]")
        HerramientasUtiles.limpiar_pantalla()

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
