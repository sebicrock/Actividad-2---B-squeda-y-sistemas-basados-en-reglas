"""
Pruebas Unitarias del Sistema de Rutas Inteligente
Verifica la correctitud de todos los componentes
"""

import unittest
from base_conocimiento import BaseConocimiento
from motor_inferencia import MotorInferencia
from sistema_rutas import SistemaRutas

class TestBaseConocimiento(unittest.TestCase):
    """Pruebas para la base de conocimiento"""
    
    def setUp(self):
        self.bc = BaseConocimiento()
    
    def test_estaciones_cargadas(self):
        """Verifica que las estaciones se cargan correctamente"""
        self.assertGreater(len(self.bc.estaciones), 0)
        self.assertIn('A_Centro', self.bc.estaciones)
    
    def test_lineas_cargadas(self):
        """Verifica que las líneas se cargan correctamente"""
        self.assertGreater(len(self.bc.lineas), 0)
        self.assertIn('Linea_Roja', self.bc.lineas)
    
    def test_agregar_estacion(self):
        """Verifica que se puede agregar una nueva estación"""
        self.bc.agregar_estacion('Test_Estacion', (10, 10))
        self.assertIn('Test_Estacion', self.bc.estaciones)
        self.assertEqual(self.bc.estaciones['Test_Estacion'], (10, 10))
    
    def test_agregar_linea(self):
        """Verifica que se puede agregar una nueva línea"""
        self.bc.agregar_linea('Linea_Test', ['A_Centro', 'B_Este'], 2, 2500)
        self.assertIn('Linea_Test', self.bc.lineas)
    
    def test_obtener_lineas_estacion(self):
        """Verifica obtención de líneas por estación"""
        lineas = self.bc.obtener_lineas_estacion('A_Centro')
        self.assertGreater(len(lineas), 0)
    
    def test_obtener_estaciones_conexas(self):
        """Verifica obtención de estaciones conexas"""
        conexas = self.bc.obtener_estaciones_conexas('A_Centro')
        self.assertIsInstance(conexas, list)
    
    def test_estaciones_proximas(self):
        """Verifica cálculo de proximidad entre estaciones"""
        resultado = self.bc._estaciones_proximas('A_Centro', 'C_Intermedia1', limite=5)
        self.assertIsInstance(resultado, bool)

class TestMotorInferencia(unittest.TestCase):
    """Pruebas para el motor de inferencia"""
    
    def setUp(self):
        self.bc = BaseConocimiento()
        self.motor = MotorInferencia(self.bc)
    
    def test_inferencia_completa(self):
        """Verifica que la inferencia se ejecuta sin errores"""
        try:
            self.motor.inferir()
            self.assertGreater(self.motor.ciclos_inferencia, 0)
        except Exception as e:
            self.fail(f"Inferencia falló con error: {e}")
    
    def test_derivar_conexiones(self):
        """Verifica que se derivan conexiones correctamente"""
        self.motor._aplicar_reglas()
        conexiones = self.bc.hechos_derivados['conexiones']
        self.assertGreater(len(conexiones), 0)
    
    def test_derivar_puntos_transferencia(self):
        """Verifica que se identifican puntos de transferencia"""
        self.motor._aplicar_reglas()
        transferencias = self.bc.hechos_derivados['puntos_transferencia']
        self.assertGreater(len(transferencias), 0)
    
    def test_no_ciclos_infinitos(self):
        """Verifica que la inferencia no entra en ciclo infinito"""
        self.motor.inferir()
        self.assertLessEqual(self.motor.ciclos_inferencia, self.motor.max_ciclos)

