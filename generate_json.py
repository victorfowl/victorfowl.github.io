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
                    acumulador = ""  # Acumula líneas hasta encontrar la siguiente sección
                    for linea in f_txt:
                        linea = linea.strip()

                        # Si la línea comienza con #, es una nueva sección
                        if linea.startswith("#"):
                        
                            # Determinar la sección actual basada en la línea
                            if "Descripcion corta" in linea.lower():
                                seccion_actual = "descripcion corta"
                            elif "Descripcion larga" in linea.lower():
                                seccion_actual = "descripcion larga"
                            elif "Empresa" in linea.lower():
                                seccion_actual = "empresa"
                            elif "Plataformas" in linea.lower():
                                seccion_actual = "plataformas"
                            elif "Aportacion" in linea.lower():
                                seccion_actual = "aportacion"
                            elif "Etiquetas" in linea.lower():
                                seccion_actual = "etiquetas"

                            if seccion_actual == "descripcion corta":
                                descripcion_corta = acumulador.strip()
                            elif seccion_actual == "descripcion larga":
                                descripcion_larga = acumulador.strip()
                            elif seccion_actual == "empresa":
                                empresa = acumulador.strip()
                            elif seccion_actual == "plataformas":
                                plataformas = acumulador.strip()
                            elif seccion_actual == "aportacion":
                                aportacion = acumulador.strip()
                            acumulador = ""  # Reiniciar acumulador para la nueva sección
                        
                        # Acumular las líneas que pertenecen a la sección actual
                        else:
                            acumulador += linea + " "

                    # Guardar la última sección al llegar al final del archivo
                    if seccion_actual == "descripcion corta":
                        descripcion_corta = acumulador.strip()
                    elif seccion_actual == "descripcion larga":
                        descripcion_larga = acumulador.strip()
                    elif seccion_actual == "empresa":
                        empresa = acumulador.strip()
                    elif seccion_actual == "plataformas":
                        plataformas = acumulador.strip()
                    elif seccion_actual == "aportacion":
                        aportacion = acumulador.strip()

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
