# -*- coding: utf-8 -*-
import os
import json

proyectos = []

try:
    for carpeta in os.listdir('proyectos'):
        path_carpeta = os.path.join('proyectos', carpeta)
        if os.path.isdir(path_carpeta):
            # Suponiendo que siempre hay un index.html y un video.mp4
            proyecto_html = os.path.join(path_carpeta, 'index.html')
            proyecto_video = os.path.join(path_carpeta, 'video.mp4')

            with open(proyecto_html, 'r', encoding='utf-8') as f_html:
                contenido_html = f_html.read()

            proyecto = {
                'titulo': carpeta,
                'link': proyecto_html,
                'video': proyecto_video,
                'descripcion': 'Descripción generada automáticamente'
            }
            proyectos.append(proyecto)

    with open('data/proyectos.json', 'w', encoding='utf-8') as json_file:
        json.dump(proyectos, json_file, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"Error al procesar: {e}")

