# Sistema Inteligente de Rutas de Transporte Masivo

## 📋 Descripción General

Sistema inteligente desarrollado en Python que utiliza **reglas lógicas** y **algoritmos de búsqueda** para encontrar la mejor ruta de transporte masivo entre dos puntos (A y B), optimizando según diferentes criterios como tiempo, costo y distancia.

## 🏗️ Arquitectura del Sistema

El sistema está compuesto por tres componentes principales:

### 1. **Base de Conocimiento** (`base_conocimiento.py`)
Almacena y gestiona:
- **Estaciones de transporte**: Ubicación geográfica (coordenadas X, Y)
- **Líneas de transporte**: Estaciones que conectan, tiempo de viaje, costo
- **Reglas lógicas**:
  - Conectividad directa entre estaciones de la misma línea
  - Proximidad geográfica entre estaciones
  - Identificación de puntos de transferencia

#### Estructura de datos:

```python
estaciones = {
    'nombre_estacion': (x, y),  # Coordenadas
    ...
}

lineas = {
    'nombre_linea': {
        'estaciones': ['est1', 'est2', 'est3'],
        'tiempo_viaje': 2,  # minutos por tramo
        'costo': 2500  # pesos por tramo
    },
    ...
}
```

### 2. **Motor de Inferencia** (`motor_inferencia.py`)
Implementa **Forward Chaining** para:
- Aplicar reglas lógicas iterativamente
- Derivar nuevos hechos de los existentes
- Identificar conexiones y puntos de transferencia
- Generar relaciones de alternancia entre estaciones

#### Reglas implementadas:

1. **Conectividad Directa**: Si dos estaciones están en la misma línea, están directamente conectadas
2. **Proximidad Geográfica**: Si dos estaciones están cercanas, son alternativas viables
3. **Puntos de Transferencia**: Estaciones donde se pueden cambiar de línea

### 3. **Sistema de Búsqueda de Rutas** (`sistema_rutas.py`)
Utiliza el **algoritmo A*** (A-Star) para:
- Buscar la ruta óptima entre dos estaciones
- Optimizar según múltiples criterios (tiempo, costo, distancia)
- Calcular funciones de evaluación heurística admisibles

#### Características:
- Algoritmo A* garantiza encontrar la ruta óptima
- Heurística euclidiana para admisibilidad
- Análisis completo de rutas (métricas, transferencias, líneas utilizadas)
- Comparación entre diferentes criterios de optimización

## 🔧 Componentes Principales

### Base de Conocimiento

```python
from base_conocimiento import BaseConocimiento

# Crear instancia
bc = BaseConocimiento()

# Agregar nueva estación
bc.agregar_estacion('Estacion_Nueva', (10, 15))

# Agregar nueva línea
bc.agregar_linea('Linea_Naranja', 
                 ['A_Centro', 'Estacion_Nueva', 'B_Este'],
                 tiempo_viaje=2,
                 costo=2500)

# Obtener información
lineas = bc.obtener_lineas_estacion('A_Centro')
estaciones_conexas = bc.obtener_estaciones_conexas('A_Centro')
```

### Motor de Inferencia

```python
from motor_inferencia import MotorInferencia

# Crear motor
motor = MotorInferencia(base_conocimiento)

# Ejecutar inferencia
motor.inferir()  # Aplica todas las reglas

# Consultar hechos derivados
conexiones = base_conocimiento.hechos_derivados['conexiones']
puntos_transferencia = base_conocimiento.hechos_derivados['puntos_transferencia']
```

### Sistema de Rutas

```python
from sistema_rutas import SistemaRutas

# Crear sistema
sr = SistemaRutas(base_conocimiento)

# Buscar ruta optimizada por tiempo
ruta_rapida = sr.buscar_ruta_optima('A_Centro', 'B_Este', criterio='tiempo')

# Buscar ruta optimizada por costo
ruta_economica = sr.buscar_ruta_optima('A_Centro', 'B_Este', criterio='costo')

# Comparar todos los criterios
comparacion = sr.comparar_rutas('A_Centro', 'B_Este')
```

## 📊 Estructura de Datos de Resultado

Cuando se busca una ruta, el sistema retorna:

```python
{
    'ruta': ['Est_A', 'Est_B', 'Est_C'],          # Secuencia de estaciones
    'pasos': [                                     # Detalles de cada paso
        {
            'origen': 'Est_A',
            'destino': 'Est_B',
            'linea': 'Linea_Roja',
            'tiempo': 2,
            'costo': 2500,
            'distancia': 3.5
        },
        ...
    ],
    'tiempo_total': 10,                            # Minutos
    'costo_total': 7500,                           # Pesos
    'distancia_total': 8.5,                        # Kilómetros
    'lineas_utilizadas': ['Linea_Roja', 'Linea_Azul'],
    'num_lineas': 2,
    'transferencias': 1,                           # Cambios de línea
    'criterio_optimizado': 'tiempo',
    'exitosa': True
}
```

##  Cómo usar

### Ejecutar el programa completo

```bash
python main.py
```

