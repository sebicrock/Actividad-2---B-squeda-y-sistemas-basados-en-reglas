# Guía de Instalación y Configuración

## 1. REQUISITOS DEL SISTEMA

- **Python 3.7+**
- **Pip** (gestor de paquetes)
- **Sistema operativo**: Windows, macOS, Linux
- **Espacio disco**: ~50 MB
- **Dependencias externas**: NINGUNA (solo librerías estándar)

## 2. INSTALACIÓN PASO A PASO

### 2.1 Verificar Python
```bash
python --version
# o
python3 --version
```

### 2.2 Descargar el proyecto
- Descargue los archivos en una carpeta local
- O clone desde repositorio si existe

### 2.3 No requiere instalación adicional
✓ El sistema usa solo librerías estándar de Python  
✓ No necesita `pip install` de paquetes externos

## 3. ESTRUCTURA DE ARCHIVOS

```
python_Actividad2/
├── base_conocimiento.py       # Base de hechos y reglas
├── motor_inferencia.py         # Motor de forward chaining
├── sistema_rutas.py           # Algoritmo A* para búsqueda
├── main.py                    # Programa principal
├── ejemplos_avanzados.py      # Ejemplos avanzados
├── test_sistema.py            # Pruebas unitarias
├── CONFIGURACION.md           # Este archivo
└── README.md                  # Documentación
```

## 4. EJECUCIÓN DEL PROGRAMA

### 4.1 Ejecutar programa principal
```bash
python main.py
```

Esto ejecutará:
1. Carga de base de conocimiento
2. Proceso de inferencia de reglas
3. Ejemplos automáticos
4. Menú interactivo

### 4.2 Ejecutar ejemplos avanzados
```bash
python ejemplos_avanzados.py
```

### 4.3 Ejecutar pruebas
```bash
python test_sistema.py
```

### 4.4 Usar como módulo
```python
from base_conocimiento import BaseConocimiento
from motor_inferencia import MotorInferencia
from sistema_rutas import SistemaRutas

bc = BaseConocimiento()
motor = MotorInferencia(bc)
motor.inferir()

sr = SistemaRutas(bc)
ruta = sr.buscar_ruta_optima('A_Centro', 'B_Este', 'tiempo')
print(ruta)
```

## 5. CONFIGURACIÓN PERSONALIZADA

### 5.1 Agregar estaciones
```python
bc.agregar_estacion('nombre_estacion', (x, y))
```

### 5.2 Agregar líneas
```python
bc.agregar_linea(
    'nombre_linea',
    ['estacion1', 'estacion2', 'estacion3'],
    tiempo_viaje=2,        # minutos
    costo=2500             # pesos
)
```

### 5.3 Ajustar ciclos de inferencia
```python
motor.max_ciclos = 20
```

## 6. CRITERIOS DE OPTIMIZACIÓN

- **'tiempo'**: Minimiza tiempo de viaje
- **'costo'**: Minimiza costo monetario  
- **'distancia'**: Minimiza distancia recorrida

## 7. ESTRUCTURA DE RESPUESTA

```python
{
    'ruta': ['A', 'B', 'C'],        # Secuencia
    'pasos': [                       # Detalles
        {
            'origen': 'A',
            'destino': 'B',
            'linea': 'Linea_Roja',
            'tiempo': 2,
            'costo': 2500,
            'distancia': 3.5
        }
    ],
    'tiempo_total': 10,              # Minutos
    'costo_total': 7500,             # Pesos
    'distancia_total': 8.5,          # Km
    'lineas_utilizadas': ['Linea_Roja'],
    'transferencias': 0,
    'exitosa': True
}
```

## 8. SOLUCIÓN DE PROBLEMAS

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError` | Verifique que los .py estén juntos |
| "No se encuentran rutas" | Valide nombres de estaciones |
| Ejecución lenta | Reduzca max_ciclos en motor |
| Resultados inesperados | Ejecute `python test_sistema.py` |

## 9. OPTIMIZACIÓN DE RENDIMIENTO

- **Memoria**: O(V + E)
- **Búsqueda**: O((V + E) log V)
- **Inferencia**: O(n²)

Para sistemas grandes:
1. Limitar ciclos de inferencia
2. Optimizar heurística
3. Usar cachés
4. Indexar estaciones

## 10. EXTENSIONES POSIBLES

Compatible con:
- ✓ Bases de datos (SQLite, PostgreSQL)
- ✓ APIs REST (Flask, FastAPI)
- ✓ GUIs (Tkinter, PyQt)
- ✓ Análisis (Pandas, NumPy)
- ✓ Visualización (Matplotlib, Plotly)

---

**¡Sistema listo! Execute: `python main.py`**