class TestSistemaRutas(unittest.TestCase):
    """Pruebas para el sistema de búsqueda de rutas"""
    
    def setUp(self):
        self.bc = BaseConocimiento()
        self.motor = MotorInferencia(self.bc)
        self.motor.inferir()
        self.sr = SistemaRutas(self.bc)
    
    def test_distancia_euclidiana(self):
        """Verifica el cálculo de distancia euclidiana"""
        distancia = self.sr._calcular_distancia_euclidiana('A_Centro', 'A_Norte')
        self.assertAlmostEqual(distancia, 5.0, places=1)
    
    def test_heuristica_tiempo(self):
        """Verifica que la heurística de tiempo es positiva"""
        h = self.sr._obtener_heuristica('A_Centro', 'B_Este', 'tiempo')
        self.assertGreaterEqual(h, 0)
    
    def test_heuristica_costo(self):
        """Verifica que la heurística de costo es positiva"""
        h = self.sr._obtener_heuristica('A_Centro', 'B_Este', 'costo')
        self.assertGreaterEqual(h, 0)
    
    def test_obtener_vecinos(self):
        """Verifica que se obtienen los vecinos correctamente"""
        vecinos = self.sr._obtener_vecinos('A_Centro')
        self.assertGreater(len(vecinos), 0)
    
    def test_buscar_ruta_valida(self):
        """Verifica búsqueda de ruta entre estaciones válidas"""
        resultado = self.sr.buscar_ruta_optima('A_Centro', 'B_Este', 'tiempo')
        self.assertNotIn('error', resultado)
        self.assertIn('ruta', resultado)
        self.assertEqual(resultado['ruta'][0], 'A_Centro')
        self.assertEqual(resultado['ruta'][-1], 'B_Este')
    
    def test_ruta_exitosa(self):
        """Verifica que la ruta sea exitosa"""
        resultado = self.sr.buscar_ruta_optima('A_Centro', 'B_Este', 'tiempo')
        self.assertTrue(resultado.get('exitosa', False))
    
    def test_buscar_ruta_estacion_invalida(self):
        """Verifica manejo de estación inexistente"""
        resultado = self.sr.buscar_ruta_optima('Inexistente', 'B_Este', 'tiempo')
        self.assertIn('error', resultado)
    
    def test_criterio_tiempo(self):
        """Verifica búsqueda optimizada por tiempo"""
        resultado = self.sr.buscar_ruta_optima('A_Centro', 'B_Este', 'tiempo')
        self.assertEqual(resultado['criterio_optimizado'], 'tiempo')
        self.assertIn('tiempo_total', resultado)
    
    def test_criterio_costo(self):
        """Verifica búsqueda optimizada por costo"""
        resultado = self.sr.buscar_ruta_optima('A_Centro', 'B_Este', 'costo')
        self.assertEqual(resultado['criterio_optimizado'], 'costo')
        self.assertIn('costo_total', resultado)
    
    def test_criterio_distancia(self):
        """Verifica búsqueda optimizada por distancia"""
        resultado = self.sr.buscar_ruta_optima('A_Centro', 'B_Este', 'distancia')
        self.assertEqual(resultado['criterio_optimizado'], 'distancia')
        self.assertIn('distancia_total', resultado)
    
    def test_metricas_ruta(self):
        """Verifica que las métricas se calculan correctamente"""
        resultado = self.sr.buscar_ruta_optima('A_Centro', 'C_Intermedia1', 'tiempo')
        
        self.assertIsInstance(resultado['ruta'], list)
        self.assertIsInstance(resultado['pasos'], list)
        self.assertGreater(resultado['tiempo_total'], 0)
        self.assertGreater(resultado['costo_total'], 0)
        self.assertGreater(resultado['distancia_total'], 0)
        self.assertGreater(len(resultado['lineas_utilizadas']), 0)
    
    def test_ruta_mismo_origen_destino(self):
        """Verifica ruta cuando origen y destino son iguales"""
        resultado = self.sr.buscar_ruta_optima('A_Centro', 'A_Centro', 'tiempo')
        # Debería retornar ruta con mismo punto o error
        if 'exitosa' in resultado:
            self.assertEqual(len(resultado['ruta']), 1)
    
    def test_transferencias_contadas(self):
        """Verifica que las transferencias se cuentan correctamente"""
        resultado = self.sr.buscar_ruta_optima('A_Norte', 'D_Conexion', 'tiempo')
        if 'exitosa' in resultado:
            self.assertGreaterEqual(resultado['transferencias'], 0)

class TestIntegracion(unittest.TestCase):
    """Pruebas de integración del sistema completo"""
    
    def setUp(self):
        self.bc = BaseConocimiento()
        self.motor = MotorInferencia(self.bc)
        self.motor.inferir()
        self.sr = SistemaRutas(self.bc)
    
    def test_flujo_completo(self):
        """Verifica el flujo completo del sistema"""
        # Base de conocimiento
        self.assertGreater(len(self.bc.estaciones), 0)
        
        # Inferencia
        self.assertGreater(len(self.bc.hechos_derivados['conexiones']), 0)
        
        # Búsqueda de rutas
        resultado = self.sr.buscar_ruta_optima('A_Centro', 'B_Este', 'tiempo')
        self.assertNotIn('error', resultado)
    
    def test_multiple_criterios(self):
        """Verifica búsqueda con múltiples criterios"""
        criterios = ['tiempo', 'costo', 'distancia']
        resultados = {}
        
        for criterio in criterios:
            resultado = self.sr.buscar_ruta_optima('A_Centro', 'B_Este', criterio)
            resultados[criterio] = resultado
            self.assertNotIn('error', resultado)
        
        # Las rutas pueden ser diferentes según criterio
        tiempo_ruta = resultados['tiempo']['ruta']
        costo_ruta = resultados['costo']['ruta']
        # No necesariamente deben ser diferentes, pero podrían
        self.assertIsInstance(tiempo_ruta, list)
        self.assertIsInstance(costo_ruta, list)

def run_tests():
    """Ejecuta todas las pruebas"""
    
    print("\n" + "="*70)
    print("EJECUTANDO PRUEBAS UNITARIAS DEL SISTEMA DE RUTAS")
    print("="*70 + "\n")
    
    # Crear suite de pruebas
    suite = unittest.TestSuite()
    
    # Agregar pruebas
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBaseConocimiento))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMotorInferencia))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSistemaRutas))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestIntegracion))
    
    # Ejecutar
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Resumen
    print("\n" + "="*70)
    print("RESUMEN DE PRUEBAS")
    print("="*70)
    print(f"Pruebas ejecutadas: {resultado.testsRun}")
    print(f"Éxitos: {resultado.testsRun - len(resultado.failures) - len(resultado.errors)}")
    print(f"Fallos: {len(resultado.failures)}")
    print(f"Errores: {len(resultado.errors)}")
    print("="*70 + "\n")
    
    return resultado.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