Esto iniciará:
1. Carga de la base de conocimiento
2. Proceso de inferencia de reglas
3. Ejemplos automáticos de búsqueda de rutas
4. Menú interactivo

### Uso programático

```python
from base_conocimiento import BaseConocimiento
from motor_inferencia import MotorInferencia
from sistema_rutas import SistemaRutas

# Iniciación
bc = BaseConocimiento()
motor = MotorInferencia(bc)
motor.inferir()

sr = SistemaRutas(bc)

# Buscar ruta
resultado = sr.buscar_ruta_optima('A_Centro', 'B_Este', 'tiempo')

# Analizar resultado
print(f"Ruta: {resultado['ruta']}")
print(f"Tiempo: {resultado['tiempo_total']} min")
print(f"Costo: ${resultado['costo_total']}")
print(f"Transferencias: {resultado['transferencias']}")
```

## 📐 Algoritmo A* Explicado

### Función de evaluación
```
f(n) = g(n) + h(n)
```

- **g(n)**: Costo real desde inicio hasta nodo n
- **h(n)**: Heurística estimada desde n hasta destino
- **f(n)**: Costo total estimado

### Heurística utilizada
```
h(n) = Distancia_Euclidiana / Velocidad_Estimada
```

### Ventajas
✓ Garantiza encontrar la ruta óptima
✓ Más eficiente que Dijkstra en espacios grandes
✓ Admisible (nunca sobrestima)

##  Reglas Lógicas Implementadas

### Regla 1: Conectividad Directa
```
SI (estación1 ∈ línea) ∧ (estación2 ∈ línea) ∧ (adyacentes)
ENTONCES (conectividad_directa(estación1, estación2))
```

### Regla 2: Proximidad Geográfica
```
SI distancia_euclidiana(est1, est2) ≤ 3km
ENTONCES (alternativa(est1, est2))
```

### Regla 3: Punto de Transferencia
```
SI cuenta_líneas(estación) > 1
ENTONCES (es_punto_transferencia(estación))
```

##  Funcionalidades Principales

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `buscar_ruta_optima()` | Encuentra la mejor ruta según criterio | `sr.buscar_ruta_optima('A', 'B', 'tiempo')` |
| `comparar_rutas()` | Compara rutas por varios criterios | `sr.comparar_rutas('A', 'B')` |
| `obtener_lineas_estacion()` | Obtiene líneas de una estación | `bc.obtener_lineas_estacion('Centro')` |
| `obtener_estaciones_conexas()` | Estaciones directamente conectadas | `bc.obtener_estaciones_conexas('Centro')` |
| `agregar_estacion()` | Añade nueva estación | `bc.agregar_estacion('Nueva', (5, 5))` |
| `agregar_linea()` | Añade nueva línea de transporte | `bc.agregar_linea('Roja', [...], 2, 2500)` |

##  Ejemplos de Uso

### Ejemplo 1: Búsqueda por tiempo mínimo
```python
resultado = sistema_rutas.buscar_ruta_optima('A_Centro', 'B_Este', 'tiempo')
# Ruta: ['A_Centro', 'C_Intermedia1', 'B_Este']
# Tiempo: 4 minutos
```

### Ejemplo 2: Búsqueda por costo mínimo
```python
resultado = sistema_rutas.buscar_ruta_optima('A_Centro', 'B_Este', 'costo')
# Ruta puede ser diferente si hay líneas más caras
```

### Ejemplo 3: Análisis de transferencias
```python
resultado = sistema_rutas.buscar_ruta_optima('A_Norte', 'D_Conexion', 'tiempo')
print(f"Transferencias: {resultado['transferencias']}")
print(f"Líneas: {resultado['lineas_utilizadas']}")
```

##  Análisis de Complejidad

- **Complejidad Espacial**: O(V + E) donde V=estaciones, E=conexiones
- **Complejidad Temporal**: O((V + E) log V) para A*
- **Base de Conocimiento**: O(1) acceso a hechos
- **Inferencia**: O(n²) en el peor caso (n=número de estaciones)

##  Archivos del Proyecto

```
python_Actividad2/
├── base_conocimiento.py      # Almacenamiento de hechos y reglas
├── motor_inferencia.py        # Forward chaining y derivación de hechos
├── sistema_rutas.py          # Algoritmo A* y búsqueda de rutas
├── main.py                   # Programa principal e interfaz
└── README.md                 # Esta documentación
```

##  Casos de Uso

1. **Planificación de viajes**: Encontrar la ruta más rápida
2. **Optimización de costos**: Encontrar la ruta más económica
3. **Minimización de distancia**: Encontrar la ruta más corta
4. **Análisis de transferencias**: Identificar cambios de línea necesarios
5. **Planificación urbana**: Analizar puntos críticos del transporte

##  Extensiones Posibles

- Incluir horarios y disponibilidad de buses
- Añadir restricciones de accesibilidad
- Integrar datos en tiempo real
- Incorporar preferencias de usuario (no usar cierta línea, etc.)
- Análisis de congestión
- Sistema de recomendaciones
