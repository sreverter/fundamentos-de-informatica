# app_eventos

Aplicación de escritorio en Python con interfaz gráfica (Tkinter) para la gestión de eventos deportivos y corredores.

---

## Funcionalidades

- Alta de eventos y corredores.
- Búsqueda de eventos por nombre de corredor.
- Visualización de ganadores y tiempos.
- Almacenamiento persistente en archivos JSON.

---

## Estructura del Proyecto tentativo

```
app_eventos/
├── Datos/                     # Archivos JSON de eventos guardados
├── logica/                    # Lógica de aplicación (ABM, filtros, reglas)
│   ├── abm_eventos.py         # Alta y almacenamiento de eventos
│   └── reglas_negocio.py      # Reglas para búsqueda y comparación
├── modelos/                   # Modelo de entidades (Evento, Corredor)
│   └── entidades.py                        
├── pantalla_busqueda.py
├── pantalla_carga.py
└── ventana_principal.py	   # Interfaz gráfica (Tkinter)
└── README.md
```

---

## Requisitos

- Python 3.x
- Tkinter

---

## Ejecución

Pendiente...


---

## Guardado de información en archivo JSON.

- Los eventos se guardan automáticamente en la carpeta `Datos/`.
- El archivo generado tiene el formato:  
  ```
  NombreEvento_FechaEvento.json
  ```
  Ejemplo:
  ```
  Buenos_Aires_Corre_20250310_Maraton.json
  ```

---

## Buscar Eventos

La pantalla de búsqueda

- Nombre del evento
- Fecha
- Lugar

---

## Pendiente

- Carga de archivos JSON existentes.
- Filtros avanzados (por fecha, lugar, etc).
- Visualización de la informacion.

---

## Grupo 4
Santiago
Ale
Martin
Gabriel
Ale


---