# Calculadora de Ventas

Una aplicación web desarrollada con Streamlit para calcular ventas de manera rápida y sencilla. Permite agregar productos, establecer precios, gestionar cantidades y exportar los resultados a CSV.

## 🚀 Características

- ➕ Agregar múltiples productos
- 💰 Establecer precios individuales
- 🔢 Aumentar/disminuir cantidades con botones intuitivos
- 🗑️ Eliminar productos
- 💾 Exportar resultados a CSV
- 📊 Cálculo automático de subtotales y total general

## 📋 Requisitos

- Python 3.8 o superior
- Streamlit
- Pandas

## 🛠️ Instalación Local

1. Clona este repositorio:
```bash
git clone <tu-repositorio>
cd ez_paladar
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run paladar.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## ☁️ Despliegue en Streamlit Cloud

### Paso 1: Preparar el repositorio

Asegúrate de tener los siguientes archivos en tu repositorio:

- `paladar.py` (archivo principal de la aplicación)
- `requirements.txt` (dependencias del proyecto)

### Paso 2: Crear requirements.txt

Crea un archivo `requirements.txt` con el siguiente contenido:

```
streamlit>=1.28.0
pandas>=2.0.0
```

### Paso 3: Subir a GitHub

1. Inicializa un repositorio Git (si aún no lo has hecho):
```bash
git init
git add .
git commit -m "Initial commit"
```

2. Crea un repositorio en GitHub y súbelo:
```bash
git remote add origin https://github.com/tu-usuario/ez_paladar.git
git branch -M main
git push -u origin main
```

### Paso 4: Desplegar en Streamlit Cloud

1. Ve a [share.streamlit.io](https://share.streamlit.io)
2. Inicia sesión con tu cuenta de GitHub
3. Haz clic en "New app"
4. Selecciona tu repositorio: `tu-usuario/ez_paladar`
5. En "Main file path", ingresa: `paladar.py`
6. Haz clic en "Deploy"

### Paso 5: Configuración (Opcional)

Si necesitas variables de entorno o configuración adicional, puedes agregarlas en la sección "Advanced settings" durante el despliegue.

## 📁 Estructura del Proyecto

```
ez_paladar/
├── paladar.py          # Archivo principal de la aplicación
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Este archivo
```

## 🎯 Uso

1. **Agregar productos**: Haz clic en el botón "➕ Agregar producto"
2. **Editar nombre**: Haz clic en el campo de texto del nombre del producto
3. **Establecer precio**: Usa el campo numérico para ingresar el precio
4. **Ajustar cantidad**: Usa los botones ➖ y ➕ para disminuir o aumentar la cantidad
5. **Eliminar producto**: Haz clic en el botón 🗑️ para eliminar un producto
6. **Exportar resultados**: Haz clic en "💾 Guardar resultados (CSV)" para descargar un archivo CSV con todos los productos y sus subtotales

## 📝 Notas

- Los cálculos se actualizan automáticamente cuando cambias precios o cantidades
- El total general se muestra al final de la página
- Los datos se mantienen en la sesión mientras navegas por la aplicación

## 🔧 Solución de Problemas

### Error al desplegar en Streamlit Cloud

- Verifica que el archivo `requirements.txt` esté presente y contenga todas las dependencias
- Asegúrate de que el nombre del archivo principal en "Main file path" sea correcto (`paladar.py`)
- Revisa los logs en Streamlit Cloud para ver errores específicos

### La aplicación no carga localmente

- Verifica que todas las dependencias estén instaladas: `pip install -r requirements.txt`
- Asegúrate de estar usando Python 3.8 o superior
- Ejecuta `streamlit --version` para verificar la instalación de Streamlit

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👤 Autor

Desarrollado para ayudar a mi novia a cuadrar la caja en su paladar :)

---

¿Necesitas ayuda? Abre un issue en el repositorio o contacta al desarrollador.

