# Algoritmos en C#

Este proyecto contiene implementaciones de algoritmos clásicos en C#, con sus respectivas pruebas unitarias.

## Carpetas

- `Algoritmos.Core` → Algoritmos implementados
- `Algoritmos.Tests` → Pruebas con xUnit

## Para correr las pruebas

``` dotnet test```

# Algoritmos en Python

Este proyecto contiene implementaciones de algoritmos clásicos (búsqueda y ordenamiento) en Python, junto con pruebas unitarias usando `pytest`.

## Estructura

- `sorting/` → Algoritmos de ordenamiento
- `searching/` → Algoritmos de búsqueda
- `tests/` → Pruebas unitarias

## Requisitos


### Crear un entorno virtual
`python -m venv venv`

### Activar (depende del sistema operativo)
#### En Windows:
`venv\Scripts\activate`
### En macOS/Linux:
`source venv/bin/activate`

#### Ahora puedes instalar cosas con pip y quedan dentro del venv
`pip install pytest`
o
`pip install -r requirements.txt`

#### Al terminar, desactivar (opcional)
`deactivate`
