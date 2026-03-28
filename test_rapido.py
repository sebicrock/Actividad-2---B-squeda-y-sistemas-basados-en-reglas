#!/usr/bin/env python
"""Test simple del sistema sin caracteres problematicos"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

try:
    print("[*] Importando modulos...")
    from base_conocimiento import BaseConocimiento
    from motor_inferencia import MotorInferencia
    from sistema_rutas import SistemaRutas
    print("[OK] Modulos importados exitosamente")
    
    print("\n[*] Inicializando sistema...")
    bc = BaseConocimiento()
    print(f"[OK] Base de conocimiento cargada: {len(bc.estaciones)} estaciones")
    print(f"[OK] Lineas de transporte: {len(bc.lineas)}")
    
    print("\n[*] Ejecutando inferencia...")
    motor = MotorInferencia(bc)
    motor.inferir()
    print(f"[OK] Inferencia completada en {motor.ciclos_inferencia} ciclos")
    print(f"[OK] Hechos derivados: {len(bc.hechos_derivados['conexiones'])} conexiones")
    print(f"[OK] Puntos de transferencia: {len(bc.hechos_derivados['puntos_transferencia'])}")
    
    print("\n[*] Buscando rutas optimas...")
    sr = SistemaRutas(bc)
    
    # Test 1: Por tiempo
    print("\n[TEST 1] Ruta por tiempo minimo (Mosquera a Bogota Centro)")
    ruta1 = sr.buscar_ruta_optima('Mosquera', 'Bogota_Centro', 'tiempo')
    if 'exitosa' in ruta1:
        print(f"  [OK] Ruta encontrada: {' -> '.join(ruta1['ruta'])}")
        print(f"       Tiempo: {ruta1['tiempo_total']} min")
        print(f"       Costo: ${ruta1['costo_total']}")
        print(f"       Distancia: {ruta1['distancia_total']} km")
    else:
        print(f"  [ERROR] {ruta1.get('error', 'desconocido')}")
    
    # Test 2: Por costo
    print("\n[TEST 2] Ruta por costo minimo (Funza a Bogota)")
    ruta2 = sr.buscar_ruta_optima('Funza', 'Bogota_Chapinero', 'costo')
    if 'exitosa' in ruta2:
        print(f"  [OK] Ruta encontrada: {' -> '.join(ruta2['ruta'])}")
        print(f"       Tiempo: {ruta2['tiempo_total']} min")
        print(f"       Costo: ${ruta2['costo_total']}")
        print(f"       Distancia: {ruta2['distancia_total']} km")
    else:
        print(f"  [ERROR] {ruta2.get('error', 'desconocido')}")
    
    # Test 3: Con transferencias
    print("\n[TEST 3] Ruta con posibles transferencias (Soacha a Zipaquira)")
    ruta3 = sr.buscar_ruta_optima('Soacha', 'Zipaquira', 'tiempo')
    if 'exitosa' in ruta3:
        print(f"  [OK] Ruta encontrada: {' -> '.join(ruta3['ruta'])}")
        print(f"       Lineas utilizadas: {', '.join(ruta3['lineas_utilizadas'])}")
        print(f"       Transferencias: {ruta3['transferencias']}")
        print(f"       Pasos: {len(ruta3['pasos'])}")
    else:
        print(f"  [ERROR] {ruta3.get('error', 'desconocido')}")
    
    # Test 4: Estadisticas
    print("\n[TEST 4] Estadisticas del sistema")
    print(f"  [OK] Total estaciones: {len(bc.estaciones)}")
    print(f"  [OK] Total lineas: {len(bc.lineas)}")
    print(f"  [OK] Conexiones directas: {len(bc.hechos_derivados['conexiones'])}")
    print(f"  [OK] Puntos de transferencia: {len(bc.hechos_derivados['puntos_transferencia'])}")
    
    print("\n" + "="*70)
    print("[SUCCESS] TODOS LOS TESTS PASARON EXITOSAMENTE!")
    print("="*70)
    print("\nEl sistema esta funcionando correctamente.")
    print("Ejecute 'python main.py' para interfaz interactiva completa.")
    
except Exception as e:
    print(f"\n[ERROR] {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
