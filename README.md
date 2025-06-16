
# Trabajo Práctico Obligatorio - Fundamentos de Informática
# UADE | 2025

## 🏁 Aplicación para gestionar tiempos de carreras

### 📌 Integrantes - Grupo Nº 4
- Citoler, Martin Alejo
- Pantano, Ma. Alejandra
- Reverter, Santiago 
- Ruffo, Eduardo Gabriel 

### 👨‍🏫 Profesor
- Maquieira, Guillermo Ramiro  
- 1º Cuatrimestre – Año 2025  
- Curso: Miércoles - Virtual  

---

## 📋 Consigna

Dentro de una lista de ejercicios propuestos, el grupo eligió desarrollar el Ejercicio Nº 3. Este consiste en implementar un programa que permita registrar los tiempos de carrera de N ciclistas, donde:

- N se ingresa por teclado.
- Cada ciclista tiene un nombre, un número único asignado aleatoriamente y un tiempo expresado en horas, minutos y segundos.
  
El programa debe permitir:
1. Mostrar al ganador (el corredor con menor tiempo).
2. Ingresar un tiempo récord y comparar si el ganador lo superó.
3. Calcular y mostrar el tiempo promedio de todos los ciclistas.

---

## 🛠️ Tecnologías usadas
- Lenguaje: Python 3.13.3

---

## 📄 Archivos del proyecto

- `main.py`: contiene el flujo principal del programa y las interacciones con el usuario.
- `funciones.py`: contiene todas las funciones auxiliares necesarias para el funcionamiento del programa.

---

## ▶️ Ejecución del programa

Para correr la aplicación:

```bash
python: main.py
```
## 🧭 Interacción del usuario

El sistema irá guiando al usuario con preguntas como:

- **Nombre de la carrera**
- **Cantidad de corredores** (entre 1 y 10)
- **Nombre del corredor**
- **Tiempo del corredor**, ingresado en formato:
  - Horas
  - Minutos
  - Segundos
- Si desea:
  - Ver al ganador
  - Ingresar un tiempo récord y compararlo
  - Mostrar el promedio de los tiempos registrados

---

## 💡 Ejemplo de salida

Ingrese el nombre de la carrera: Vuelta Tandil 2025

Ingrese la cantidad de corredores (máximo 10): 3

Ingrese nombre del corredor: Ana

Ingrese el tiempo del corredor (formato hh mm ss):

Horas: 1
Minutos: 2
Segundos: 30

Ingrese nombre del corredor: Bruno

Ingrese el tiempo del corredor (formato hh mm ss):

Horas: 1
Minutos: 5
Segundos: 10

Ingrese nombre del corredor: Carla

Ingrese el tiempo del corredor (formato hh mm ss):

Horas: 0
Minutos: 59
Segundos: 45

¿Desea ver al ganador? (si/no): si

El ganador es Carla con un tiempo de 0h 59m 45s y el número de corredor 2

¿Desea ingresar el tiempo record? (si/no): si

Ingrese el tiempo récord (formato hh mm ss):

Horas: 1
Minutos: 0
Segundos: 0

Se ha roto el tiempo record. El nuevo tiempo record es: 3585

Es decir: 0h 59m 45s

¿Desea ver el promedio de tiempos? (si/no): si

El promedio de tiempo de los corredores es: 3815.0 segundos

Es decir: 1h 3m 35s


---

## ✅ Validaciones implementadas

- Verificación de que el nombre de la carrera y los corredores no estén vacíos.
- Control de cantidad de corredores entre 1 y 10.
- Validación de tiempo (horas ≥ 0, minutos y segundos entre 0 y 59).
- Conversión y visualización de los tiempos en formato `hh:mm:ss`.

---

## 📚 Bibliografía y recursos consultados

- Apuntes de clase - Fundamentos de Informática (2025)  
- [Documentación oficial de Python](https://docs.python.org/3/)

---

## 📚 Documento proyecto
 
- [TPO fundamentos de la informatica](https://docs.google.com/document/d/1vkaL4kkrKlzmJWq4H-NaXZ0RkJ0eqDnaNXrUZaiTOgk/edit?usp=sharing)
