# 🚌 ÍNDICE DEL PROYECTO - Sistema Inteligente de Rutas de Transporte

## 📁 Estructura General

Este proyecto implementa un **sistema inteligente de búsqueda de rutas** para transporte masivo usando:
- 🧠 **Reglas Lógicas** (Base de Conocimiento)
- 🔄 **Forward Chaining** (Inferencia Automática)
- 🔍 **Algoritmo A*** (Búsqueda Óptima)

---

## 📑 Archivos y Su Propósito

### 🚀 **Punto de Entrada**

#### `main.py` ⭐ *COMENZAR AQUÍ*
- **Qué hace**: Programa principal que integra todo el sistema
- **Características**:
  - Carga la base de conocimiento
  - Ejecuta el motor de inferencia
  - Muestra ejemplos automáticos
  - Proporciona menú interactivo
- **Cómo ejecutar**: `python main.py`
- **Tiempo estimado**: 2-3 minutos

#### `herramientas.py`
- **Qué hace**: Menú centralizado con todas las opciones
- **Características**:
  - Acceso a todos los programas
  - Modo demostración rápido
  - Estadísticas del sistema
- **Cómo ejecutar**: `python herramientas.py`
- **Ideal para**: Usuarios nuevos

---

### 🧠 **Componentes Principales**

#### `base_conocimiento.py`
- **Qué hace**: Almacena hechos y reglas sobre el transporte
- **Características principales**:
  - Almacena estaciones con coordenadas
  - Define líneas de transporte
  - Implementa 3 reglas lógicas:
    1. Conectividad directa
    2. Proximidad geográfica
    3. Puntos de transferencia
  - Métodos para agregar datos dinámicamente
- **Uso típico**:
  ```python
  from base_conocimiento import BaseConocimiento
  bc = BaseConocimiento()
  bc.agregar_estacion('Nueva', (5, 5))
  ```

#### `motor_inferencia.py`
- **Qué hace**: Aplica reglas lógicas mediante forward chaining
- **Características principales**:
  - Ejecuta ciclos de inferencia
  - Genera nuevos hechos automáticamente
  - Identifica conexiones y transferencias
  - Detecta fin de inferencia
- **Uso típico**:
  ```python
  from motor_inferencia import MotorInferencia
  motor = MotorInferencia(bc)
  motor.inferir()
  print(bc.hechos_derivados)
  ```

#### `sistema_rutas.py`
- **Qué hace**: Busca rutas óptimas usando algoritmo A*
- **Características principales**:
  - Algoritmo A* completo
  - 3 criterios de optimización: tiempo, costo, distancia
  - Cálculo de heurística admisible (euclidiana)
  - Análisis completo de rutas con métricas
  - Comparación entre criterios
- **Uso típico**:
  ```python
  from sistema_rutas import SistemaRutas
  sr = SistemaRutas(bc)
  ruta = sr.buscar_ruta_optima('A', 'B', 'tiempo')
  ```

---

### 📚 **Documentación**

#### `README.md` 📖
- **Contenido**:
  - Descripción completa del sistema
  - Arquitectura y componentes
  - Explicación de algoritmo A*
  - Reglas lógicas detalladas
  - Ejemplos de uso
  - Análisis de complejidad
- **Cuándo leer**: Para entender cómo funciona todo

#### `CONFIGURACION.md` ⚙️
- **Contenido**:
  - Requisitos del sistema
  - Pasos de instalación
  - Cómo ejecutar cada programa
  - Configuración personalizada
  - Solución de problemas
  - Optimización de rendimiento
- **Cuándo leer**: Para instalar y configurar

#### `INDICE.md` (este archivo)
- **Contenido**: Guía de navegación del proyecto
- **Cuándo leer**: Como primer paso

---

### 💡 **Ejemplos y Pruebas**

#### `ejemplos_avanzados.py`
- **Qué hace**: Demuestra casos de uso complejos
- **Ejemplos incluidos**:
  1. Expansión del sistema
  2. Análisis de puntos críticos
  3. Análisis costo-beneficio
  4. Análisis de grafos
  5. Simulación de viaje interactivo
- **Cómo ejecutar**: `python ejemplos_avanzados.py`
- **Ideal para**: Aprender casos avanzados

#### `test_sistema.py`
- **Qué hace**: Pruebas unitarias exhaustivas
- **Cobertura**:
  - Pruebas de base de conocimiento (7 tests)
  - Pruebas de motor de inferencia (4 tests)
  - Pruebas de búsqueda de rutas (11 tests)
  - Pruebas de integración (3 tests)
  - Total: 25+ pruebas
- **Cómo ejecutar**: `python test_sistema.py`
- **Ideal para**: Validar funcionamiento

---

## 🎯 Guías de Inicio Según Tu Objetivo

### ✅ Apenas empiezas
1. Lee **INDICE.md** (este archivo) - 5 min
2. Lee **README.md** - 10 min
3. Ejecuta `python main.py` - 5 min
4. ¡Listo! Ya entienden el sistema

### 🔧 Quieres personalizar
1. Lee **CONFIGURACION.md**
2. Modifica `base_conocimiento.py`
3. Agrega nuevas estaciones y líneas
4. Ejecuta nuevamente

