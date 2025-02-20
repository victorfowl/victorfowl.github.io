# -*- coding: utf-8 -*-
import os
import json

proyectos = []

try:
    for carpeta in os.listdir('proyectos'):
        path_carpeta = os.path.join('proyectos', carpeta)
        if os.path.isdir(path_carpeta):
            proyecto_html = os.path.join(path_carpeta, 'index.html')
            proyecto_txt = os.path.join(path_carpeta, 'description.txt')
            proyecto_video = None
            proyecto_imagen = None
            link_videos = []

            # Leer la descripción del archivo .txt
            descripcion_corta = ""
            descripcion_larga = ""
            empresa = ""
            plataformas = ""
            aportacion = ""
            etiquetas = []
            
            if os.path.exists(proyecto_txt):
                with open(proyecto_txt, 'r', encoding='utf-8') as f_txt:
                    seccion_actual = None
                    for linea in f_txt:
                        linea = linea.strip()
                        if linea.startswith("#"):
                            etiquetas.append(linea[1:].lower())  # Guardar etiquetas en minúsculas
                        elif "Descripción corta" in linea:
                            seccion_actual = "corta"
                        elif "Descripción larga" in linea:
                            seccion_actual = "larga"
                        elif "Empresa" in linea:
                            seccion_actual = "empresa"
                        elif "Plataformas" in linea:
                            seccion_actual = "plataformas"
                        elif "Aportación" in linea:
                            seccion_actual = "aportacion"
                        elif "Enlaces de video" in linea:
                            seccion_actual = "video"
                        else:
                            if seccion_actual == "corta":
                                descripcion_corta += linea + " "
                            elif seccion_actual == "larga":
                                descripcion_larga += linea + " "
                            elif seccion_actual == "empresa":
                                empresa = linea
                            elif seccion_actual == "plataformas":
                                plataformas = linea
                            elif seccion_actual == "aportacion":
                                aportacion = linea
                            elif seccion_actual == "video":
                                link_videos.append(linea)  # Agregar todos los enlaces de video

            # Si no hay un link de video en la descripción, buscar un video en la carpeta
            if not link_videos:
                video_formats = ['mp4', 'webm', 'ogg']
                for formato in video_formats:
                    potential_video = os.path.join(path_carpeta, f'video.{formato}')
                    if os.path.exists(potential_video):
                        link_videos.append(potential_video)
                        break

            # Si no se encontró video, buscar una imagen
            if not link_videos:
                for archivo in os.listdir(path_carpeta):
                    if archivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        proyecto_imagen = os.path.join(path_carpeta, archivo)
                        break

            # Crear el proyecto con los datos correspondientes
            proyecto = {
                'titulo': carpeta,
                'link': proyecto_html,
                'descripcion_corta': descripcion_corta.strip(),
                'descripcion_larga': descripcion_larga.strip(),
                'empresa': empresa,
                'plataformas': plataformas,
                'aportacion': aportacion,
                'etiquetas': etiquetas,
                'tipo': 'link' if link_videos else 'video' if link_videos else 'imagen',
                'media': link_videos[0] if link_videos else proyecto_imagen,
                'videos': link_videos  # Todos los enlaces de video
            }
            proyectos.append(proyecto)

    # Escribir el archivo JSON
    with open('data/proyectos.json', 'w', encoding='utf-8') as json_file:
        json.dump(proyectos, json_file, ensure_ascii=False, indent=4)

except Exception as e:
    print(f"Error al procesar: {e}")
