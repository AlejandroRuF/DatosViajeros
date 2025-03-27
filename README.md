# AutoDatosViajeros

## 🇪🇸 Aplicación para la generación automática de XML válidos para el alta masiva de viajeros

Esta aplicación ha sido desarrollada con el objetivo de ayudar a **alojamientos turísticos** (casas rurales, hoteles, apartamentos, etc.) a cumplir con el **Real Decreto 933/2021**, que obliga a registrar y comunicar los datos de los viajeros de forma digital al Ministerio del Interior en España.

✅ **AutoDatosViajeros** genera **archivos XML válidos** para subir al sistema de comunicaciones de viajeros de forma masiva, ahorrando tiempo y evitando errores manuales.

---

## 🛠 ¿Qué hace esta app?

- Carga automáticamente los datos de viajeros, contratos y establecimiento desde archivos **Excel o CSV**.
- Valida que todos los campos obligatorios estén presentes.
- Transforma los datos a una estructura XML válida según las especificaciones oficiales.
- Permite usar la app desde el código fuente (`Main.py`) o desde el ejecutable (`AutoDatosViajeros.exe`).

---

## 📂 Archivos requeridos

Debes tener los siguientes archivos en la misma carpeta que el ejecutable (`.exe`) o que `Main.py`:

- `DatosEstablecimiento.xlsx` → Información del alojamiento (nombre, dirección, etc.)
- `DatosContrato.xlsx` → Información del contrato (fechas, forma de pago...)
- `DatosViajeros.xlsx` → Información de cada persona alojada (nombre, documento, dirección...)

> 💡 **Recomendamos usar los Excel ya creados** y no hacerlos desde cero, ya que incluyen listas desplegables y validaciones que te ayudan a evitar errores comunes.

---

## 🚀 ¿Cómo se usa?

### Opción 1: Desde el ejecutable (sin necesidad de Python)
1. Coloca los archivos `.xlsx` en la misma carpeta que `AutoDatosViajeros.exe`.
2. Haz doble clic sobre el `.exe`.
3. Sigue las instrucciones que aparecen en pantalla para seleccionar cada archivo.
4. Se generará un archivo XML listo para subir.

### Opción 2: Desde el código fuente
1. Asegúrate de tener Python 3.8+ instalado.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Coloca los archivos `.xlsx` en la misma carpeta que `Main.py`.
4. Ejecuta el programa:
   ```bash
   python Main.py
   ```

---

## 💾 Formatos de archivo compatibles

- `.xlsx`, `.xls`, `.xlsm`, `.xlsb` (Excel)
- `.odf` (OpenDocument Spreadsheet)
- `.csv` (valores separados por comas)

---

## 📄 Estructura del XML generado

El XML incluirá:

- Datos del establecimiento
- Información del contrato (fechas, forma de pago…)
- Datos de cada viajero
- Códigos oficiales de documento, país y parentesco

🧩 Compatible con la **carga masiva de partes de entrada** en la web oficial del Ministerio del Interior.

---

## ✏️ Personalización

Si tienes conocimientos de programación, eres **libre de adaptar y modificar el código** para ajustarlo a las particularidades de tu alojamiento o gestión de reservas.

---

## 📌 Requisitos (solo si usas el código fuente)

- Python 3.8 o superior
- Dependencias (instalables con `requirements.txt`):
  - `pandas`
  - `openpyxl`
  - `odfpy` (si usas `.odf`)
  - `lxml`

---

## ℹ️ Información adicional

- [Texto completo del Real Decreto 933/2021 (BOE)](https://www.boe.es/eli/es/rd/2021/10/26/933)

---

## 🧑‍💻 Autor

Esta herramienta ha sido desarrollada como apoyo práctico para pequeños alojamientos turísticos. Puedes adaptarla, mejorarla o compartirla libremente.

---
