# -*- coding: utf-8 -*-
import os
import json

proyectos = []

try:
    for carpeta in os.listdir('proyectos'):
        path_carpeta = os.path.join('proyectos', carpeta)
        if os.path.isdir(path_carpeta):
            # Suponiendo que siempre hay un index.html, video.mp4 y descripcion.txt
            proyecto_html = os.path.join(path_carpeta, 'index.html')
            proyecto_video = os.path.join(path_carpeta, 'video.mp4')
            proyecto_txt = os.path.join(path_carpeta, 'description.txt')

            # Leer el contenido del archivo HTML
            with open(proyecto_html, 'r', encoding='utf-8') as f_html:
                contenido_html = f_html.read()

            # Leer la descripción del archivo .txt
            descripcion = ""
            if os.path.exists(proyecto_txt):
                with open(proyecto_txt, 'r', encoding='utf-8') as f_txt:
                    descripcion = f_txt.read().strip() 

            # Crear el proyecto con los datos correspondientes
            proyecto = {
                'titulo': carpeta,
                'link': proyecto_html,
                'video': proyecto_video,
                'descripcion': descripcion
            }
            proyectos.append(proyecto)

    # Escribir el archivo JSON
    with open('data/proyectos.json', 'w', encoding='utf-8') as json_file:
        json.dump(proyectos, json_file, ensure_ascii=False, indent=4)

except Exception as e:
    print(f"Error al procesar: {e}")


