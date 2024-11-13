# Detector de plagio
## Descripción

El Detector de Plagio es una herramienta avanzada diseñada para identificar y prevenir el plagio en documentos de texto. Utiliza algoritmos sofisticados para comparar el contenido de los documentos y detectar similitudes.

#### Resumen de la Interpretación del Puntaje de Similitud:

- 0: No hay similitud entre los archivos; casi con certeza no hay plagio.
- 0 < puntaje < 0.5: Baja similitud; los archivos pueden tener algunos temas superpuestos o frases comunes, pero probablemente sean diferentes.
- 0.5 < puntaje < 0.8: Similitud moderada; los archivos pueden compartir frases o estructuras significativas, lo que podría sugerir plagio parcial o una fuerte inspiración.
- 0.8 < puntaje < 1: Alta similitud; los archivos son muy similares y probablemente plagiados.
- 1: Contenido idéntico; muy probablemente sea plagio directo.

Este método es útil como una primera capa de detección, aunque no es perfecto.

## Características

- Detección de plagio en archivos Python
- Comparación de dos documentos

## Instalación

Para instalar el Detector de Plagio, sigue estos pasos:
1. Clonar el repositorio 
```bash
git clone https://github.com/Luis-ERP/code-plagarism-detector.git
```

2. Instalar dependencias
```bash
pip install -r requirements.txt
```

3. Instalar recursos de NLTK
```bash
python
```
```python
import nltk
nltk.download('punkt') 
```

## Uso
```bash
python main.py path/to/file1.py path/to/file2.py
```


## Autores

- Luis Edgar Ramriez Perez A01702056
- Juan Manuel González Ascencio A00572003
- Rodolfo Arechiga A01634610

## Profesores

- Dr. Oscar Pedro Pérez Murueta
- Dr. Adolfo Centeno Tellez
- Alexis Edmundo Gallegos Acosta
- Víctor Manuel Rodríguez Bahena

