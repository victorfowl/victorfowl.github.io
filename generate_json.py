# -*- coding: utf-8 -*-
import os
import json

proyectos = []

try:
    for carpeta in os.listdir('proyectos'):
        path_carpeta = os.path.join('proyectos', carpeta)
        if os.path.isdir(path_carpeta):
            # Definir rutas y variables iniciales
            proyecto_html = os.path.join(path_carpeta, 'index.html')
            proyecto_txt = os.path.join(path_carpeta, 'description.txt')
            proyecto_video = None
            proyecto_imagen = None
            link_video = None

            # Leer la descripción del archivo .txt
            descripcion = ""
            etiquetas = []
            if os.path.exists(proyecto_txt):
                with open(proyecto_txt, 'r', encoding='utf-8') as f_txt:
                    for linea in f_txt:
                        linea = linea.strip()
                        if linea.startswith("#"):
                            etiquetas.append(linea[1:].lower())  # Guardar etiquetas en minúsculas
                        elif linea.startswith("URL:"):
                            link_video = linea.split("URL:", 1)[1].strip()  # Extraer el link del video
                        else:
                            descripcion += linea + "\n"
                    descripcion = descripcion.strip()

            # Si no hay un link de video en la descripción, buscar un video en la carpeta
            if not link_video:
                video_formats = ['mp4', 'webm', 'ogg']
                for formato in video_formats:
                    potential_video = os.path.join(path_carpeta, f'video.{formato}')
                    if os.path.exists(potential_video):
                        proyecto_video = potential_video
                        break

            # Si no se encontró video, buscar una imagen
            if not proyecto_video and not link_video:
                for archivo in os.listdir(path_carpeta):
                    if archivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        proyecto_imagen = os.path.join(path_carpeta, archivo)
                        break

            # Crear el proyecto con los datos correspondientes
            proyecto = {
                'titulo': carpeta,
                'link': proyecto_html,
                'descripcion': descripcion,
                'etiquetas': etiquetas,
                'tipo': 'link' if link_video else 'video' if proyecto_video else 'imagen',
                'media': link_video or proyecto_video or proyecto_imagen
            }
            proyectos.append(proyecto)

    # Escribir el archivo JSON
    with open('data/proyectos.json', 'w', encoding='utf-8') as json_file:
        json.dump(proyectos, json_file, ensure_ascii=False, indent=4)

except Exception as e:
    print(f"Error al procesar: {e}")