### 📊 Quieres ver ejemplos avanzados
1. Ejecuta `python ejemplos_avanzados.py`
2. Explora los 5 ejemplos
3. Entiende patrones de uso
4. ¡Adapta para tu caso!

### 🧪 Quieres validar funcionamiento
1. Ejecuta `python test_sistema.py`
2. Verifica que todas las pruebas pasen
3. Revisa el código de pruebas
4. Ahora sí confía en el código

### 💻 Quieres integrar en tu código
1. Lee la sección de uso programático en **README.md**
2. Importa los módulos necesarios
3. Crea tu instancia de BaseConocimiento
4. ¡Úsalo como librería Python!

### 🚀 Quieres modo fácil
1. Ejecuta `python herramientas.py`
2. Elige opción del menú
3. ¡Sin necesidad de terminal!

---

## 📊 Mapa de Dependencias

```
main.py
├── base_conocimiento.py ✓
├── motor_inferencia.py
│   └── base_conocimiento.py ✓
└── sistema_rutas.py
    └── base_conocimiento.py ✓

ejemplos_avanzados.py
├── base_conocimiento.py ✓
├── motor_inferencia.py ✓
└── sistema_rutas.py ✓

test_sistema.py
├── base_conocimiento.py ✓
├── motor_inferencia.py ✓
└── sistema_rutas.py ✓

herramientas.py (independiente, llama otros .py)
```

---

## 🔍 Referencia Rápida de Funciones

### BaseConocimiento
| Función | Parámetros | Retorna |
|---------|-----------|---------|
| `agregar_estacion()` | nombre, (x,y) | void |
| `agregar_linea()` | nombre, [estaciones], tiempo, costo | void |
| `obtener_lineas_estacion()` | nombre | list |
| `obtener_estaciones_conexas()` | nombre | list |

### MotorInferencia
| Función | Parámetros | Retorna |
|---------|-----------|---------|
| `inferir()` | - | void |
| `consultar_hecho()` | condicion | bool |
| `obtener_especializacion()` | concepto | list |

### SistemaRutas
| Función | Parámetros | Retorna |
|---------|-----------|---------|
| `buscar_ruta_optima()` | origen, destino, criterio | dict |
| `comparar_rutas()` | origen, destino | dict |
| `_mostrar_ruta()` | dict, criterio | void |

---

## 📈 Línea de Complejidad

```
Fácil          Intermedio         Avanzado
 ↓               ↓                  ↓
main.py → ejemplos_avanzados.py → Modificar sistema_rutas.py
           → test_sistema.py      → Agregar nuevas reglas
           → herramientas.py      → Integrar con APIs
```

---

## 🎓 Conceptos Clave

### 🧠 Reglas Lógicas
- Se aplican automáticamente mediante forward chaining
- Generan nuevos hechos sin necesidad de consultas
- Son declarativas, no procedurales

### 🔍 Algoritmo A*
- Garantiza encontrar la ruta más corta/barata/rápida
- Combina costo real con heurística estimada
- Más eficiente que Dijkstra

### 🚌 Sistema de Transporte
- Estaciones: puntos geográficos
- Líneas: rutas que conectan estaciones
- Transfers: cambio de línea en misma estación

---

## 💡 Consejos Útiles

✅ **HACER**:
- Comenzar por `main.py` para entender flujo
- Leer README.md para conceptos
- Ejecutar ejemplos_avanzados.py para ver casos
- Usar test_sistema.py para validar cambios
- Consultar esta documentación cuando dudes

❌ **NO HACER**:
- Modificar algoritmo A* sin entender bien
- Cambiar reglas sin ejecutar pruebas
- Agregar muchas estaciones sin optimizar
- Ignorar errores de tipo
- Copiar código sin entender

---

## 🐛 Troubleshooting Común

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError` | Archivos no en mismo folder | Verify archivos juntos |
| "No route found" | Estaciones desconectadas | Use `obtener_estaciones_conexas()` |
| Inferencia lenta | Muchas estaciones | Reduce `max_ciclos` |
| Tipo incorrecto | Parámetro erróneo | Verifica con `print()` |

---

## 📞 ¿Necesitas ayuda?

1. **Pregunta sobre qué hace algo**: Mira este INDICE.md
2. **Quieres entender algoritmo**: Lee README.md
3. **Quieres instalar**: Lee CONFIGURACION.md
4. **Quieres ver ejemplos**: Ejecuta ejemplos_avanzados.py
5. **Quieres validar**: Ejecuta test_sistema.py
6. **Quieres código limpio**: Lee test_sistema.py

---

## 🎉 ¡Bienvenido!

Ahora que conoces la estructura, elige tu camino:

- 👶 **Principiante**: `python main.py`
- 🎓 **Estudiante**: Lee README.md + ejecuta ejemplos
- 👨‍💻 **Desarrollador**: Integra en tu código
- 🔬 **Investigador**: Modifica algoritmos y reglas

**¡Que disfrutes explorando el sistema! 🚀**

---

*Última actualización: 2026-03-28*  
*Sistema de Rutas Inteligente - Versión 1.0*
